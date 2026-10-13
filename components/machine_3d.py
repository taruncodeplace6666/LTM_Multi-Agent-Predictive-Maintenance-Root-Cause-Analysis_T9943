
from pathlib import Path
import base64
import json
import math

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURATION
# ============================================================

TARGET_NODE_NAME = "Object_170"
EXPECTED_GEOMETRY_NAME = "Object_55"

# Example threshold only: adjust to your sensor's actual units.
X_AXIS_THRESHOLD = 1000.0


# ============================================================
# READ VIBRATION VALUES
# ============================================================

def _get_vibration_value(data, axis):
    if not isinstance(data, dict):
        return 0.0

    keys = [
        axis.upper(),
        axis.lower(),
        f"vibration_{axis.lower()}",
        f"vibration_{axis.upper()}",
    ]

    for key in keys:
        value = data.get(key)

        if value is None:
            continue

        try:
            number = float(value)

            if math.isfinite(number):
                return number

        except (TypeError, ValueError):
            continue

    return 0.0


# ============================================================
# DISPLAY 3D CNC MACHINE
# ============================================================

def display_machine_3d(latest_values=None):

    st.subheader("3D CNC Machine")

    if not isinstance(latest_values, dict):
        latest_values = {}

    vibration = {
        "x": _get_vibration_value(latest_values, "x"),
        "y": _get_vibration_value(latest_values, "y"),
        "z": _get_vibration_value(latest_values, "z"),
    }

    is_anomaly = abs(vibration["x"]) > X_AXIS_THRESHOLD

    # --------------------------------------------------------
    # Find model file
    # --------------------------------------------------------

    model_path = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "cnc_machine.glb"
    )

    if not model_path.exists():
        st.error("CNC 3D model file not found.")
        st.code(str(model_path))
        return

    try:
        model_bytes = model_path.read_bytes()
        model_base64 = base64.b64encode(
            model_bytes
        ).decode("utf-8")

    except OSError as error:
        st.error(f"Could not read the 3D model: {error}")
        return

    # --------------------------------------------------------
    # Debug information
    # --------------------------------------------------------

    with st.expander("Vibration and Model Debug Information"):
        st.write("Input sensor values:", latest_values)
        st.write("Parsed vibration:", vibration)
        st.write("Target node:", TARGET_NODE_NAME)
        st.write("Reference geometry:", EXPECTED_GEOMETRY_NAME)
        st.write("X-axis threshold:", X_AXIS_THRESHOLD)
        st.write("X-axis status:", "ANOMALY" if is_anomaly else "NORMAL")

    # JSON values safely passed into JavaScript.
    vibration_json = json.dumps(vibration)
    target_node_json = json.dumps(TARGET_NODE_NAME)
    expected_geometry_json = json.dumps(EXPECTED_GEOMETRY_NAME)
    threshold_json = json.dumps(X_AXIS_THRESHOLD)

    # --------------------------------------------------------
    # Three.js viewer
    # --------------------------------------------------------

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<script type="importmap">
{{
  "imports": {{
    "three": "https://unpkg.com/three@0.170.0/build/three.module.js",
    "three/addons/": "https://unpkg.com/three@0.170.0/examples/jsm/"
  }}
}}
</script>

<style>
html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    font-family: Arial, sans-serif;
}}

#scene {{
    width: 100%;
    height: 520px;
    position: relative;
}}

#machine {{
    display: block;
    width: 100%;
    height: 100%;
}}

.panel {{
    position: absolute;
    z-index: 5;
    top: 12px;
    left: 12px;
    width: 225px;
    padding: 13px;
    box-sizing: border-box;
    border-radius: 10px;
    color: #ffffff;
    background: rgba(20, 25, 35, 0.94);
    font-size: 13px;
}}

.panel-title {{
    font-weight: bold;
    font-size: 15px;
    margin-bottom: 12px;
}}

.reading {{
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin: 10px 0;
}}

#status {{
    margin-top: 12px;
    padding-top: 10px;
    border-top: 1px solid #666;
    line-height: 1.5;
    white-space: pre-line;
    overflow-wrap: anywhere;
}}

#status.anomaly {{
    color: #ff7777;
}}

#status.normal {{
    color: #8ff0a4;
}}
</style>
</head>

