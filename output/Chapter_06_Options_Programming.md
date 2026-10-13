## Chapter 6: Options Programming

## 6.1 Introduction

In  addition  to  the  standard  functions  included  with  your  machine,  you  may  also  have optional equipment with special programming considerations. This section tells you how to program these options.

You can contact your HFO to purchase most of these options, if your machine did not come equipped with them.

## 6.2 Feature List

The Feature List contains both standard and purchasable options.

## F6.1: Features Tab

<!-- image -->

To access the list:

1. Press [DIAGNOSTIC] .
2. Navigate to the Parameters and then the Features tab. (Purchased options are marked in green and their status is set as PURCHASED.)

## 6.3 Purchased Options Enable/Disable

To enable or disable a purchased option:

1. Highlight the option on the FEATURES tab.
2. Press to turn /
3. [ENTER] ON OFF the option.

If the featured option is turned OFF , the option is not available.

## 6.4 Option Tryout

Some options have a 200-hour tryout available. The FEATURES tab Status column shows the options available for tryout.

<!-- image -->

NOTE:

<!-- image -->

NOTE:

If an option does not have a tryout, the Status column shows FEATURE DISABLED , and you must purchase the option to use it.

To start tryout:

1. Highlight the feature.
2. Press [ENTER] . Press [ENTER] again to disable the option and stop the timer.

The status of the feature changes to TRYOUT ENABLED , and the date column shows the remaining hours left in the tryout period. When the tryout period expires, the status changes to EXPIRED . You cannot extend the tryout time for expired options. You must purchase them to use them.

Tryout time is only updated while the option is enabled.

## 6.5 Rotation and Scaling

Rotation lets you rotate a pattern to another location or around a circumference. Scaling reduces or enlarges a toolpath or pattern.

## 6.6 Visual Programming System (VPS)

VPS lets you quickly build programs from program templates. To access VPS, press [EDIT] and then select the VPS tab.

- F6.2: VPS Starting Screen. [1] Recently Used Templates, [2] Template Directory Window, [3] [ENTER] to Load a Template, [4] [F4] to Switch Between Recently Used and Template Directory.

<!-- image -->

In the template directory window, you can choose from the VPS or CUSTOM directories. Highlight  a  directory  name  and  press  the [RIGHT] cursor  arrow  to  see  the  directory's contents.

The VPS starting screen also lets you choose templates you have recently used. Press [F4] to  change  to  the  Recently  Used  window  and  highlight  a  template  from  the  list.  Press [ENTER] to load the template.

## 6.7 VPS Example

When you use VPS, you choose a template for the function you want to program, and then enter  variables  to  create  a  program.  The  default  templates  include  probing  and  part features. You can also create custom templates. Contact the Applications department at your HFO for help with custom templates.

In this  example, we use a VPS template to program the engraving cycle from the G47 program example in this manual. The G47 description starts on page 347 . VPS templates all work in the same way: You first fill in values for the template variables, and you then output a program.

1. Press [EDIT] , and then select the VPS tab.
2. Use the cursor arrow keys to highlight the VPS menu option. Press the [RIGHT] cursor arrow key to select the option.
3. Highlight and select the Engraving option from the next menu.
4. F6.3: VPS Engraving Program Generation Window Example. [1] Variable Illustration, [2] Variables Table, [3] Variable Description Text, [4] Template Illustration, [5] Generate G-code [F4] , [6] Run in MDI [CYCLE START] , [7] Clear [ORIGIN] , [8] Default value was changed indicator.

<!-- image -->

4. In the Program Generation window, use the [UP] and [DOWN] cursor arrow keys to highlight the variable rows.
5. Type a value for the highlighted variable and press ENTER. The control will display an asterisk (*) next to variable if the default value is changed. To set the variable back to default press the [ORIGIN] button. Press the DOWN cursor arrow key to move to the next variable.

To generate the example engraving cycle, we use these variable values. Note that all of the position values are given in work coordinates.

| Variable     | Description                                                | Value           |
|--------------|------------------------------------------------------------|-----------------|
| WORK_OFFSETS | Work Offset Number                                         | 54              |
| T            | Tool Number                                                | 1               |
| S            | Spindle Speed                                              | 1000            |
| F            | Feedrate                                                   | 15.             |
| M8           | Coolant (1 - YES / 0 - NO)                                 | 1               |
| X            | Starting X Position                                        | 2.              |
| Y            | Starting Y Position                                        | 2.              |
| R            | R-Plane Height                                             | 0.05            |
| Z            | Z Depth                                                    | -0.005          |
| P            | Text or Serial Number Switch (0 - Text, 1 - Serial Number) | 0               |
| J            | Text Height                                                | 0.5             |
| I            | Text Angle (Degrees from Horizontal)                       | 45.             |
| TEXT         | Text to Engrave                                            | TEXT TO ENGRAVE |

6. With all of the variables entered, you can press [CYCLE START] to immediately run the program in MDI, or F4 to output the code to either the clipboard or MDI without running the program.

This VPS template creates a program with the specified variables to engrave the text:

```
% O11111 ; (Engraving) ; ( TOOL 1 ) ; ( SPINDLE 1000 RPM / FEED 15. ) ; ( DEPTH -0.005 ) ; T1 M06 ; G00 G90 G54 X2. Y2. S1000 M03 ; G43 Z0.05 H1 ; M08 ; G00 G90 G54 X2. Y2. ; ( TEXT ENGRAVING : TEXT TO ENGRAVE ) ; G47 E7.5000 F15. I45. J.5 P0 R0.05 Z-0.005 (TEXT TO ENGRAVE) ; G0 Z0.05 M09 ; M05 ; G91 G28 Z0. ; G91 G28 Y0. ; M01 ( END ENGRAVING ) ; %
```

## 6.8 Rigid Tapping

This option synchronizes the spindle's RPM with the feedrate during a tapping operation.

## 6.9 M19 Spindle Orientation

The Spindle Orientation lets you position the spindle to a programmed angle. This option provides inexpensive, accurate positioning. For more information about M19, refer to page 439 .

## 6.10 High-Speed Machining

The  Haas  high-speed  machining  option  allows  faster  feedrates  and  more  complex toolpaths. HSM uses a motion algorithm called Acceleration Before Interpolation combined with full look-ahead to provide contouring feeds up to 1200 ipm (30.5 m/min) without risk of distortion  to  the  programmed  path.  This  reduces  cycle  times,  improves  accuracy,  and smooths motion.

## 6.11 Additional Memory Options

This option expands the on-board solid-state memory and allows the control to store, run, and edit large programs directly at the machine.

## 6.12 Probing

You can use an optional probe system to set offsets, check work, measure tools, and check tools. This section describes basic probe use and troubleshooting.

## 6.12.1 Check Tool Probe

Do these steps to make sure the tool probe operates correctly:

## F6.4: Tool Probe Test

<!-- image -->

1. In MDI mode, run:

M59 P2 ;

G04 P1.0 ;

M59 P3 ;

This turns on tool probe communication, delays one second, and turns on the tool probe. The LED [1] on the tool probe flashes green.

2. Touch the stylus [2].

The machine makes a "beep" sound and the LED becomes red [1]. This tells you that the tool probe is started.

3. Press [RESET] to deactivate the probe.

The probe LED [1] turns off.

## 6.12.2 Check Work Probe

Do these steps to make sure the work probe operates correctly:

## F6.5: Work Probe Test

<!-- image -->

1. Select the work probe with a tool change, or manually insert the work probe into the spindle.
2. In MDI mode, run M69 P2 ;

This starts communication with the work probe.

3. in MDI mode: run M59 P3 ;

The probe LED flashes green [1].

4. Touch the stylus [2].

The machine makes a "beep" sound and the LED becomes red [3]. This tells you that the work probe is started.

5. Press [RESET] to deactivate the probe.

The work probe LED turns off [1].

## 6.12.3 Probe Example

You  can  use  a  probe  to  check  your  part  for  correct  dimensions  during  the  machining process. For example, this program uses the work probe to check for squareness. The program uses G65 to call 9XXXXX macro programs created specifically for probing. You can find  more information  on these  programs in  the Renishaw  manuals  on the  web  at www.haascnc.com then click on the Service tab.

The program does the following:

1. After a tool change, home, and adding tool length compensation, the system turns on the work probe and moves to a safe start location.
2. The probe stylus moves adjacent to the surface at the required Z-Axis point to provide a central start position [1].
3. The cycle makes two measurements, symmetrically about the start position, to establish the surface angle [2], [3].
4. Finally, the probe stylus moves to its safe out position, tuns off the probe, and returns home.

## F6.6: Check for Square: [1] Safe Move Position, [2] First Measurement, [3] Second Measurement

<!-- image -->

Example:

```
% O00010 (CHECK FOR SQUARE) ; T20 M06 (PROBE) ;
```

```
G00 G90 G54 X0. Y0. ; G43 H20 Z6. ; G65 P9832 (WORK PROBE ON) ; G65 P9810 Z-0.5 F100. (SAFE MOVE) ; G65 P9843 Y-0.5 D0.5 A15. (ANGLE MEAS.) ; G65 P9810 Z6. F100. (SAFE OUT) ; G65 P9833 (WORK PROBE OFF) ; G00 G90 G53 Z0. ; M01 ; ; ; ( PART PROGRAM ) ; G00 G90 G54 X0. Y0. ; T2 M06 (1/2" END MILL) ; G00 G90 G43 H02 Z1.5 ; G68 R#189 ; G01 X-2. F50. ; M30 ; %
```

## 6.12.4 Probe Use with Macros

Macro statements select and turn on and off the probe the same as M-codes.

## T6.1: Probe Macro Values

| M-Code   | System Variable   |   Macro Value | Probe               |
|----------|-------------------|---------------|---------------------|
| M59 P2 ; | #12002            |      1.000000 | Tool Probe Selected |
| M69 P2 ; | #12002            |      0.000000 | Work Probe Selected |
| M59 P3 ; | #12003            |      1.000000 | Probe Enable        |
| M69 P3 ; | #12003            |      0.000000 | Probe Disable       |

If you assign the system variable to a viewable global variable, you can see the macro value change in the Macro Vars tab under [CURRENT COMMANDS] .

For example,

```
M59 P3 ; #10003=#12003 ;
```

The global variable #10003 shows the output from M59 P3 ; as 1.000000. This means that either the tool probe or work probe is on.

## 6.12.5 VPS Probe Operations

VPS offers templates to simplify probe operations in (3) categories: Tool Setting, Spindle Probe, and Calibration. Select PROBING in the VPS menu and then select a template. Fill in the variable fields to generate the probing code. Refer to the VPS section of this manual for more information on using VPS templates.

VPS Probe Example (Tool Probe Calibration)

F6.7: Tool Probe Calibration Screen

<!-- image -->

To calibrate the tool probe:

1. In VPS, select PROBING &gt; CALIBRATION &gt; Tool Probe Calibration .
2. Enter the Calibration Tool Length (L), the Calibration Tool Diameter (S), and the Table Side of the Probe (D).
3. Press [CYCLE START] to run the program, or F4 to generate the code to the clipboard or MDI.

## 6.12.6 Probe Troubleshooting

If you cannot get the tool or work probe to beep or flash, do these steps:

1. In [MDI] mode, run M69 P2 ; to select the spindle work probe or M59 P2 ; to select the table tool probe.
2. Run M59 P3 ; to make the probe flash.
3. To check the I/O values for the probe, press [DIAGNOSTIC] and select the Diagnostics tab, then the I/O tab.
4. Type PROBE and press [F1] to search for I/O items that contain the word 'probe.'
5. Check the table for proper probe values. For example, Output 2 with a value of 0 selects the work probe.
6. If you are using the correct I/O values in your programs, but the probe does not flash or beep, check the batteries in the probes, and then check the wired connections to the control.

| Type   |   Numbe r | M-code   | M-code   | Name                  |   Value | Probe    |
|--------|-----------|----------|----------|-----------------------|---------|----------|
| OUTPUT |         2 | M69 P2   | ;        | PROBE_SELECT_TO_PROBE |       0 | work     |
| OUTPUT |         2 | M59 P2   | ;        | PROBE_SELECT_TO_PROBE |       1 | tool     |
| OUTPUT |         3 | M69 P3   | ;        | PROBE_ENABLE_TO_PROBE |       0 | Off      |
| OUTPUT |         3 | M59 P3   | ;        | PROBE_ENABLE_TO_PROBE |       1 | flashing |

## 6.13 Maximum Spindle Speed

This option increases the maximum speed at which you can run the machine spindle.

## 6.14 Compensation Tables

With this option, the control stores a compensation table to correct for small errors in the rotary worm gear, as well as small errors in X, Y, and Z.

## 6.15 New Rotary Configuration

When you install a rotary unit to your machine, you must:

- Designate the correct rotary model so that the machine control can load the correct parameters.
- Assign an axis letter (A, B, or C) to each new axis.
- Tell the machine which physical connection (4th or 5th axis) to use for each axis.

You do these tasks on the Rotary Selection page:

1. Press [SETTING] .
2. Select the Rotary tab.

Make sure the machine is not in Hand Jog mode when you go to the Rotary Selection page. The control does not allow changes to rotary configuration in Hand Jog mode.

When you go to the Rotary Selection page to install a rotary unit for the first time, both the 4th and 5th axes are disabled and have no rotary model selections. This process assigns a rotary model axis, and an axis letter, to the 4th and 5th axes.

To use Tool Center Point Control (TCPC) and Dynamic Work Offsets (DWO), your axis definitions and rotary installation must match the ANSI standard, where the A, B, and C Axes each rotate about the X, Y, and Z Axes, respectively. Refer to page 414 for more information about TCP. Refer to page 419 for more information about DWO.

<!-- image -->

NOTE:

<!-- image -->

NOTE:

## F6.8: Rotary Selections Page. [1] Current Rotary Selections, [2] Select New Rotaries Table.

<!-- image -->

## 6.16 Rotary Model Selection

In  this  procedure, you select your particular rotary model from the list of models in the control, so that the control can load the correct parameters for that unit. In this example, we have a TR160 unit installed on the table, with the tilt axis parallel to X.

We want to configure both the rotary (platter) and tilt (trunnion) axes. The rotary axis is physically connected to the 5th axis at the control cabinet. We want to designate the rotary axis C . The tilt axis is physically connected to the 4th axis at the control cabinet. We want to designate the tilt axis A .

1. Find the nameplate on your rotary unit. Record the values in the 'MODEL NO.' (model number) and 'VER' (version) fields. On our example nameplate, we find that the model number is TR160 , and the version is P4 .
2. F6.9: Example rotary nameplate. [1] Model Number, [2] Version
2. On the Rotary Selection page, use the [CURSOR] keys or the jog handle to browse the list of rotary models to find your model.

<!-- image -->

Dual-axis rotary units have two entries in the list: one for the rotary axis ( ROT ), and one for the tilt axis ( TLT ). Be sure to select the rotary model that matches both the model number and version on the nameplate. In the example below, the cursor highlights the rotary axis of the model that matches our example nameplate ( TR160-P4-ROT ).

- F6.10: Rotary Selection Example. [1] Model Column, [2] Name Column, [3] Fifth Axis Column, [4] Fourth Axis Column, [5] Current Selection (Highlighted).
3. Press [ENTER] . The Select Table Orientation window appears.
- F6.11: The Select Table Orientation Window. [1] Orientation Example Image, [2] Axis Configuration (Letter Assignment), [3] Physical Connection, [4] The Rotary Configuration Must Match the Picture to use TCPC/DWO.
4. Press [A] , [B] , or [C] to change the axis letter.
5. Press [F4] to toggle the physical connection setting between 4th and 5th .
6. Press [ENTER] to save the configuration to the Select New Rotaries table, or press [UNDO] to cancel.
7. Repeat steps 2-6 for the tilt axis, if applicable. In this example, we would now set up the TR160 tilt axis ( TR160-P4-TLT ).

<!-- image -->

<!-- image -->

8. After you complete the axis configuration, press [EMERGENCY STOP] , and then press [F3] to apply the rotary parameters.
9. Cycle power.

## 6.17 Custom Rotary Configurations

When you change a tool change offset or grid offset for an installed rotary, the control saves this information as a custom rotary configuration. You give this configuration a name that appears in the Name column of the Current Rotary Selections and Select New Rotaries tables.

The control keeps the default values in the base configuration and makes your custom configuration  an  option  in  the  list  of  available  rotaries.  After  you  define  a  custom configuration  for  an  axis,  the  control  saves  future  changes  to  the  same  custom configuration name.

- F6.12: Custom Rotary Configurations [1] In the Current Rotary Selections Table, and [2] in the Select New Rotaries Table.

<!-- image -->

The custom rotary configurations appear as options in the Select New Rotaries table. You can select them in the same way you would select a base rotary configuration. You can also save more than one custom configuration for the same rotary unit:

1. Start again with the base configuration of the installed rotary.
2. Configure the TC offset and grid offsets as needed.
3. Save this configuration with a new name.

You can also transfer custom rotary configurations to other machines. The control saves custom rotary files in the User Data / My Rotary folder in the Device Manager ( [LIST PROGRAM] ). You can transfer these files to the User Data / My Rotary folder on a different machine to make those configurations available in the Select New Rotaries table on that machine.

## F6.13: Custom Rotary Files in the User Data Tab

<!-- image -->

## 6.18 Rotary Tool Change Offset

After you define a rotary unit's axes in your machine control, you can set the tool change offset. This defines axis positions that put the rotary platter perpendicular to its defined axis.

1. In Handle Jog mode, jog the axes to make the platter face perpendicular to its defined axis. Use an indicator to verify perpendicularity.
2. Press [SETTING] and select the Rotary tab.
3. Highlight one of the axes in the Current Rotary Selections table.
4. Press [INSERT] to define the current axis position as the tool change offset position.
5. Type a name for your custom configuration, if prompted. You will see a prompt for a configuration name only when you make changes to a base configuration for the first time. Otherwise, the control saves your changes to the current custom configuration.

## 6.19 Rotary Grid Offset

You use the rotary grid offset to set new zero positions for your rotary unit.

1. In Handle Jog mode, jog the axes to the positions you want to use as the offset positions.
2. Press [SETTING] and select the Rotary tab.
3. Highlight one of the axes in the Current Rotary Selections table.
4. Press [ALTER] to define the current axis positions as the grid offset positions.
5. Type a name for your custom configuration, if prompted. You will see a prompt for a configuration name only when you make changes to a base configuration for the first time. Otherwise, the control saves your changes to the current custom configuration.

## 6.20 TCPC/DWO Activation

You can use Tool Center Point Control (TCPC) and Dynamic Work Offsets (DWO) if your rotary  configuration  is  correct,  and  you  have  correctly  set  Machine  Rotary  Zero  Point (MRZP) settings (255-257). Refer to page 414 for more information about TCPC. Refer to page 419 for more information about DWO.

<!-- image -->

NOTE:

To use Tool Center Point Control (TCPC) and Dynamic Work Offsets (DWO), your axis definitions  and  rotary  installation  must  match  the ANSI standard, where the A, B, and C Axes each rotate about the X, Y, and Z Axes, respectively. When you activate TCPC/DWO, you must confirm that your configuration is correct.

1. On the Rotary page, press [F4] .

The Confirm TCPC/DWO Configuration pop-up window appears.

- F6.14: Confirm TCPC/DWO Configuration Pop-up Window. [1] A- and C-Axis Configuration, [2] B- and C-Axis Configuration
2. If your rotary configuration matches the diagram, press [ENTER] to confirm so. This activates TCPC/DWO.

<!-- image -->

<!-- image -->

If your configuration does not match the diagram, you must adjust it to match; for example, you may need to redefine the axis letters or change the rotary unit's orientation.

3. After you activate TCPC/DWO, press F3 to save the rotary configuration. If you do not save the configuration, then TCPC/DWO is deactivated when you turn off the machine.

## 6.21 Machine Rotary Zero Point (MRZP)

The Machine Rotary Zero Point (MRZP) Offsets are control settings that define the centers of rotation for the rotary table relative to the home positions of the linear axes. The control uses the MRZP for Tool Center Point Control (TCPC) and Dynamic Work Offsets (DWO) for 4th- and 5th-axis machining. MRZP uses Settings 255, 256, and 257 to define the zero point.

255 - Machine Rotary Zero Point X Offset

256 - Machine Rotary Zero Point Y Offset

257 - Machine Rotary Zero Point Z Offset

The value stored in each of these settings is the distance from the home position of a linear axis to the center of rotation of a rotary axis. The units are in current machine units (as defined by Setting 9).

In machines with built-in 4th and 5th axes, such as the UMC-750, the initial MRZP offsets are set at the factory. You do not have to set initial values for these machines.

You do the MRZP adjustment procedures when:

- You install a new rotary unit in a mill, and you want to use TCPC/DWO.
- The machine has been crashed.
- The machine's level has changed.
- You want to make sure that the MRZP settings are correct.

MRZP adjustment consists of (2) stages: rough and finish. The rough stage establishes MRZP values that the control uses for the finish stage. Generally, you do the rough stage only at new installations, or when you are not sure if the current MRZP settings are close enough to correct for the finish set procedure.

Both the rough and finish MRZP procedures use the work probe to generate values in macro variables,  which  you then  transfer to the  correct settings.  You must change the values manually because the setting values cannot be set via macro. This protects them from accidental change in the middle of a program.

<!-- image -->

These  instructions  assume  that  the  probe  system  is  installed  and correctly calibrated.

## 6.22 MRZP Rough Set

This procedure establishes basic values for MRZP, which you then refine with the finish set process.

<!-- image -->

NOTE:

<!-- image -->

NOTE:

You should do this procedure only at new rotary installations, or when you are unsure if your current MRZP values are close enough to do the finish set procedure.

To do this procedure, you need to know the diameter of the center bore in your rotary platter.

1. Load or command the work probe into the spindle.
2. Jog the probe tip to approximately 0.4" (10 mm) above the approximate center of the ring gauge or bored hole.
3. Press [EDIT] .
4. Select the VPS tab, then use the [RIGHT] cursor arrow key to select Probing , Calibration , MRZP Calibration , and then MRZP Rough Set .
5. Highlight variable C , and then type the diameter of the ring gauge or bored hole. Press [ENTER] .
6. Highlight variable H , and then type the approximate distance between the rotary platter surface and the trunnion's center of rotation. Press [ENTER] .

This distance is approximately 2" on a UMC-750; refer to your rotary unit's layout drawing to find this dimension for other units, or follow the procedure on page 264 .

7. Press [CYCLE START] to immediately run the probe program in MDI, or press [F4] to choose to output the probing program to the clipboard or MDI to run later.
8. When the probing program runs, it automatically places values in macro variables #10121 , #10122 , and #10123 . These variables show the machine rotary zero point axis travel distance from the home position in the X, Y, and Z Axes. Record the values.

<!-- image -->

Press [CURRENT COMMANDS] and select the Macro Vars tab to view the variables. When the cursor is in the window, you can type a macro variable number and press the [DOWN] cursor arrow key to jump to that variable.

9. Enter the values from macro variables #10121, #10122, and #10123 into Settings 255, 256, and 257, respectively.
10. Do the Finish MRZP Set procedure.

## 6.23 MRZP Finish Set

Follow this  procedure to get final values  for  the  MRZP settings. You  can also  use this procedure to check your current setting values against new readings, to make sure the current values are correct.

If you want to use this procedure to check your current setting values, make sure that the setting values you start with are close to correct to begin with. Values of zero generate an alarm. If the settings are too far off, the probe will not contact the gauge ball when it rotates positions during the cycle. The MRZP rough set process establishes appropriate starting values, so if you are unsure of the current values, you should do the MRZP rough set process first.

To do this procedure, you need a gauge ball with a magnetic base.

1. Place the gauge ball on the table.

## IMPORTANT:

So that the gauge ball post does not interfere with the probe, position the ball post at an angle of approximately 45 degrees to the X Axis.

## F6.15: Gauge Ball Set at 45 Degrees Relative to X (UMC Shown)

<!-- image -->

2. Load or command the work probe into the spindle.
3. Position the work probe above the tooling ball.
4. Press [EDIT] .
5. Select the VPS tab, then use the [RIGHT] cursor arrow key to select Probing , Calibration , MRZP Calibration , and then MRZP Finish Set .
6. Highlight variable B , and then type the gauge ball diameter. Press [ENTER] .
7. Press [CYCLE START] to immediately run the probe program in MDI, or press [F4] to choose to output the probing program to the clipboard or MDI to run later.
8. When the probing program runs, it automatically places values in macro variables #10121 , #10122 , and #10123 . These variables show the machine rotary zero point axis travel distance from the home position in the X, Y, and Z Axes. Record the values.

Press [CURRENT COMMANDS] and select the Macro Vars tab to view the variables. When the cursor is in the variable list, you can type a macro variable number and press the [DOWN] cursor arrow key to jump to that variable.

9. Enter the values from macro variables #10121, #10122, and #10123 into Settings 255, 256, and 257, respectively.

<!-- image -->

## 6.24 Disabling and Enabling Rotary Axes

A disabled rotary axis does not move, but it stays configured. Disabling a rotary axis is a good way to temporarily stop using a rotary axis without removing it completely from the machine.

<!-- image -->

## NOTE:

You can also disable and enable built-in rotary axes this same way.

Enabled  rotary  axes  appear  with  a  filled-in  checkbox  in  the Current Rotary Selections table.

- F6.16: [1] Enabled Rotary Axis, [2] Disabled Rotary Axis.
1. Highlight the axis you want to disable or enable.
2. Press [EMERGENCY STOP] .
3. Press [ENTER] .

<!-- image -->

The control must not be in Jog mode when you disable an axis. If you get a Wrong  Mode message, press [MEMORY] to  change modes, and then press [SETTING] to return to the Rotary page.

The control toggles the enabled state of the rotary axis.

4. Release [EMERGENCY STOP] to continue operation.

<!-- image -->

NOTE:

## 6.25 4th and 5th Axis Programming

F6.17: Axis Motion on an Example Rotary Trunnion Unit: [1] Rotary Axis, [2] Tilt Axis

<!-- image -->

## 6.26 Creating Five-Axis Programs

## 6.27 Offsets

1. Press [OFFSET] and select the WORK tab.
2. Jog the axes to the zero point of the workpiece. Refer to page 140 for jogging information.
3. Highlight the axis and offset number.
4. Press [PART ZERO SET] and the current machine position is automatically stored in that address.

<!-- image -->

## CAUTION:

If  you  use  automatically  generated  tool  length  offsets,  you  should leave the Z-Axis work offset values at zero. Nonzero Z-Axis work offset values interfere with automatically generated tool length offsets, and can cause a machine crash.