<body>
<div id="scene">

    <canvas id="machine"></canvas>

    <div class="panel">
        <div class="panel-title">CNC Vibration Monitoring</div>

        <div class="reading">
            <span>X Axis</span>
            <b id="vibX">--</b>
        </div>

        <div class="reading">
            <span>Y Axis</span>
            <b id="vibY">--</b>
        </div>

        <div class="reading">
            <span>Z Axis</span>
            <b id="vibZ">--</b>
        </div>

        <div id="status">Loading 3D model...</div>
    </div>

</div>

<script type="module">

import * as THREE from "three";

import {{ OrbitControls }} from
    "three/addons/controls/OrbitControls.js";

import {{ GLTFLoader }} from
    "three/addons/loaders/GLTFLoader.js";


// ============================================================
// CONFIGURATION
// ============================================================

const vibration = {vibration_json};
const targetNodeName = {target_node_json};
const expectedGeometryName = {expected_geometry_json};
const threshold = {threshold_json};

const canvas = document.getElementById("machine");
const statusElement = document.getElementById("status");

let targetNode = null;
let boundMeshes = [];

const originalMaterials = new Map();
const highlightMaterials = new Map();


// ============================================================
// THREE.JS SCENE
// ============================================================

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xf0f2f5);

const camera = new THREE.PerspectiveCamera(
    45, 1, 0.1, 10000
);

const renderer = new THREE.WebGLRenderer({{
    canvas: canvas,
    antialias: true
}});

renderer.setPixelRatio(
    Math.min(window.devicePixelRatio || 1, 2)
);

renderer.outputColorSpace = THREE.SRGBColorSpace;

scene.add(
    new THREE.HemisphereLight(
        0xffffff, 0x555566, 2
    )
);

const directionalLight = new THREE.DirectionalLight(
    0xffffff, 2
);

directionalLight.position.set(200, 300, 250);
scene.add(directionalLight);

const controls = new OrbitControls(
    camera, renderer.domElement
);

controls.enableDamping = true;
controls.autoRotate = true;


// ============================================================
// DISPLAY SENSOR READINGS
// ============================================================

document.getElementById("vibX").textContent =
    vibration.x.toFixed(3);

document.getElementById("vibY").textContent =
    vibration.y.toFixed(3);

document.getElementById("vibZ").textContent =
    vibration.z.toFixed(3);


// ============================================================
// HIGHLIGHT MATERIAL CREATION
// ============================================================

function createHighlightMaterial(material) {{

    const highlighted = material.clone();

    if (highlighted.color) {{
        highlighted.color.set(0xff2020);
    }}

    if (highlighted.emissive) {{
        highlighted.emissive.set(0x660000);
        highlighted.emissiveIntensity = 0.8;
    }}

    return highlighted;
}}


// ============================================================
// APPLY HIGHLIGHT TO BOUND MESHES
// ============================================================

function applyComponentHighlight() {{

    if (boundMeshes.length === 0) {{
        return;
    }}

    const anomaly = Math.abs(vibration.x) > threshold;

    boundMeshes.forEach(mesh => {{

        if (anomaly) {{
            mesh.material = highlightMaterials.get(mesh.uuid);
        }} else {{
            mesh.material = originalMaterials.get(mesh.uuid);
        }}
    }});

    statusElement.className = anomaly ? "anomaly" : "normal";

    statusElement.textContent =
        "Node: " + targetNodeName +
        "\\nMeshes highlighted: " + boundMeshes.length +
        "\\nX-axis: " +
        (anomaly ? "THRESHOLD EXCEEDED" : "NORMAL") +
        "\\nThreshold: " + threshold;
}}


// ============================================================
// LOAD GLB MODEL
// ============================================================

const loader = new GLTFLoader();