5. The X and Y work coordinate offsets are always given as negative values from machine zero. Work coordinates are entered into the table as a number only. To enter an X value of X-2.00 into G54 , highlight the X Axis column in the G54 row, type -2.0 , and press [F1] to set the value.

## 6.28 Five-Axis Programming Notes

Program approach vectors (moving tool paths) to the workpiece at a safe distance above or to the side of the workpiece. This is important when you program the approach vectors with a rapid move ( G00 ), because the axes arrive at the programmed position at different times; the axis with shortest distance from target arrives first, and longest distance last. However, a linear move at a high feed rate forces the axes to arrive at the commanded position at the same time, avoiding the possibility of a crash.

## 6.29 G-codes

G93 inverse  time  feed  mode  must  be  in  effect  for  simultaneous  4-  or  5-axis  motion; however, if your mill supports Tool Center Point Control ( G234 ), you may use G94 (feed per minute). Refer to G93 on page 386 for more information.

Limit the post processor (CAD/CAM software) to a maximum G93 F value of 45000. This is the maximum allowable feedrate in G93 inverse time feed mode.

## 6.30 M-codes

IMPORTANT:

When doing any non 5-axis motion, engage the rotary axes brakes. Cutting with the brakes off causes excessive wear in the gear sets.

M10 / M11 engages/disengages the fourth axis brake.

M12 / M13 engages/disengages the fifth axis brake.

When in a 4 or 5 axis cut, the machine pauses between blocks. This pause is due to the Rotary  Axes  brakes  releasing.  To  avoid  this  dwell  and  allow  for  smoother  program execution,  program  an M11 and/or M13 before  the G93 .  The  M-codes  disengage  the brakes, resulting in a smoother and uninterrupted flow of motion. Remember that if the brakes are never re-engaged, they remain off indefinitely.

## 6.31 Settings

Settings used for 4th and 5th axis programing include:

For the 4th axis:

- Setting 34 - 4th Axis Diameter

For the 5th axis:

- Setting 79 - 5th-Axis Diameter

For the Axis mapped to the 4th or 5th Axis:

- Setting 48 - Mirror Image A-Axis
- Setting 80 - Mirror Image B-Axis
- Setting 250 - Mirror Image C-Axis

Setting 85 - Maximum Corner Rounding should be set to 0.0500 for 5-axis cutting. Settings lower than 0.0500 move the machine closer to an exact stop and cause uneven motion.

You can also use G187 Pn Ennnn to set the smoothness level in the program to slow the axes down. G187 temporarily overrides Setting 85. Refer to page 413 for more information.

## 6.32 Jogging the 4th and 5th Axes

Jogging the rotary axes works like jogging the linear axes: you select an axis and a jog rate, and then you use the jog handle or jog keys to move the axis. In Hand Jog mode, press the [+A/C +B] or [-A/C -B] jog key to select the 4th axis. To select the 5th axis, press [SHIFT] and then [+A/C +B] or [-A/C -B] .

The  control  remembers  the  last  rotary  axis  you  selected,  and [+A/C +B] or [-A/C  -B] continue to select that axis until you select the other axis. For example, after you select the 5th axis as described above, each time you press [+A/C +B] or [-A/C -B] selects the 5th axis for jogging. To select the 4th axis again, press SHIFT and then [+A/C +B] or [-A/C -B] . Now, each subsequent press of [+A/C +B] or [-A/C -B] selects the 4th axis.

## 6.33 Tilt Axis Center-of-Rotation Offset (Tilting Rotary Products)

This procedure determines the distance between the plane of the rotary axis platter and the tilt axis centerline on tilting rotary products. Some CAM software applications require this offset value. You also need this value to rough-set the MRZP offsets. Refer to page 257 for more information.

- F6.18: Tilt Axis Center-of-Rotation Offset Diagram (side view): [1] Tilt Axis Center-of-Rotation Offset, [2] Tilt Axis, [3] Plane of the Rotary Axis Platter.
- F6.19: Tilt Axis Center-of-Rotation Illustrated Procedure. Numeric labels in this diagram correspond to the step numbers in the procedure.
1. Jog the tilt axis until the rotary platter is vertical. Attach a dial indicator to the machine spindle (or other surface independent of table motion) and indicate the platter face. Set the dial indicator to zero.

<!-- image -->

<!-- image -->

The rotary unit's orientation on the table determines which linear axis to jog in these steps. If the tilt axis is parallel to the X Axis, use the Y Axis in these steps. If the tilt axis is parallel to the Y Axis, use the X Axis in these steps.

<!-- image -->

NOTE:

2. Set the X- or Y-Axis operator position to zero.
3. Jog the tilt Axis 180 degrees.
4. Indicate the platter face from the same direction as the first indication:
- a. Hold a 1-2-3 block against the platter face.
- b. Indicate the face of the block that rests against the platter face.
- c. Jog the X or Y Axis to zero the indicator against the block.
5. Read the new X- or Y-Axis operator position. Divide this value by 2 to determine the tilt axis center-of-rotation offset value.

## 6.34 Macros Introduction

<!-- image -->

NOTE:

This control feature is optional; call your HFO for information on how to purchase it.

For the most current Macros information scan the code below with your mobile device:

F6.20: Mill Interactive Operator's Manual - Macros Chapter

<!-- image -->

Macros add capabilities and flexibility to the control that are not possible with standard G-code.  Some  possible  uses  are:  families  of  parts,  custom  canned  cycles,  complex motions, and driving optional devices. The possibilities are almost endless.

A Macro is any routine/subprogram that you can run multiple times. A macro statement can assign  a  value  to  a  variable,  read  a  value  from  a  variable,  evaluate  an  expression, conditionally or unconditionally branch to another point within a program, or conditionally repeat some section of a program.

Here are a few examples of the applications for Macros. The examples are outlines and not complete macro programs.

- Tools For Immediate, On-Table Fixturing - You can semi-automate many setup procedures to assist the machinist. You can reserve tools for immediate situations that  you  did  not  anticipate  in  your  application  design.  For  instance,  suppose  a company uses a standard clamp with a standard bolt hole pattern. If you discovered, after  setup,  that  a  fixture  needs  an  additional  clamp,  and  suppose  that  you programmed macro subprogram 2000 to drill the bolt pattern of the clamp, then you only need this two-step procedure to add the clamp to the fixture:
- a) Jog the machine to the X, Y, and Z coordinates and angle where you want to place the clamp. Read the position coordinates from the machine display.
- b) Execute this command in MDI mode:

G65 P2000 Xnnn Ynnn Znnn Annn ;

where nnn are the coordinates determined in Step a). Here, macro 2000 ( P2000 ) does the work since it was designed to drill the clamp bolt hole pattern at the specified angle of A. Essentially, this is a custom canned cycle.

- Simple Patterns That Are Repeated - You can define and store repeated patterns with macros. For example:
- a) Bolt hole patterns
- b) Slotting
- c) Angular patterns, any number of holes, at any angle, with any spacing
- d) Specialty milling such as soft jaws
- e) Matrix Patterns, (e.g. 12 across and 15 down)
- f) Fly-cutting a surface, (e.g. 12 inches by 5 inches using a 3 inch fly cutter)
- Automatic  Offset  Setting  Based  On  The  Program -  With  macros,  coordinate offsets can be set in each program so that setup procedures become easier and less error-prone (macro variables #2001-2800 ).
- Probing - Using a probe enhances the capabilities of the machine, some examples are:
- a) Profiling of a part to determine unknown dimensions for machining.
- b) Tool calibration for offset and wear values.
- c) Inspection prior to machining to determine material allowance on castings.
- d) Inspection after machining to determine parallelism and flatness values as well as location.

## 6.35 Useful G and M Codes

```
M00 , M01 , M30 - Stop Program G04 - Dwell G65 Pxx - Macro subprogram call. Allows passing of variables. M29 - Set output relay with M-FIN. M59 - Set output relay.
```

```
M69 - Clear output relay. M96 Pxx Qxx - Conditional Local Branch when Discrete Input Signal is 0 M97 Pxx - Local Sub Routine Call M98 Pxx - Sub Program Call M99 - Sub Program Return or Loop G103 - Block Lookahead Limit. No cutter comp allowed.
```

- M109 - Interactive User Input (refer to page 454 )

## 6.36 Round Off

The  control  stores  decimal  numbers  as  binary  values.  As  a  result,  numbers  stored  in variables can be off by 1 least significant digit. For example, the number 7 stored in macro variable #10000 , may later be read as 7.000001, 7.000000, or 6.999999. If your statement was

```
IF [#10000 EQ 7]… ;
```

it may give a false reading. A safer way of programming this would be

```
IF [ROUND [#10000] EQ 7]… ;
```

This issue is usually a problem only when you store integers in macro variables where you do not expect to see a fractional part later.

## 6.37 Look-ahead

Look-ahead is a very important concept in macro programming. The control attempts to process as many lines as possible ahead of time in order to speed up processing. This includes the interpretation of macro variables. For example,

```
#12012 = 1 ; G04 P1. ; #12012 = 0 ;
```

This  is  intended  to  turn  an  output  on,  wait  1  second,  and  then  turn  it  off.  However, lookahead  causes  the  output  to  turn  on  then  immediately  back  off  while  the  control processes the dwell. G103 P1 is used to limit lookahead to 1 block. To make this example work properly, modify it as follows:

G103 P1 (See the G-code section of the manual for a further

```
explanation of G103) ; ; #12012=1 ; G04 P1. ; ; ; ; #12012=0 ;
```

## 6.38 Block Look-Ahead and Block Delete

The Haas control uses block look-ahead to read and prepare for blocks of code that come after the current block of code. This lets the control transition smoothly from one motion to the next. G103 limits how far ahead the control looks at blocks of code. The P nn address code  in G103 specifies  how  far  ahead  the  control  is  allowed  to  look.  For  additional information, refer to G103 on page 390 .

Block  Delete  mode  lets  you  selectively  skip  blocks  of  code.  Use  a / character  at  the beginning of the program blocks that you want to skip. Press [BLOCK DELETE] to enter the Block Delete mode. While Block Delete mode is active, the control does not execute the blocks marked with a / character. For example:

Using a

```
/M99 (Sub-Program Return) ;
```

before a block with

```
M30 (Program End and Rewind) ;
```

makes the sub-program a main program when [BLOCK DELETE] is on. The program is used as a sub-program when Block Delete is off.

When a block delete token "/" is used, even if Block Delete mode is not active, the line will block look ahead. This is useful for debugging macro processing within NC programs.

## 6.39 Operation Notes

You save or load macro variables through the Net Share or USB port, much like settings, and offsets.

## 6.40 Macro Variable Display Page

The local and global macro variables #1 - #33 and #10000 - #10999 are displayed and modified through the Current Commands display.

<!-- image -->

Internal to the machine, 10000 is added to 3-digit macro variables. For example: Macro 100 is displayed as 10100.

1. Press [CURRENT COMMANDS] and use navigation keys to get to the Macro Vars page.

As the control interprets a program, the variable changes and results are displayed on the Macro Vars display page.

2. Enter a value (maximum is 999999.000000) and then press [ENTER] to set the macro variable. Press [ORIGIN] to clear macro variables, this displays the Origin clear entry popup. Press number 1 - 3 to make a selection or press [CANCEL] to exit.
2. F6.21: Origin Clear Entry Popup. 1: Clear Cell - Clears the highlighted cell to zero. 2: Clear Column - Clears the active cursor column entries to zero. 3: Clear All Global Macros - Clears Global Macro entries (Macro 1-33, 10000-10999) to zero.
3. To search for a variable, enter the macro variable number and press the up or down arrow.
4. The variables displayed represent values of the variables when the program runs. At times, this may be up to 15 blocks ahead of actual machine actions. Debugging programs is easier when a G103 P1 is inserted at the beginning of a program to limit block buffering. A G103 without the P value can be added after the macro variable blocks in the program. For a macro program to operate correctly it is recommended that the G103 P1 be left in the program during loading of variables. For more details about G103 see the G-code section of the manual.

<!-- image -->

## 6.41 Display Macro Variables in the Timers And Counters Window

In the Timers  And  Counters window, you can display the values of any two macro variables and assign them a display name.

To set which two macro variables display in the Timers And Counters window:

1. Press [CURRENT COMMANDS] .
2. Use the navigation keys to select the TIMERS page.
3. Highlight the Macro Label #1 name or Macro Label #2 name.
4. Key in a new name, and press [ENTER] .
5. Use arrow keys to pick the Macro Assign #1 or Macro Assign #2 entry field (corresponding to your chosen Macro Label name).
6. Key in the macro variable number (without #) and press [ENTER] .

On the Timers And Counters window, the field to the right of the entered Macro Label (#1 or #2) name displays the assigned variable value.

## 6.42 Macro Arguments

The arguments in a G65 statement are a means to send values to a macro subprogram and set the local variables of a macro subprogram.

The next (2) tables indicate the mapping of the alphabetic address variables to the numeric variables used in a macro subprogram.

## 6.43 Alphabetic Addressing

## T6.2: Alphabetic Address Table

| Address   |   Variable | Address   | Variable   |
|-----------|------------|-----------|------------|
| A         |          1 | N         | -          |
| B         |          2 | O         | -          |
| C         |          3 | P         | -          |
| D         |          7 | Q         | 17         |
| E         |          8 | R         | 18         |

| Address   | Variable   | Address   |   Variable |
|-----------|------------|-----------|------------|
| F         | 9          | S         |         19 |
| G         | -          | T         |         20 |
| H         | 11         | U         |         21 |
| I         | 4          | V         |         22 |
| J         | 5          | W         |         23 |
| K         | 6          | X         |         24 |
| L         | -          | Y         |         25 |
| M         | 13         | Z         |         26 |

## Alternate Alphabetic Addressing

| Address   |   Variable | Address   |   Variable | Address   |   Variable |
|-----------|------------|-----------|------------|-----------|------------|
| A         |          1 | K         |         12 | J         |         23 |
| B         |          2 | I         |         13 | K         |         24 |
| C         |          3 | J         |         14 | I         |         25 |
| I         |          4 | K         |         15 | J         |         26 |
| J         |          5 | I         |         16 | K         |         27 |
| K         |          6 | J         |         17 | I         |         28 |
| I         |          7 | K 18      |            | J         |         29 |
| J         |          8 | I         |         19 | K         |         30 |
| K         |          9 | J         |         20 | I         |         31 |
| I         |         10 | K         |         21 | J         |         32 |
| J         |         11 | I         |         22 | K         |         33 |

Arguments accept any floating-point value to four decimal places. If the control is in metric, it will assume thousandths (.000). In example below, local variable #1 will receive .0001. If a decimal is not included in an argument value, such as:

G65 P9910 A1 B2 C3 ;

The values are passed to macro subprograms according to this table:

## 6.44 Integer Argument Passing (no decimal point)

| Address   | Variable   | Address   | Variable   | Address   |   Variable |
|-----------|------------|-----------|------------|-----------|------------|
| A         | .0001      | J         | .0001      | S         |         1. |
| B         | .0002      | K         | .0001      | T         |         1. |
| C         | .0003      | L         | 1.         | U         |      .0001 |
| D         | 1.         | M         | 1.         | V         |      .0001 |
| E         | 1.         | N         | -          | W         |      .0001 |
| F         | 1.         | O         | -          | X         |      .0001 |
| G         | -          | P         | -          | Y         |      .0001 |
| H         | 1.         | Q         | .0001      | Z         |      .0001 |
| I         | .0001      | R         | .0001      |           |            |

All 33 local macro variables can be assigned values with arguments by using the alternate addressing method. The following example shows how to send two sets of coordinate locations to a macro subprogram. Local variables #4 through #9 would be set to .0001 through .0006 respectively.

Example:

<!-- formula-not-decoded -->

The following letters cannot be used to pass parameters to a macro subprogram: G, L, N, O or P.

## 6.45 Macro Variables

There are (3) categories of macro variables: local, global, and system.

Macro  constants  are  floating-point  values  placed  in  a  macro  expression.  They  can  be combined with addresses A-Z, or they can stand alone when used within an expression. Examples of constants are 0.0001, 5.3 or -10.

## 6.46 Local Variables

Local variables range between #1 and #33 . A set of local variables is available at all times. When a call to a subprogram with a G65 command is executed, local variables are saved and a new set is available for use. This is called nesting of local variables. During a G65 call, all new local variables are cleared to undefined values and any local variables that have corresponding address variables in the G65 line are set to G65 line values. Below is a table of the local variables along with the address variable arguments that change them:

| Variable:   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10   | 11   |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|
| Address:    | A   | B   | C   | I   | J   | K   | D   | E   | F   |      | H    |
| Alternate:  |     |     |     |     |     |     | I   | J   | K   | I    | J    |
| Variable:   | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21   | 22   |
| Address:    |     | M   |     |     |     | Q   | R   | S   | T   | U    | V    |
| Alternate:  | K   | I   | J   | K   | I   | J   | K   | I   | J   | K    | I    |
| Variable:   | 23  | 24  | 25  | 26  | 27  | 28  | 29  | 30  | 31  | 32   | 33   |
| Address:    | W   | X   | Y   | Z   |     |     |     |     |     |      |      |
| Alternate:  | J   | K   | I   | J   | K   | I   | J   | K   | I   | J    | K    |

Variables 10 , 12 , 14 - 16 and 27 - 33 do not have corresponding address arguments. They can be set if a sufficient number of I , J and K arguments are used as indicated above in the section about arguments. Once in the macro subprogram, local variables can be read and modified by referencing variable numbers 1 - 33 .

When  the L argument  is  used  to  do  multiple  repetitions  of  a  macro  subprogram,  the arguments are set only on the first repetition. This means that if local variables 1 - 33 are modified in the first repetition, then the next repetition will have access only to the modified values. Local values are retained from repetition to repetition when the L address is greater than 1.

Calling  a  subprogram  via  an M97 or M98 does  not  nest  the  local  variables.  Any  local variables referenced in a subprogram called by an M98 are the same variables and values that existed prior to the M97 or M98 call.

## 6.47 Global Variables

Global variables are accessible at all times and remain in memory when power is turned off.  There  is  only  one  copy  of  each  global  variable.  Global  variables  are  numbered #10000 - #10999 .  Three legacy ranges: ( #100 - #199 , #500 - #699 ,  and #800 - #999 )  are included. The legacy 3 digit macro variables begin at the #10000 range; ie., macro variable #100 is displayed as #10100.

<!-- image -->

NOTE:

<!-- image -->

CAUTION:

Using variable #100 or #10100 in a program the control will access the same data. Using either variable number is acceptable.

Sometimes, factory-installed options use global variables, for example, probing and pallet changers, etc. Refer to the Macro Variables Table on page 274 for global variables and their use.

When you use a global variable, make sure that no other programs on the machine use the same global variable.

## 6.48 System Variables

System variables let you interact with a variety of control conditions. System variable values can change the function of the control. When a program reads a system variable, it can modify its behavior based on the value in the variable. Some system variables have a Read Only status; this means that you cannot modify them. Refer to the Macro Variables Table on page 274 for a list of system variables and their use.

## 6.49 Macro Variables Table

The macro variables table of local, global, and system variables and their usage follows. The new generation control variables list includes legacy variables.

For the most current Macro Variables Table scan the code below with your mobile device:

## F6.22: Mill Interactive Operator's Manual - Macros Chapter

<!-- image -->

| NGC Variable    | Legacy Variable   | Usage                                                             |
|-----------------|-------------------|-------------------------------------------------------------------|
| #0              | #0                | Not a number (read only)                                          |
| #1 - #33        | #1 - #33          | Macro call arguments                                              |
| #10000 - #10146 | #100 - #146       | General-purpose variables saved on power off                      |
| #10147 - #10199 | #147 - #199       | Probe values (if installed)                                       |
| #10200 - #10399 | N/A               | General-purpose variables saved on power off                      |
| #10400 - #10499 | N/A               | General-purpose variables saved on power off                      |
| #10500 - #10549 | #500 - #549       | General-purpose variables saved on power off                      |
| #10550 - #10599 | #550 - #599       | Probe calibration data (if installed)                             |
| #10600 - #10699 | #600 - #699       | General-purpose variables saved on power off                      |
| #10700 - #10799 | N/A               | General-purpose variables saved on power off                      |
| #700 - #749     | #700 - #749       | Hidden variables for internal use only                            |
| #709            | #709              | Used for the Fixture Clamp Input. Do not use for general purpose. |
| #10800 - #10999 | #800 - #999       | General-purpose variables saved on power off                      |
| #11000 - #11063 | N/A               | 64 discrete inputs (read only)                                    |
| #1064 - #1068   | #1064 - #1068     | Maximum axis loads for X, Y, Z, A, and B Axes, respectively       |
| #1080 - #1087   | #1080 - #1087     | Raw analog to digital inputs (read only)                          |

| NGC Variable   | Legacy Variable   | Usage                                                      |
|----------------|-------------------|------------------------------------------------------------|
| #1090 - #1098  | #1090 - #1098     | Filtered analog to digital inputs (read only)              |
| #1098          | #1098             | Spindle load with Haas vector drive (read only)            |
| #1264 - #1268  | #1264 - #1268     | Maximum axis loads for C, U, V, W, and T-axes respectively |
| #1601 - #1800  | #1601 - #1800     | Number of flutes on tools #1 through 200                   |
| #1801 - #2000  | #1801 - #2000     | Maximum recorded vibrations of tools 1 through 200         |
| #2001 - #2200  | #2001 - #2200     | Tool length offsets                                        |
| #2201 - #2400  | #2201 - #2400     | Tool length wear                                           |
| #2401 - #2600  | #2401 - #2600     | Tool diameter/radius offsets                               |
| #2601 - #2800  | #2601 - #2800     | Tool diameter/radius wear                                  |
| #3000          | #3000             | Programmable alarm                                         |
| #3001          | #3001             | Millisecond timer                                          |
| #3002          | #3002             | Hour timer                                                 |
| #3003          | #3003             | Single block suppression                                   |
| #3004          | #3004             | Override [FEED HOLD] control                               |
| #3006          | #3006             | Programmable stop with message                             |
| #3011          | #3011             | Year, month, day                                           |
| #3012          | #3012             | Hour, minute, second                                       |
| #3020          | #3020             | Power on timer (read only)                                 |
| #3021          | #3021             | Cycle start timer                                          |
| #3022          | #3022             | Feed timer                                                 |
| #3023          | #3023             | Present part timer (read only)                             |
| #3024          | #3024             | Last complete part timer (read only)                       |
| #3025          | #3025             | Previous part timer (read only)                            |

| NGC Variable   | Legacy Variable   | Usage                                                                                                                                                                                       |
|----------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #3026          | #3026             | Tool in spindle (read only)                                                                                                                                                                 |
| #3027          | #3027             | Spindle RPM (read only)                                                                                                                                                                     |
| #3028          | #3028             | Number of pallets loaded on receiver                                                                                                                                                        |
| #3030          | #3030             | Single block                                                                                                                                                                                |
| #3032          | #3032             | Block delete                                                                                                                                                                                |
| #3033          | #3033             | Opt stop                                                                                                                                                                                    |
| #3034          | N/A               | Safe Run (read only)                                                                                                                                                                        |
| #3196          | #3196             | Cell safe timer                                                                                                                                                                             |
| #3201 - #3400  | #3201 - #3400     | Actual diameter for tools 1 through 200                                                                                                                                                     |
| #3401 - #3600  | #3401 - #3600     | Programmable coolant positions for tools 1 through 200                                                                                                                                      |
| #3901          | #3901             | M30 count 1                                                                                                                                                                                 |
| #3902          | #3902             | M30 count 2                                                                                                                                                                                 |
| #4000 - #4099  | #4000 - #4099     | Previous block G-code group codes                                                                                                                                                           |
| #4101 - #4126  | #4101 - #4126     | Previous block address codes. NOTE: (1) Mapping of 4101 to 4126 is the same as the alphabetic addressing of Macro Arguments section; e.g., the statement X1.3 sets variable  <!-- image --> |
| #4132          | n/a               | #4124 to 1.3. Returns current active work offset number (including sub offset number if applicable)                                                                                         |
| #5001 - #5006  | #5001 - #5006     | Previous block end position                                                                                                                                                                 |

| NGC Variable   | Legacy Variable   | Usage                                                                               |
|----------------|-------------------|-------------------------------------------------------------------------------------|
| #5011 - #5019  | n/a               | Present skip signal position - X, Y, Z, A, B, C, U, V, W (machine position)         |
| #5021 - #5026  | #5021 - #5026     | Present machine coordinate position                                                 |
| #5041 - #5046  | #5041 - #5046     | Present work coordinate position                                                    |
| #5051 - #5056  | N/A               | Used in TCPC and DWO calculations                                                   |
| #5061 - #5069  | #5061 - #5069     | Present skip signal position - X, Y, Z, A, B, C, U, V, W (unrotated work positions) |
| #5081 - #5086  | #5081 - #5086     | Present tool offset                                                                 |
| #5201 - #5206  | #5201 - #5206     | G52 work offsets                                                                    |
| #5221 - #5226  | #5221 - #5226     | G54 work offsets                                                                    |
| #5241 - #5246  | #5241 - #5246     | G55 work offsets                                                                    |
| #5261 - #5266  | #5261 - #5266     | G56 work offsets                                                                    |
| #5281 - #5286  | #5281 - #5286     | G57 work offsets                                                                    |
| #5301 - #5306  | #5301 - #5306     | G58 work offsets                                                                    |
| #5321 - #5326  | #5321 - #5326     | G59 work offsets                                                                    |
| #5401 - #5500  | #5401 - #5500     | Tool feed timers (seconds)                                                          |
| #5501 - #5600  | #5501 - #5600     | Total tool timers (seconds)                                                         |
| #5601 - #5699  | #5601 - #5699     | Tool life monitor limit                                                             |
| #5701 - #5800  | #5701 - #5800     | Tool life monitor counter                                                           |
| #5801 - #5900  | #5801 - #5900     | Tool load monitor maximum load sensed so far                                        |
| #5901 - #6000  | #5901 - #6000     | Tool load monitor limit                                                             |
| #6001 - #6999  | #6001 - #6999     | Reserved. Do not use.                                                               |

| NGC Variable   | Legacy Variable   | Usage                                                                                                 |
|----------------|-------------------|-------------------------------------------------------------------------------------------------------|
| #6198          | #6198             | DS9/NGC/CF flag NOTE: DS9 is 19 inch NGC machines and NGC is for 15 inch NGC Machines  <!-- image --> |
| #6601          | #6601             | DS9/NGC/CF flag NOTE: DS9 is 19 inch NGC machines and NGC is for 15 inch NGC Machines  <!-- image --> |
| #7001 - #7006  | #7001 - #7006     | G110 (G154 P1) additional work offsets                                                                |
| #7021 - #7026  | #7021 - #7026     | G111 (G154 P2) additional work offsets                                                                |
| #7041 - #7386  | #7041 - #7386     | G112 - G129 ( G154 P3 - P20) additional work offsets                                                  |
| #7501 - #7506  | #7501 - #7506     | Pallet priority                                                                                       |
| #7601 - #7606  | #7601 - #7606     | Pallet status                                                                                         |
| #7701 - #7706  | #7701 - #7706     | Part program numbers assigned to pallets                                                              |
| #7801 - #7806  | #7801 - #7806     | Pallet usage count                                                                                    |
| #8500          | #8500             | Advanced Tool Management (ATM) group ID                                                               |
| #8501          | #8501             | ATM percent of available tool life of all tools in the group                                          |
| #8502          | #8502             | ATM total available tool usage count in the group                                                     |
| #8503          | #8503             | ATM total available tool hole count in the group                                                      |
| #8504          | #8504             | ATM total available tool feed time (in seconds) in the group                                          |
| #8505          | #8505             | ATM total available tool total time (in seconds) in the group                                         |
| #8510          | #8510             | ATM next tool number to be used                                                                       |
| #8511          | #8511             | ATM percent of available tool life of the next tool                                                   |
| #8512          | #8512             | ATM available usage count of the next tool                                                            |

| NGC Variable    | Legacy Variable   | Usage                                                         |
|-----------------|-------------------|---------------------------------------------------------------|
| #8513           | #8513             | ATM available hole count of the next tool                     |
| #8514           | #8514             | ATM available feed time of the next tool (in seconds)         |
| #8515           | #8515             | ATM available total time of the next tool (in seconds)        |
| #8550           | #8550             | Individual tool ID                                            |
| #8551           | #8551             | Number of flutes of tools                                     |
| #8552           | #8552             | Maximum recorded vibrations                                   |
| #8553           | #8553             | Tool length offsets                                           |
| #8554           | #8554             | Tool length wear                                              |
| #8555           | #8555             | Tool diameter offsets                                         |
| #8556           | #8556             | Tool diameter wear                                            |
| #8557           | #8557             | Actual diameter                                               |
| #8558           | #8558             | Programmable coolant position                                 |
| #8559           | #8559             | Tool feed timer (seconds)                                     |
| #8560           | #8560             | Total tool timers (seconds)                                   |
| #8561           | #8561             | Tool life monitor limit                                       |
| #8562           | #8562             | Tool life monitor counter                                     |
| #8563           | #8563             | Tool load monitor maximum load sensed so far                  |
| #8564           | #8564             | Tool load monitor limit                                       |
| #9000           | #9000             | Thermal comp accumulator                                      |
| #9000 - #9015   | #9000 - #9015     | Reserved (duplicate of axis thermal accumulator)              |
| #9016           | #9016             | Thermal spindle comp accumulator                              |
| #9016 - #9031   | #9016 - #9031     | Reserved (duplicate of axis thermal accumulator from spindle) |
| #10000 - #10999 | N/A               | General purpose variables                                     |

| NGC Variable    | Legacy Variable   | Usage                                             |
|-----------------|-------------------|---------------------------------------------------|
| #11000 - #11255 | N/A               | Discrete inputs (read only)                       |
| #12000 - #12255 | N/A               | Discrete outputs                                  |
| #13000 - #13063 | N/A               | Filtered analog to digital inputs (read only)     |
| #13013          | N/A               | Coolant level                                     |
| #14001 - #14006 | N/A               | G110(G154 P1) additional work offsets             |
| #14021 - #14026 | N/A               | G110(G154 P2) additional work offsets             |
| #14041 - #14386 | N/A               | G110(G154 P3 - G154 P20) additional work offsets  |
| #14401 - #14406 | N/A               | G110(G154 P21) additional work offsets            |
| #14421 - #15966 | N/A               | G110(G154 P22 - G154 P99) additional work offsets |
| #20000 - #29999 | N/A               | Settings                                          |
| #30000 - #39999 | N/A               | Parameters                                        |
| #32014          | N/A               | Machine Serial Number                             |
| #50001 - #50200 | N/A               | Tool Type                                         |
| #50201 - #50400 | N/A               | Tool material                                     |
| #50401 - #50600 | N/A               | Tool Offset Point                                 |
| #50601 - #50800 | N/A               | Estimated RPM                                     |
| #50801 - #51000 | N/A               | Estimated Feedrate                                |
| #51001 - #51200 | N/A               | Offset Pitch                                      |
| #51201 - #51400 | N/A               | Actually VPS Estimated RPM                        |
| #51401 - #51600 | N/A               | Work Material                                     |
| #51601 - #51800 | N/A               | VPS Feedrate                                      |
| #51801 - #52000 | N/A               | Approximate length                                |
| #52001 - #52200 | N/A               | Approximate diameter                              |

| NGC Variable    | Legacy Variable   | Usage                      |
|-----------------|-------------------|----------------------------|
| #52201 - #52400 | N/A               | Edge Measure height        |
| #52401 - #52600 | N/A               | Tool Tolerance             |
| #52601 - #52800 | N/A               | Probe Type                 |
| #56701 - #56900 | N/A               | Max Spindle Speed Per tool |

## 6.50 System Variables In-Depth

System variables are associated with specific functions. A detailed description of these functions follows.

## 6.51 #550-#699 #10550- #10699 General and Probe Calibration Data

These general purpose variables  are  saved  on  power  off.  Some  of  these  higher  #5xx variables store probe calibration data. Example: #592 sets which side of the table the tool probe is positioned. If these variables are overwritten, you will need to calibrate the probe again.

<!-- image -->

NOTE:

If  the machine does not have a probe installed, you can use these variables as general-purpose variables saved on power off.

## 6.52 #1080-#1097 #11000-#11255 #13000-#13063 1-Bit Discrete Inputs

You can connect designated inputs from external devices with these macros:

| Variables     | Legacy Variables        | Usage                                                 |
|---------------|-------------------------|-------------------------------------------------------|
| #11000-#11255 |                         | 256 discrete inputs (read only)                       |
| #13000-#13063 | #1080-#1087 #1090-#1097 | Raw and Filtered analog to digital inputs (read only) |

Specific input values can be read from within a program. The format is #11nnn where nnn is the Input Number. Press [DIAGNOSTIC] and select the I/O tab to see the Input and Output numbers for different devices.

Example:

#10000=#11018

This  example  records  the  state  of  #11018,  which  refers  to  Input  18  (M-Fin\_Input),  to variable #10000.

For available User Inputs on the I/O PCB, refer to the Robot Integration Aid reference document in the Haas service website.

F6.23: Scan the QR code for Robot Integration Aid reference document

<!-- image -->

## 6.53 #12000-#12255 1-Bit Discrete Outputs

The Haas control is capable of controlling up to 256 discrete outputs. However, a number of these outputs are reserved for the Haas control to use.

| Variables       | Legacy Variables   | Usage                |
|-----------------|--------------------|----------------------|
| #12000 - #12255 |                    | 256 discrete outputs |

Specific output values can be read, or written to, from within a program. The format is #12nnn where nnn is the Output Number.

Example:

#10000=#12018 ;

This example records the state of #12018 , which refers to Input 18 (Coolant Pump Motor), to variable #10000.

## 6.54 Maximum Axis Loads

These variables contain the maximum load an axis has achieved since the machine was last powered on, or since that Macro Variable was cleared. The Maximum Axis Load is the greatest load (100.0 = 100%) an axis has seen, not the Axis Load at the time that the control reads the variable.

| #1064   | = X Axis   | #1264   | = C axis   |
|---------|------------|---------|------------|
| #1065   | = Y Axis   | #1265   | = U axis   |
| #1066   | = Z Axis   | #1266   | = V axis   |
| #1067   | = A Axis   | #1267   | = W axis   |
| #1068   | = B Axis   | #1268   | = T axis   |

## 6.55 Tool Offsets

Each tool offset has a length (H) and diameter (D) along with associated wear values.

| #2001 - #2200   | H geometry offsets (1-200) for length.   |
|-----------------|------------------------------------------|
| #2201 - #2400   | H geometry wear (1-200) for length.      |
| #2401 - #2600   | D geometry offsets (1-200) for diameter. |
| #2601 - #2800   | D geometry wear (1-200) for diameter.    |

## 6.56 #3000 Programmable Alarm Messages

#3000 Alarms can be programmed. A programmable alarm will act like the built-in alarms. An alarm is generated by setting macro variable #3000 to a number between 1 and 999.

```
#3000= 15 (MESSAGE PLACED INTO ALARM LIST) ;
```

When this is done, Alarm flashes at the bottom of the display and the text in the next comment is placed into the alarm list. The alarm number (in this example, 15) is added to 1000 and used as an alarm number. If an alarm is generated in this manner all motion stops and the program must be reset to continue. Programmable alarms are always numbered between 1000 and 1999.

## 6.57 #3001-#3002 Timers

Two timers can be set to a value by assigning a number to the respective variable. A program can then read the variable and determine the time passed since the timer was set. Timers  can  be  used  to  imitate  dwell  cycles,  determine  part-to-part  time  or  wherever time-dependent behavior is desired.

- #3001 Millisecond Timer - The millisecond timer represents the system time after power on in number of milliseconds. The whole number returned after accessing #3001 represents the number of milliseconds.
- #3002 Hour Timer - The hour timer is similar to the millisecond timer except that the number returned after accessing #3002 is in hours. The hour and millisecond timers are independent of each other and can be set separately.

## 6.58 System Overrides

Variable #3003 overrides the Single Block function in G-code. When #3003 has a value of 1, the control executes each G-code command continuously even though the Single Block function is ON . When #3003 has a value of zero, Single Block operates as normal. You must press [CYCLE START] to execute each line of code in single block mode.

```
... #3003=1 ; G54 G00 G90 X0 Y0 ; S2000 M03 ; G43 H01 Z.1 ; G81 R.1 Z-0.1 F20. ; #3003=0 ; T02 M06 ; G43 H02 Z.1 ; S1800 M03 ; G83 R.1 Z-1. Q.25 F10. ; X0. Y0. ; %
```

## 6.59 Variable #3004

Variable #3004 overrides specific control features during operation.

The first bit disables [FEED HOLD] . If variable #3004 is set to 1, [FEED HOLD] is disabled for the program blocks that follow. Set #3004 to  0  to  enable [FEED HOLD] again. For example:

...

```
(Approach code - [FEED HOLD] allowed) ; #3004=1 (Disables [FEED HOLD] ) ; (Non-stoppable code - [FEED HOLD] not allowed) ; #3004=0 (Enables [FEED HOLD] ) ; (Depart code - [FEED HOLD] allowed) ; ...
```

Variable #3004 resets to 0 at M30.

This is a map of variable #3004 bits and the associated overrides.

E = Enabled D = Disabled

|   #3004 | Feed Hold   | Feed Rate Override   | Exact Stop Check   |
|---------|-------------|----------------------|--------------------|
|       0 | E           | E                    | E                  |
|       1 | D           | E                    | E                  |
|       2 | E           | D                    | E                  |
|       3 | D           | D                    | E                  |
|       4 | E           | E                    | D                  |
|       5 | D           | E                    | D                  |
|       6 | E           | D                    | D                  |
|       7 | D           | D                    | D                  |

## 6.60 #3006 Programmable Stop

You can add stops to the program that act like an M00 - The control stops and waits until you press [CYCLE START] , then the program continues with the block after the #3006 . In this example, the control displays the comment on the lower-center of the screen.

```
#3006=1 (comment here) ;
```

## 6.61 #3030 Single Block

In Next Generation Control when the system variable #3030 is set to a 1; the control will go into single block mode. There is no need to limit the lookahead using a G103 P1 , the Next Generation Control will correctly process this code.

<!-- image -->

For  the  Classic  Haas  Control  to  process  system  variable  #3030=1 correctly, it is necessary to limit the lookahead to 1 block using a G103 P1 before the #3030=1 code.

## 6.62 #4001-#4021 Last Block (Modal) Group Codes

G-code groups let the machine control process the codes more efficiently. G-codes with similar functions are usually in the same group. For example, G90 and G91 are under group 3. Macro variables #4001 through #4021 store the last or default G code for any of 21 groups.

G-Codes Group number is listed next to it's description in the G-Code section.

Example:

G81 Drill Canned Cycle (Group 09)

When a macro program reads the group code, the program can change the behavior of the G-code. If #4003 contains 91, then a macro program could determine that all moves should be incremental rather than absolute. There is no associated variable for group zero; group zero G codes are Non-modal.

## 6.63 #4101-#4126 Last Block (Modal) Address Data

Address  codes  A-Z  (excluding  G)  are  maintained  as  modal  values.  The  information represented by the last line of code interpreted by the lookahead process is contained in variables #4101 through #4126 . The numeric mapping of variable numbers to alphabetic addresses  corresponds  to  the  mapping  under  alphabetic  addresses.  For  example,  the value of the previously interpreted D address is found in #4107 and the last interpreted I value is #4104 . When aliasing a macro to an M-code, you may not pass variables to the macro using variables #1 - #33 . Instead, use the values from #4101 - #4126 in the macro.

## 6.64 #5001-#5006 Last Target Position

The final programmed point for the last motion block can be accessed through variables #5001 - #5006 , X, Z, Y, A, B, and C respectively. Values are given in the current work coordinate system and can be used while the machine is in motion.

## 6.65 #5021-#5026 Current Machine Coordinate Position

To get the current machine axis positions, call macro variables #5021 - #5026 corresponding to axis X, Y, Z, A, B, and C, respectively.

| #5021 X Axis   | #5022 Y Axis   | #5023 Z Axis   |
|----------------|----------------|----------------|
| #5024 A Axis   | #5025 B Axis   | #5026 C Axis   |

<!-- image -->

## NOTE:

Values CANNOT be read while the machine is in motion.

## 6.66 #5041-#5046 Current Work Coordinate Position

To  get  the  current  work  coordinate  positions,  call  macro  variables #5041 - #5046 corresponding to axis X, Y, Z, A, B, and C, respectively.

<!-- image -->

NOTE:

The values CANNOT be read while the machine is in motion.

## 6.67 #5061-#5069 Current Skip Signal Position

Macro variables #5061 - #5069 corresponding to X, Y, Z, A, B, C, U, V and W respectively, give the axis positions where the last skip signal occurred. Values are given in the current work coordinate system and can be used while the machine is in motion.

The value of #5063 ( Z ) has tool length compensation applied to it.

## 6.68 #5081-#5086 Tool Length Compensation

Macro variables #5081 - #5086 give the current total tool length compensation in axis X, Y, Z, A, B, or C, respectively. This includes tool length offset referenced by the current value set in H ( #4008 ) plus the wear value.

## 6.69 #5201-#5326, #7001-#7386, #14001-#14386 Work Offsets

Macro expressions can read and set all work offsets. This lets you preset coordinates to exact locations, or set coordinates to values based upon the results of skip signal (probed) locations and calculations. When any of the offsets are read, the interpretation look-ahead queue is stopped until that block is executed.

| Variables       | Legacy Variables   | Usage                                   |
|-----------------|--------------------|-----------------------------------------|
|                 | #5201 - #5206      | G52 X , Y , Z , A , B , C OFFSET VALUES |
|                 | #5221 - #5226      | G54 X , Y , Z , A , B , C OFFSET VALUES |
|                 | #5241 - #5246      | G55 X , Y , Z , A , B , C OFFSET VALUES |
|                 | #5261 - #5266      | G56 X , Y , Z , A , B , C OFFSET VALUES |
|                 | #5281 - #5286      | G57 X , Y , Z , A , B , C OFFSET VALUES |
|                 | #5301 - #5306      | G58 X , Y , Z , A , B , C OFFSET VALUES |
|                 | #5321 - #5326      | G59X , Y , Z , A , B , C OFFSET VALUES  |
| #14001 - #14006 | #7001 - #7006      | G110 (G154 P1) additional work offsets  |
| #14021 - #14026 | #7021 - #7026      | G111 (G154 P2) additional work offsets  |
| #14041 - #14046 | #7041 - #7046      | G112 (G154 P3) additional work offsets  |
| #14061 - #14066 | #7061 - #7066      | G113 (G154 P4) additional work offsets  |
| #14081 - #14086 | #7081 - #7086      | G114 (G154 P5) additional work offsets  |
| #14101 - #14106 | #7101 - #7106      | G115 (G154 P6) additional work offsets  |
| #14121 - #14126 | #7121 - #7126      | G116 (G154 P7) additional work offsets  |
| #14141 - #14146 | #7141 - #7146      | G117 (G154 P8) additional work offsets  |
| #14161 - #14166 | #7161 - #7166      | G118 (G154 P9) additional work offsets  |
| #14181 - #14186 | #7181 - #7186      | G119 (G154 P10) additional work offsets |
| #14201 - #14206 | #7201 - #7206      | G120 (G154 P11) additional work offsets |

| Variables       | Legacy Variables   | Usage                                   |
|-----------------|--------------------|-----------------------------------------|
| #14221 - #14226 | #7221 - #7226      | G121 (G154 P12) additional work offsets |
| #14241 - #14246 | #7241 - #7246      | G122 (G154 P13) additional work offsets |
| #14261 - #14266 | #7261 - #7266      | G123 (G154 P14) additional work offsets |
| #14281 - #14286 | #7281 - #7286      | G124 (G154 P15) additional work offsets |
| #14301 - #14306 | #7301 - #7306      | G125 (G154 P16) additional work offsets |
| #14321 - #14326 | #7321 - #7326      | G126 (G154 P17) additional work offsets |
| #14341 - #14346 | #7341 - #7346      | G127 (G154 P18) additional work offsets |
| #14361 - #14366 | #7361 - #7366      | G128 (G154 P19) additional work offsets |
| #14381 - #14386 | #7381 - #7386      | G129 (G154 P20) additional work offsets |

## 6.70 #6001-#6250 Settings Access with Macro Variables

Access settings  through  variables #20000 - #20999 or #6001 - #6250 ,  starting  from setting 1 respectively. Refer to page 463 for the detailed descriptions of the settings that are available in the control.

<!-- image -->

NOTE:

The #20000 - 20999 range numbers correspond directly to Setting numbers. You should use #6001 - #6250 for settings access only if you need your program to be compatible with older Haas machines.

## 6.71 #6198 Next-Generation Control Identifier

The macro variable #6198 has a read-only value of 1000000.

You can test #6198 in a program to detect the control version, and then conditionally run program code for that control version. For example:

```
% IF[#6198 EQ 1000000] GOTO5 ; (Non-NGC code) ; GOTO6 ;
```

<!-- image -->

## NOTE:

```
N5 (NGC code) ; N6 M30 ; %
```

In this program, if the value stored in #6198 is equal to 1000000, go to Next Generation Control compatible code then end the program. If if the value stored in #6198 is not equal to 1000000, run the non-NGC program and then end the program.

## 6.72 #6996-#6999 Parameter Access With Macro Variables

These macro variables can access all parameters and any of the parameter bits, as follows:

```
#6996 : Parameter Number #6997 : Bit Number (optional) #6998 : Contains the value of the parameter number specified in variable #6996
```

#6999 : Contains the bit value (0 or 1) of the parameter bit specified in variable #6997 .

Variables #6998 and #6999 are read-only.

You  can  also  use  macro  variables #30000 - #39999 ,  starting  from  parameter  1, respectively. Contact your HFO for more details regarding parameter numbers.

## 6.73 Usage

To  access  the  value  of  a  parameter,  copy  the  number  of  that  parameter  into  variable #6996 . The value of that parameter is available in macro variable #6998 , as shown:

```
% #6996=601 (Specify parameter 601) ; #10000=#6998 (Copy the value of parameter 601 to variable #10000) ; %
```

To access a specific parameter bit, copy the parameter number into variable 6996 and the bit number to macro variable 6997. The value of that parameter bit is available in macro variable 6999, as shown:

%

```
#6996=57 (Specify parameter 57) ; #6997=0 (Specify bit zero) ; #10000=#6999 (Copy parameter 57 bit 0 to variable #10000) ; %
```

## 6.74 Pallet Changer Variables

The status of the pallets from the Automatic Pallet Changer is checked with these variables:

| #7501 - #7506   | Pallet priority                          |
|-----------------|------------------------------------------|
| #7601 - #7606   | Pallet status                            |
| #7701 - #7706   | Part program numbers assigned to pallets |
| #7801 - #7806   | Pallet usage count                       |
| #3028           | Number of pallet loaded on receiver      |

## 6.75 #8500-#8515 Advanced Tool Management

These  variables  give  information  on  Advanced  Tool  Management  (ATM).  Set  variable #8500 to the tool group number, then access information for the selected tool group with the read-only macros #8501-#8515.

| #8500   | Advanced Tool Management (ATM). Group ID                        |
|---------|-----------------------------------------------------------------|
| #8501   | ATM. Percent of available tool life of all tools in the group.  |
| #8502   | ATM. Total available tool usage count in the group.             |
| #8503   | ATM. Total available tool hole count in the group.              |
| #8504   | ATM. Total available tool feed time (in seconds) in the group.  |
| #8505   | ATM. Total available tool total time (in seconds) in the group. |
| #8510   | ATM. Next tool number to be used.                               |

| #8511   | ATM. Percent of available tool life of the next tool.    |
|---------|----------------------------------------------------------|
| #8512   | ATM. Available usage count of the next tool.             |
| #8513   | ATM. Available hole count of the next tool.              |
| #8514   | ATM. Available feed time of the next tool (in seconds).  |
| #8515   | ATM. Available total time of the next tool (in seconds). |

## 6.76 #8550-#8567 Advanced Tool Management Tooling

These variables give information on tooling. Set variable #8550 to the tool offset number, then access information for the selected tool with the read-only macros #8551 - #8567 .

<!-- image -->

Macro  variables #1601 - #2800 give  access  to  the  same  data  for individual tools as #8550 - #8567 give for Tool Group tools.

| #8550   | Individual tool ID            |
|---------|-------------------------------|
| #8551   | Number of Flutes on tool      |
| #8552   | Maximum recorded vibration    |
| #8553   | Tool length offset            |
| #8554   | Tool length wear              |
| #8555   | Tool diameter offset          |
| #8556   | Tool diameter wear            |
| #8557   | Actual diameter               |
| #8558   | Programmable coolant position |
| #8559   | Tool feed timer (seconds)     |
| #8560   | Total tool timers (seconds)   |

| #8561   | Tool life monitor limit                      |
|---------|----------------------------------------------|
| #8562   | Tool life monitor counter                    |
| #8563   | Tool load monitor maximum load sensed so far |
| #8564   | Tool load monitor limit                      |

## 6.77 #50001 - #50200 Tool Type

Use macro variables #50001 - #50200, to read or write the tool type set in the tool offset page.

## T6.3: Available Tool Types for Mill

| Tool Type              | Tool Type #   |
|------------------------|---------------|
| Drill                  | 1             |
| Tap                    | 2             |
| Shell Mill             | 3             |
| End Mill               | 4             |
| Spot Drill             | 5             |
| Ball Nose              | 6             |
| Probe                  | 7             |
| Reserve for Future Use | 8-20          |

## 6.78 Variable Usage

All  variables are referenced with a number sign ( # )  followed  by  a  positive  number: #1 , #10001 , and #10501 .

Variables are decimal values that are represented as floating point numbers. If a variable has never been used, it can take on a special undefined value. This indicates that it has not been used. A variable can be set to undefined with the special variable #0 . #0 has the value of undefined or 0.0 depending on its context. Indirect references to variables can be accomplished by enclosing the variable number in brackets: #[&lt;Expression&gt;]

The expression is evaluated and the result becomes the variable accessed. For example:

```
#1=3 ; #[#1]=3.5 + #1 ;
```

This sets the variable #3 to the value 6.5.

A variable can be used in place of a G-code address where address refers to the letters A - Z . In the block:

```
N1 G0 G90 X1.0 Y0 ;
```

the variables can be set to the following values:

```
#7=0 ; #11=90 ; #1=1.0 ; #2=0.0 ;
```

and replaced by:

```
N1 G#7 G#11 X#1 Y#2 ;
```

Values in the variables at runtime are used as the address values.

## 6.79 Address Substitution

The usual method of setting control addresses A - Z is the address followed by a number. For example:

```
G01 X2.5 Y3.7 F20.;
```

sets addresses G , X , Y and F to 1, 1.5, 3.7 and 20.0 respectively and thus instructs the control to move linearly, G01 , to position X=2.5 Y=3.7 at a feed rate of 20 (in/mm). Macro syntax allows the address values to be replaced with any variable or expression.

The previous statement can be replaced by this code:

```
#1=1 ; #2=1.5 ; #3=3.7 ;
```

```
#4=20 ; G#1 X[#1+#2] Y#3 F#4 ;
```

The permissible syntax on addresses A - Z (exclude N or O ) is as follows:

| <address><variable>        | A#101        |
|----------------------------|--------------|
| <address><-><variable>     | A-#101       |
| <address>[<expression>]    | Z[#5041+3.5] |
| <address><->[<expression>] | Z-[SIN[#1]]  |

If the variable value does not agree with the address range, the control generates an alarm. For example, this code causes a range error alarm because the tool diameter numbers range from 0 to 200.

<!-- formula-not-decoded -->

When a variable or expression is used in place of an address value, the value is rounded to the least significant digit. If #1=.123456, then G01 X#1 would move the machine tool to .1235 on the X Axis. If the control is in the metric mode, the machine would be moved to .123 on the X axis.

When an undefined variable is used to replace an address value, that address reference is ignored. For example, if #1 is undefined, then the block

```
G00 X1.0 Y#1 ;
```

becomes

```
G00 X1.0 ;
```

and no Y movement takes place.

## 6.80 Macro Statements

Macro statements are lines of code that allow the programmer to manipulate the control with  features  similar  to  any  standard  programming  language.  Included  are  functions, operators,  conditional  and  arithmetic  expressions,  assignment  statements,  and  control statements.

Functions  and  operators  are  used  in  expressions  to  modify  variables  or  values.  The operators are essential to expressions while functions make the programmer's job easier.

## 6.81 Functions

Functions are built-in routines that the programmer has available to use. All functions have the  form  &lt;function\_name&gt;[argument]  and  return  floating-point  decimal  values.  The functions provided in the Haas control are as follows:

| Function   | Argument   | Returns   | Notes                                |
|------------|------------|-----------|--------------------------------------|
| SIN[ ]     | Degrees    | Decimal   | Sine                                 |
| COS[ ]     | Degrees    | Decimal   | Cosine                               |
| TAN[ ]     | Degrees    | Decimal   | Tangent                              |
| ATAN[ ]    | Decimal    | Degrees   | Arctangent Same as FANUC ATAN[ ]/[1] |
| SQRT[ ]    | Decimal    | Decimal   | Square root                          |
| ABS[ ]     | Decimal    | Decimal   | Absolute value                       |
| ROUND[ ]   | Decimal    | Decimal   | Round off a decimal                  |
| FIX[ ]     | Decimal    | Integer   | Truncate fraction                    |
| ACOS[ ]    | Decimal    | Degrees   | Arc cosine                           |
| ASIN[ ]    | Decimal    | Degrees   | Arcsine                              |
| #[ ]       | Integer    | Integer   | Indirect reference Refer to page 294 |

## 6.82 Notes on Functions

The function ROUND works differently depending on the context that it is used. When used in arithmetic expressions, any number with a fractional part greater than or equal to .5 is rounded up to the next whole integer; otherwise, the fractional part is truncated from the number.

```
% #1=1.714 ; #2=ROUND[#1] (#2 is set to 2.0) ; #1=3.1416 ; #2=ROUND[#1] (#2 is set to 3.0) ; %
```

When ROUND is used in an address expression, metric and angle dimensions are rounded to three-place precision. For inch dimensions, four-place precision is the default.

```
% #1= 1.00333 ; G00 X[ #1 + #1 ] ; (Table X Axis moves to 2.0067) ; G00 X[ ROUND[ #1 ] + ROUND[ #1 ] ] ; (Table X Axis moves to 2.0067) ; G00 A[ #1 + #1 ] ; (Axis rotates to 2.007) ; G00 A[ ROUND[ #1 ] + ROUND[ #1 ] ] ; (Axis rotates to 2.007) ; D[1.67] (Diameter rounded up to 2) ; %
```

## 6.83 Fix vs. Round

```
% #1=3.54 ; #2=ROUND[#1] ; #3=FIX[#1]. %
```

#2 will be set to 4. #3 will be set to 3.

## 6.84 Operators

Operators have (3) categories: Boolean, Arithmetic, and Logical.

## 6.85 Boolean Operators

Boolean operators always evaluate to 1.0 (TRUE) or 0.0 (FALSE). There are six Boolean operators. These operators are not restricted to conditional expressions, but they most often are used in conditional expressions. They are:

- EQ - Equal To

NE - Not Equal To

GT - Greater Than

- LT - Less Than

GE - Greater Than or Equal To

- LE - Less Than or Equal To

Here are four examples of how Boolean and Logical operators can be used:

| Example        | Example        | Explanation                                                                                |
|----------------|----------------|--------------------------------------------------------------------------------------------|
| IF [#1 EQ 0.0] | GOTO100 ;      | Jump to block 100 if value in variable #1 equals 0.0.                                      |
| WHILE [#101    | LT 10] DO1 ;   | While variable #101 is less than 10 repeat loop DO1..END1.                                 |
| #1=[1.0 LT     | 5.0] ;         | Variable #1 is set to 1.0 (TRUE).                                                          |
| IF [#1 AND #2  | EQ #3] GOTO1 ; | If variable #1 AND variable #2 are equal to the value in #3 then control jumps to block 1. |

## 6.86 Arithmetic Operators

Arithmetic operators consist of unary and binary operators. They are:

| +   | - Unary plus         | +1.23                        |
|-----|----------------------|------------------------------|
| -   | - Unary minus        | -[COS[30]]                   |
| +   | - Binary addition    | #1=#1+5                      |
| -   | - Binary subtraction | #1=#1-1                      |
| *   | - Multiplication     | #1=#2*#3                     |
| /   | - Division           | #1=#2/4                      |
| MOD | - Remainder          | #1=27 MOD 20 (#1 contains 7) |

## 6.87 Logical Operators

Logical operators are operators that work on binary bit values. Macro variables are floating point  numbers.  When  logical  operators  are  used  on  macro  variables,  only  the  integer portion of the floating point number is used. The logical operators are:

OR - logically OR two values together

XOR - Exclusively OR two values together

AND - Logically AND two values together

## Examples:

```
% #1=1.0 ; #2=2.0 ; #3=#1 OR #2 ; %
```

Here the variable #3 will contain 3.0 after the OR operation.

```
% #1=5.0 ; #2=3.0 ; IF [[#1 GT 3.0] AND [#2 LT 10]] GOTO1 ;
```

<!-- image -->

NOTE:

%

Here control will transfer to block 1 because #1 GT 3.0 evaluates to 1.0 and #2 LT 10 evaluates to 1.0, thus 1.0 AND 1.0 is 1.0 (TRUE) and the GOTO occurs.

To achieve your desired results, be very careful when you use logical operators.

## 6.88 Expressions

Expressions are defined as any sequence of variables and operators surrounded by the square brackets [ and ] . There are two uses for expressions: conditional expressions or arithmetic  expressions.  Conditional expressions return  FALSE  (0.0)  or  TRUE  (any  non zero)  values.  Arithmetic  expressions  use  arithmetic  operators  along  with  functions  to determine a value.

## 6.89 Arithmetic Expressions

An arithmetic expression is any  expression using variables, operators, or functions.  An arithmetic  expression  returns  a  value.  Arithmetic  expressions  are  usually  used  in assignment statements, but are not restricted to them.

Examples of Arithmetic expressions:

```
% #10001=#10045*#10030 ; #10001=#10001+1 ; X[#10005+COS[#10001]] ; #[#10200+#10013]=0 ; %
```

## 6.90 Conditional Expressions

In the Haas control, all expressions set a conditional value. The value is either 0.0 (FALSE) or the value is nonzero (TRUE). The context in which the expression is used determines if the expression is a conditional expression. Conditional expressions are used in the IF and WHILE statements and in the M99 command. Conditional expressions can make use of Boolean operators to help evaluate a TRUE or FALSE condition.

The M99 conditional construct is unique to the Haas control. Without macros, M99 in the Haas control has the ability to branch unconditionally to any line in the current subprogram by placing a P code on the same line. For example:

```
N50 M99 P10 ;
```

branches to line N10 .  It  does not return control to the calling subprogram. With macros enabled, M99 can be used with a conditional expression to branch conditionally. To branch when variable #10000 is less than 10 we could code the above line as follows:

```
N50 [#10000 LT 10] M99 P10 ;
```

In this case, the branch occurs only when #10000 is less than 10, otherwise processing continues with the next program line in sequence. In the above, the conditional M99 can be replaced with

```
N50 IF [#10000 LT 10] GOTO10 ;
```

## 6.91 Assignment Statements

Assignment statements let you modify variables. The format of the assignment statement is:

```
<expression>=<expression>
```

The expression on the left of the equal sign must always refer to a macro variable, whether directly  or  indirectly.  This  macro  initializes  a  sequence  of  variables  to  any  value.  This example uses both direct and indirect assignments.

```
% O50001 (INITIALIZE A SEQUENCE OF VARIABLES) ; N1 IF [#2 NE #0] GOTO2 (B=base variable) ; #3000=1 (Base variable not given) ; N2 IF [#19 NE #0] GOTO3 (S=size of array) ; #3000=2 (Size of array not given) ; N3 WHILE [#19 GT 0] DO1 ; #19=#19-1 (Decrement count) ; #[#2+#19]=#22 (V=value to set array to) ; END1 ; M99 ; %
```

You could use the above macro to initialize three sets of variables as follows:

```
% G65 P300 B101. S20 (INIT 101..120 TO #0) ; G65 P300 B501. S5 V1. (INIT 501..505 TO 1.0) ; G65 P300 B550. S5 V0 (INIT 550..554 TO 0.0) ; %
```

The decimal point in B101. , etc. would be required.

## 6.92 Control Statements

Control statements allow the programmer to branch, both conditionally and unconditionally. They also provide the ability to iterate a section of code based on a condition.

## 6.93 Unconditional Branch (GOTOnnn and M99 Pnnnn)

In the Haas control, there are two methods of branching unconditionally. An unconditional branch will always branch to a specified block. M99 P15 will branch unconditionally to block number 15. The M99 can be used whether or not macros is installed and is the traditional method for branching unconditionally in the Haas control. GOTO15 does the same as M99 P15 . In the Haas control, a GOTO command can be used on the same line as other G-codes. The GOTO is executed after any other commands like M codes.

## 6.94 Computed Branch (GOTO#n and GOTO [expression])

Computed branching allows the program to transfer control to another line of code in the same subprogram. The control can compute the block while the program runs, using the GOTO [expression] form, or it can pass the block in through a local variable, as in the GOTO#n form.

The GOTO rounds the variable or expression result that is associated with the Computed branch. For instance, if variable #1 contains 4.49 and the program contains a GOTO#1 command, the control attempts to transfer to a block that contains N4 . If #1 contains 4.5, then the control transfers to a block that contains N5 .

Example: You could develop this code skeleton into a program that adds serial numbers to parts:

```
% O50002 (COMPUTED BRANCHING) ; (D=Decimal digit to engrave) ; ;
```

```
IF [[#7 NE #0] AND [#7 GE 0] AND [#7 LE 9]] GOTO99 ; #3000=1 (Invalid digit) ; ; N99; #7=FIX[#7] (Truncate any fractional part) ; ; GOTO#7 (Now engrave the digit) ; ; N0 (Do digit zero) ; M99 ; ; N1 (Do digit one) ; ; M99 ; %
```

With the above subprogram, you would use this call to engrave the fifth digit:

```
G65 P9200 D5 ;
```

Computed GOTO s  using  expression  could  be  used  to  branch  processing  based  on  the results of reading hardware inputs. For example:

```
% GOTO [[#1030*2]+#1031] ; N0(1030=0, 1031=0) ; ...M99 ; N1(1030=0, 1031=1) ; ...M99 ; N2(1030=1, 1031=0) ; ...M99 ; N3(1030=1, 1031=1) ; ...M99 ; % #1030 and #1031 .
```

## 6.95 Conditional Branch (IF and M99 Pnnnn)

Conditional branching allows the program to transfer control to another section of code within the same subprogram. Conditional branching can only be used when macros are enabled.  The  Haas  control  allows  two  similar  methods  for  accomplishing  conditional branching:

```
IF [<conditional expression>] GOTOn
```

As discussed, &lt;conditional expression&gt; is any expression that uses any of the six Boolean operators EQ , NE , GT , LT , GE ,  or LE .  The  brackets  surrounding  the  expression  are mandatory. In the Haas control, it is not necessary to include these operators. For example:

```
IF [#1 NE 0.0] GOTO5 ;
```

could also be:

```
IF [#1] GOTO5 ;
```

In this statement, if the variable #1 contains anything but 0.0, or the undefined value #0 , then branching to block 5 occurs; otherwise, the next block is executed.

In the Haas control, a &lt;conditional expression&gt; is also used with the M99 Pnnnn format. For example:

```
G00 X0 Y0 [#1EQ#2] M99 P5;
```

Here,  the conditional  is for the M99 portion  of  the  statement  only.  The  machine  tool is instructed to go to X0 , Y0 whether or not the expression evaluates to True or False. Only the branch, M99 , is executed based on the value of the expression. It is recommended that the IF GOTO version be used if portability is desired.

## 6.96 Conditional Execution (IF THEN)

Execution of control statements can also be achieved by using the IF THEN construct. The format is:

```
IF [<conditional expression>] THEN <statement> ;
```

<!-- image -->

## NOTE:

To preserve compatibility with FANUC syntax THEN may not be used with GOTOn .

This format is traditionally used for conditional assignment statements such as:

```
IF [#590 GT 100] THEN #590=0.0 ;
```

Variable #590 is set to zero when the value of #590 exceeds 100.0. In the Haas control, if a conditional evaluates to FALSE (0.0), then the remainder of the IF block is ignored. This means that control statements can also be conditioned so that we could write something like:

```
IF [#1 NE #0] THEN G01 X#24 Y#26 F#9 ;
```

This  executes  a  linear  motion  only  if  variable #1 has  been  assigned  a  value.  Another example is:

```
IF [#1 GE 180] THEN #101=0.0 M99 ;
```

This says that if variable #1 (address A ) is greater than or equal to 180, then set variable #101 to zero and return from the subprogram.

Here is an example of an IF statement that branches if a variable has been initialized to contain any  value. Otherwise, processing  continues and  an  alarm  is  generated. Remember, when an alarm is generated, program execution is halted.

```
% N1 IF [#9NE#0] GOTO3 (TEST FOR VALUE IN F) ; N2 #3000=11(NO FEED RATE) ; N3 (CONTINUE) ; %
```

## 6.97 Iteration/Looping (WHILE DO END)

Essential to all programming languages is the ability to execute a sequence of statements a given number of times or to loop through a sequence of statements until a condition is met. Traditional G coding allows this with the use of the L address. A subprogram can be executed any number of times by using the L address.

```
M98 P2000 L5 ;
```

This  is  limited  since  you  cannot  terminate  execution  of  the  subprogram  on  condition. Macros allow flexibility with the WHILE-DO-END construct. For example:

```
% WHILE [<conditional expression>] DOn ; <statements> ; ENDn ; %
```

This executes the statements between DOn and ENDn as long as the conditional expression evaluates  to  True.  The  brackets  in  the  expression  are  necessary.  If  the  expression evaluates to False, then the block after ENDn is executed next. WHILE can be abbreviated to WH . The DOn - ENDn portion of the statement is a matched pair. The value of n is 1-3. This means that there can be no more than three nested loops per subprogram. A nest is a loop within a loop.

Although nesting of WHILE statements can only be up to three levels, there really is no limit since each subprogram can have up to three levels of nesting. If there is a need to nest to a level greater than 3, then the segment containing the three lowest levels of nesting can be made into a subprogram thus overcoming the limitation.

If two separate WHILE loops are in a subprogram, they can use the same nesting index. For example:

```
% #3001=0 (WAIT 500 MILLISECONDS) ; WH [#3001 LT 500] DO1 ; END1 ; <Other statements> #3001=0 (WAIT 300 MILLISECONDS) ; WH [#3001 LT 300] DO1 ; END1 ; %
```

You can use GOTO to jump out of a region encompassed by a DO - END , but you cannot use a GOTO to jump into it. Jumping around inside a DO - END region using a GOTO is allowed.

An infinite loop can be executed by eliminating the WHILE and expression. Thus,

```
% DO1 ; <statements>
```

<!-- image -->

## CAUTION:

```
END1 ; %
```

executes until the RESET key is pressed.

The following code can be confusing:

```
% WH [#1] D01 ; END1 ; %
```

In this example, an alarm results indicating no Then was found; Then refers to the D01 . Change D01 (zero) to DO1 (letter O).

## 6.98 Communication With External Devices - DPRNT[ ]

Macros allow additional capabilities  to communicate with  peripheral  devices.  With  user provided devices you can digitize parts, provide runtime inspection reports, or synchronize controls.

## 6.99 Formatted Output

The DPRNT statement lets programs send formatted text to the serial port. DPRNT can print any text and any variable to the serial port. The form of the DPRNT statement is as follows:

```
DPRNT [<text> <#nnnn[wf]>... ] ;
```

DPRNT must be the only command in the block. In the previous example, &lt;text&gt; is any character from A to Z or the letters (+,-,/,*, ., ?, and the space). When an asterisk is output, it  is  converted  to  a  space.  The &lt;#nnnn[wf]&gt; is  a  variable  followed  by  a  format.  The variable number can be any macro variable. The format [wf] is required and consists of two digits within square brackets. Remember that macro variables are real numbers with a whole part and a fractional part. The first digit in the format designates the total places reserved in the output for the whole  part. The second digit  designates the  total  places reserved for the fractional part. The control can use any number from 0-9 for both whole and fractional parts.

A decimal point is printed out between the whole part and the fractional part. The fractional part  is  rounded  to  the  least  significant  place.  When  zero  places  are  reserved  for  the fractional part, then no decimal point is printed out. Trailing zeros are printed if there is a fractional part. At least one place is reserved for the whole part, even when a zero is used. If the value of the whole part has fewer digits than have been reserved, then leading spaces are output. If the value of the whole part has more digits than has been reserved, then the field is expanded so that these numbers are printed.

The control sends a carriage return after every DPRNT block.

DPRNT[ ] Example:

| Code                                     | Output                            |
|------------------------------------------|-----------------------------------|
| #1= 1.5436 ;                             |                                   |
| DPRNT[X#1[44]*Z#1[03]*T#1[40]] ;         | X1.5436 Z 1.544 T 1               |
| DPRNT[***MEASURED*INSIDE*DIAMETER** *] ; | MEASURED INSIDE DIAMETER          |
| DPRNT[] ;                                | (no text, only a carriage return) |
| #1=123.456789 ;                          |                                   |
| DPRNT[X-#1[35]] ;                        | X-123.45679 ;                     |

## 6.100 DPRNT[ ] Settings

Setting 261 determines the destination for DPRNT statements. You can choose to output them to a file, or to a TCP port. Settings 262 and 263 specify the destination for DPRNT output. Refer to the Settings section of this manual for more information.

## 6.101 Execution

DPRNT statements are executed at look-ahead time. This means that you must be careful about where the DPRNT statements appear in the program, particularly if the intent is to print out.

G103 is useful for limiting lookahead. If you wanted to limit look-ahead interpretation to one block, you would include this command at the start of your program: This causes the control to look ahead (2) blocks.

```
G103 P1 ;
```

To cancel the lookahead limit, change the command to G103 P0 . G103 cannot be used when cutter compensation is active.

## 6.102 Editing

Improperly structured or improperly placed macro statements will generate an alarm. Be careful when editing expressions; brackets must be balanced.

The DPRNT[ ] function can be edited much like a comment. It can be deleted, moved as a whole item, or individual items within the bracket can be edited. Variable references and format expressions must be altered as a whole entity. If you wanted to change [24] to [44], place the cursor so that [24] is highlighted, enter [44] and press [ENTER] . Remember, you can use the jog handle to maneuver through long DPRNT[ ] expressions.

Addresses  with  expressions  can  be  somewhat  confusing.  In  this  case,  the  alphabetic address stands alone. For instance, this block contains an address expression in X :

```
G01 G90 X [COS [90]] Y3.0 (CORRECT) ;
```

Here, the X and brackets stand-alone and are individually editable items. It is possible, through editing, to delete the entire expression and replace it with a floating-point constant.

```
G01 G90 X 0 Y3.0 (WRONG) ;
```

The above block will result in an alarm at runtime. The correct form looks as follows:

```
G01 G90 X0 Y3.0 (CORRECT) ;
```

<!-- image -->

## NOTE:

There is no space between the X and the Zero (0). REMEMBER when you see an alpha character standing alone it is an address expression.

## 6.103 G65 Macro Subprogram Call Option (Group 00)

G65 is the command that calls a subprogram with the ability to pass arguments to it. The format follows:

```
G65 Pnnnnn [Lnnnn] [arguments] ;
```

Arguments italicized in square  brackets  are optional. See  the Programming section  for more details on macro arguments.

The G65 command requires a P address corresponding to a program number currently located in the control's drive or path to a program. When the L address is used the macro call is repeated the specified number of times.

When a subprogram is called, the control looks for the subprogram on the active drive or the path to the program. If the subprogram cannot be located on the active drive, the control looks in the drive designated by Setting 251. Refer to the Setting Up Search Locations section for more information on subprogram searching. An alarm occurs if the control does not find the subprogram.

In  Example  1,  subprogram  1000  is  called  once  without  conditions  passed  to  the subprogram. G65 calls are similar to, but not the same as, M98 calls. G65 calls can be nested up to 9 times, which means, program 1 can call program 2, program 2 can call program 3 and program 3 can call program 4.

If an M-code is placed on the same line as a G65 it must go after G65. For  example: M14  G65  P1000 will  generate Alarm 339 Multiple codes while G65 P1000 M14 will work.

```
Example 1: % G65 P1000 (Call subprogram O01000 as a macro) ; M30 (Program stop) ; O01000 (Macro Subprogram) ; ... M99 (Return from Macro Subprogram) ; %
```

<!-- image -->

NOTE:

<!-- image -->

NOTE:

In Example 2, the program LightHousing.nc is called using the path that it is in.

## Example 2:

```
% G65 P15 A1. B1.; G65 (/Memory/LightHousing.nc) A1. B1.;
```

Paths are case sensitive.

<!-- image -->

NOTE:

In Example 3, subprogram 9010 is designed to drill a sequence of holes along a line whose slope is determined by the X and Y arguments that are passed to it in the G65 command line. The Z drill depth is passed as Z , the feed rate is passed as F , and the number of holes to be drilled is passed as T . The line of holes is drilled starting from the current tool position when the macro subprogram is called.

Example 3:

The subprogram program O09010 should reside on the active drive or on a drive designated by Setting 252.

```
% G00 G90 X1.0 Y1.0 Z.05 S1000 M03 (Position tool) ; G65 P9010 X.5 Y.25 Z.05 F10. T10 (Call O09010) ; M30 ; O09010 (Diagonal hole pattern) ; F#9 (F=Feedrate) ; WHILE [#20 GT 0] DO1 (Repeat T times) ; G91 G81 Z#26 (Drill To Z depth) ; #20=#20-1 (Decrement counter) ; IF [#20 EQ 0] GOTO5 (All holes drilled) ; G00 X#24 Y#25 (Move along slope) ; N5 END1 ; M99 (Return to caller) ; %
```

## 6.104 G66 Modal Macro Subprogram Call Option / G67 Modal Macro Subprogram Call Cancel(Group 00)

G66 works similarly to G65 but is modal. It turns on calls for a subprogram with the ability to pass arguments to it. It is canceled with G67. The format follows:

```
G66 Pnnnnn [Lnnnn] [arguments];
```

Arguments italicized in square  brackets  are optional. See  the Programming section  for more details on macro arguments.

The G66 command requires a P address corresponding to a program number currently located in the control's drive or path to a program. When the L address is used, the macro call is repeated the specified number of times.

Like G65 calls,  G66 can be nested up to nine times, which means program 1 can call program 2, program 2 can call program 3, and program 3 can call program 4.

When a subprogram is called, the control looks for it on the active drive or the path to the program. If it cannot be located on the active drive, the control looks in the drive designated by Setting 251. Refer to the Setting Up Search Locations section for more information on subprogram searching. An alarm occurs if the control does not find the subprogram.

If the subprogram program specified by the P code is not should reside on the active drive or on a drive designated by Setting 252.

In the example, subprogram 9010 is called once at each XY location with conditions passed to the subprogram, 'a b d f r'.

## Example 1:

```
% G66 P9010 a b d f r;M30 (Program stop) ; XY (Call O09010); XY (Call O09010); XY (Call O09010); XY (Call O09010); %
```

Paths are case sensitive. In Example 2, In this example O01066 is the Main Program which makes use of a G66 P1067 call, which calls up subprogram O01067 which is embedded in this same script example.

```
O01066 (G81 TO G66 DRILL CYCLE); (G66 AVAILABLE IN NGC SW 100.23.000.1201);
```

```
M06 T1 (DRILL); M03 S1500; G54 G00 G90 X1. Y-1.5 (HOLE 1 XY); G54 G00 G90 X1. Y-1.5 (HOLE 1 XY); G54 G00 G90 X1. Y-1.5 (HOLE 1 XY); G43 H01 Z0.1; / G66 P1067 Z-2.25 R0.1 F15. I0.125 J1. (MODAL MACRO CALL); X2. (HOLE 2); X3. (HOLE 3); G67 (MODAL MACRO OFF); G00 Z2.; G00 Z2.; M30; (G66: Modal Macro Call); Z = #26 = Drill Cycle Maximum Depth); (R = #18 = Clearance Plane); (F = #9  = Feedrate); (I = #4  = Extrusion Wall Thickness); (J = #5  = Extrusion Height); O01067(G66 SUBPROGRAM, DRILL-RAPID-DRILL); (NOTE THAT A / BLOCKS LOOKAHEAD, MAKES LOCAL VARIABLES EASIER TO SEE ON MACRO PAGE); / G01 G91 Z - [ 0.2 + #4 ] F#9; / G00 G90 Z - [ #5 - #4 - 0.1 ]; / G01 G90 Z - [ #5 + 0.1 ]; / G00 G90 Z#18; (COPY LOCAL VAR. TO GLOBAL VAR.) (JUST FOR TROUBLESHOOTING) #100= #9 (F); #101= #18 (R); #102= #26 (Z); #103= #4 (I); #104= #5 (J); M99 (RETURN TO MAIN PROGRAM); (G66: Modal Macro Call); (Z = #26 = Drill Cycle Maximum Depth); (R = #18 = Clearance Plane); (F = #9  = Feedrate); (I = #4  = Extrusion Wall Thickness); (J = #5  = Extrusion Height); %
```

## F6.24: In the above example J is the height of the extrusion, I is the wall thickness of the extrusion, and H is the height of the clearance plane.

<!-- image -->

## 6.105 Aliasing

Aliased codes are user defined G and M-codes that reference a macro program. There are 10 G alias codes and 10 M alias codes available to users. Program numbers 9010 through 9019 are reserved for G-code aliasing and 9000 through 9009 are reserved for M-code aliasing.

Aliasing is a means of assigning a G-code or M-code to a G65 P##### sequence. For instance, in the previous Example 2, it would be easier to write:

G06 X.5 Y.25 Z.05 F10. T10 ;

When aliasing, variables can be passed with a G-code; variables cannot be passed with an M-code.

Here,  an  unused  G-code  has  been  substituted, G06 for G65  P9010 .  In  order  for  the previous block to work, the value associated with subprogram 9010 must be set to 06. Refer to the Setting Aliases section for how to setup aliases.

G00 , G65 , G66 , and G67 cannot be aliased. All other codes between 1 and 255 can be used for aliasing.

If a macro call subprogram is set to a G-code and the subprogram is not in memory, then an alarm is given. Refer to the G65 Macro Subprogram Call section on page 311 on how to locate the subprogram. An alarm occurs if the sub-program is not found.

<!-- image -->

NOTE:

## 6.106 Setting Aliases

The G-code or M-code alias setup is done on the Alias Codes window. To setup an alias:

1. Press [SETTING] and navigate to the Alias Codes tab.
2. Press [EMERGENCY STOP] on the control.
3. Using the cursor keys select the M or G Macro Call to be used.
4. Enter the number of the G-code or M-code you want to alias. For example, if you want to alias G06 type 06.
5. Press [ENTER] .
6. Repeat steps 3 - 5 for other aliased G or M-codes.
7. Release the [EMERGENCY STOP] on the control.

Setting an alias value to 0 disables aliasing for the associated subprogram.

F6.25: Alias Codes Window

<!-- image -->