try {{

    const binaryString = atob("{model_base64}");
    const modelBytes = new Uint8Array(binaryString.length);

    for (let i = 0; i < binaryString.length; i++) {{
        modelBytes[i] = binaryString.charCodeAt(i);
    }}

    loader.parse(
        modelBytes.buffer,
        "",

        function (gltf) {{

            const model = gltf.scene;
            scene.add(model);

            // -----------------------------------------------
            // Find Object_170 anywhere in the model hierarchy
            // -----------------------------------------------

            model.traverse(object => {{

                if (object.name === targetNodeName) {{
                    targetNode = object;
                }}
            }});

            if (!targetNode) {{

                statusElement.className = "anomaly";

                statusElement.textContent =
                    "Node not found: " + targetNodeName +
                    "\\nOpen browser Console (F12).";

                console.error("Node not found:", targetNodeName);

                model.traverse(object => {{
                    console.log(
                        "Model object:",
                        object.name,
                        "Type:",
                        object.type,
                        "Geometry:",
                        object.geometry?.name
                    );
                }});

                return;
            }}

            // -----------------------------------------------
            // Collect mesh descendants of Object_170
            // -----------------------------------------------

            const meshesUnderNode = [];

            targetNode.traverse(object => {{

                if (object.isMesh) {{
                    meshesUnderNode.push(object);
                }}
            }});

            console.log("Target node:", targetNode.name);

            console.table(
                meshesUnderNode.map(mesh => ({{
                    meshName: mesh.name,
                    geometryName: mesh.geometry?.name,
                    parentName: mesh.parent?.name,
                    uuid: mesh.uuid
                }}))
            );

            // -----------------------------------------------
            // FIX: use all meshes beneath Object_170.
            // Do not require geometry name Object_55 to match.
            // -----------------------------------------------

            boundMeshes = meshesUnderNode;

            if (boundMeshes.length === 0 && targetNode.isMesh) {{
                boundMeshes = [targetNode];
            }}

            if (boundMeshes.length === 0) {{

                statusElement.className = "anomaly";

                statusElement.textContent =
                    "Node found: " + targetNodeName +
                    "\\nNo mesh exists under this node." +
                    "\\nInspect Console (F12).";

                console.error(
                    "Target node contains no meshes:",
                    targetNode
                );

                return;
            }}

            // -----------------------------------------------
            // Save original materials and create red materials
            // -----------------------------------------------

            boundMeshes.forEach(mesh => {{

                originalMaterials.set(
                    mesh.uuid, mesh.material
                );

                const redMaterial = Array.isArray(mesh.material)
                    ? mesh.material.map(createHighlightMaterial)
                    : createHighlightMaterial(mesh.material);

                highlightMaterials.set(
                    mesh.uuid, redMaterial
                );
            }});

            console.log("Mesh binding successful.");

            console.log(
                "Expected geometry name from inspection:",
                expectedGeometryName
            );

            console.log(
                "Meshes currently bound:",
                boundMeshes.map(mesh => mesh.name)
            );

            // Apply current reading to the model.
            applyComponentHighlight();

            // -----------------------------------------------
            // Fit camera to model
            // -----------------------------------------------

            const box = new THREE.Box3().setFromObject(model);
            const size = box.getSize(new THREE.Vector3());
            const center = box.getCenter(new THREE.Vector3());

            const maxDimension =
                Math.max(size.x, size.y, size.z) || 100;

            controls.target.copy(center);

            camera.position.set(
                center.x + maxDimension * 1.5,
                center.y + maxDimension * 1.2,
                center.z + maxDimension * 1.5
            );

            camera.near = Math.max(maxDimension / 1000, 0.01);
            camera.far = maxDimension * 100;

            camera.updateProjectionMatrix();
            controls.update();
        }},

        function (error) {{

            console.error("GLB parsing error:", error);

            statusElement.className = "anomaly";

            statusElement.textContent =
                "Failed to load the model." +
                "\\nCheck browser Console (F12).";
        }}
    );

}} catch (error) {{

    console.error("3D viewer initialization failed:", error);

    statusElement.className = "anomaly";

    statusElement.textContent =
        "3D initialization failed." +
        "\\nCheck browser Console (F12).";
}}


// ============================================================
// RENDER LOOP
// ============================================================

function animate() {{

    requestAnimationFrame(animate);

    controls.update();

    const width = canvas.clientWidth;
    const height = canvas.clientHeight;

    if (width > 0 && height > 0) {{

        const pixelRatio = renderer.getPixelRatio();

        if (
            canvas.width !== Math.floor(width * pixelRatio) ||
            canvas.height !== Math.floor(height * pixelRatio)
        ) {{
            renderer.setSize(width, height, false);

            camera.aspect = width / height;
            camera.updateProjectionMatrix();
        }}

        renderer.render(scene, camera);
    }}
}}

animate();

</script>
</body>
</html>
"""

    components.html(
        html,
        height=530,
        scrolling=False
    )
