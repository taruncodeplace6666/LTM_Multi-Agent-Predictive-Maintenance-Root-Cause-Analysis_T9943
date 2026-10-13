## Chapter 7: G-codes

## 7.1 List of G-codes

<!-- image -->

## CAUTION:

<!-- image -->

NOTE:

The sample programs in this manual have been tested for accuracy, but they are for illustrative purposes only. The programs do not define tools, offsets, or materials. They do not describe workholding or other fixturing. If you choose to run a sample program on your machine, do so in Graphics mode. Always follow safe machining practices when you run an unfamiliar program.

The sample programs in this manual represent a very conservative programming style. The samples are intended to demonstrate safe and reliable programs, and they are not necessarily the fastest or most efficient  way  to  operate  a  machine.  The  sample  programs  use G-codes that you might choose not to use in more efficient programs.

| Code   | Description                       |   Group |   Page |
|--------|-----------------------------------|---------|--------|
| G00    | Rapid Motion Positioning          |      01 |    322 |
| G01    | Linear Interpolation Motion       |      01 |    323 |
| G02    | Circular Interpolation Motion CW  |      01 |    325 |
| G03    | Circular Interpolation Motion CCW |      01 |    325 |
| G04    | Dwell                             |      00 |    332 |
| G09    | Exact Stop                        |      00 |    332 |
| G10    | Set Offsets                       |      00 |    333 |
| G12    | Circular Pocket Milling CW        |      00 |      5 |
| G13    | Circular Pocket Milling CCW       |      00 |      5 |
| G17    | XY Plane Selection                |      02 |    337 |

| Code   | Description                            | Group    |   Page |
|--------|----------------------------------------|----------|--------|
| G18    | XZ Plane Selection                     | 02       |    337 |
| G19    | YZ Plane Selection                     | 02       |    337 |
| G20    | Select Inches                          | 06       |    337 |
| G21    | Select Metric                          | 06       |    337 |
| G28    | Return To Machine Zero Point           | 00       |    337 |
| G29    | Return From Reference Point            | 00       |    338 |
| G31    | Feed Until Skip                        | 00       |    338 |
| G35    | Automatic Tool Diameter Measurement    | 00       |    340 |
| G36    | Automatic Work Offset Measurement      | 00       |    342 |
| G37    | Automatic Tool Offset Measurement      | 00       |    344 |
| G40    | Cutter Compensation Cancel             | 07       |    345 |
| G41    | 2D Cutter Compensation Left            | 07       |    345 |
| G42    | 2D Cutter Compensation Right           | 07       |    345 |
| G43    | Tool Length Compensation + (Add)       | 08       |    346 |
| G44    | Tool Length Compensation - (Subtract)  | 08       |    346 |
| G47    | Text Engraving                         | 00       |    347 |
| G49    | G43 / G44 / G143 Cancel                | 08       |    353 |
| G50    | Cancel Scaling                         | 11       |    353 |
| G51    | Scaling                                | 11       |    353 |
| G52    | Set Work Coordinate System             | 00 or 12 |    358 |
| G53    | Non-Modal Machine Coordinate Selection | 00       |    358 |
| G54    | Select Work Coordinate System #1       | 12       |    359 |
| G55    | Select Work Coordinate System #2       | 12       |    359 |

| Code    | Description                           |   Group |   Page |
|---------|---------------------------------------|---------|--------|
| G56     | Select Work Coordinate System #3      |      12 |    359 |
| G57     | Select Work Coordinate System #4      |      12 |    359 |
| G58     | Select Work Coordinate System #5      |      12 |    359 |
| G59     | Select Work Coordinate System #6      |      12 |    359 |
| G60     | Uni-Directional Positioning           |      00 |    359 |
| G61     | Exact Stop Mode                       |      15 |    359 |
| G64     | G61 Cancel                            |      15 |    359 |
| G65     | Macro Subprogram Call Option          |      00 |    359 |
| G66/G67 | Modal Macro Subprogram Call Option    |      00 |    361 |
| G68     | Rotation                              |      16 |    363 |
| G69     | Cancel G68 Rotation                   |      16 |    367 |
| G70     | Bolt Hole Circle                      |      00 |    367 |
| G71     | Bolt Hole Arc                         |      00 |    368 |
| G72     | Bolt Holes Along an Angle             |      00 |    368 |
| G73     | High-Speed Peck Drilling Canned Cycle |      09 |    369 |
| G74     | Reverse Tap Canned Cycle              |      09 |    371 |
| G76     | Fine Boring Canned Cycle              |      09 |    371 |
| G77     | Back Bore Canned Cycle                |      09 |    373 |
| G80     | Canned Cycle Cancel                   |      09 |    375 |
| G81     | Drill Canned Cycle                    |      09 |    375 |
| G82     | Spot Drill Canned Cycle               |      09 |    377 |
| G83     | Normal Peck Drilling Canned Cycle     |      09 |    378 |
| G84     | Tapping Canned Cycle                  |      09 |    381 |

| Code   | Description                             |   Group |   Page |
|--------|-----------------------------------------|---------|--------|
| G85    | Boring Canned Cycle                     |      09 |    382 |
| G86    | Bore and Stop Canned Cycle              |      09 |    383 |
| G89    | Bore In, Dwell, Bore Out Canned Cycle   |      09 |    384 |
| G90    | Absolute Position Command               |      03 |    385 |
| G91    | Incremental Position Command            |      03 |    385 |
| G92    | Set Work Coordinate Systems Shift Value |      00 |    385 |
| G93    | Inverse Time Feed Mode                  |      05 |    386 |
| G94    | Feed Per Minute Mode                    |      05 |    386 |
| G95    | Feed per Revolution                     |      05 |    386 |
| G98    | Canned Cycle Initial Point Return       |      10 |    382 |
| G99    | Canned Cycle R Plane Return             |      10 |    388 |
| G100   | Cancel Mirror Image                     |      00 |    389 |
| G101   | Enable Mirror Image                     |      00 |    389 |
| G103   | Limit Block Buffering                   |      00 |    390 |
| G107   | Cylindrical Mapping                     |      00 |    391 |
| G110   | #7 Coordinate System                    |      12 |    392 |
| G111   | #8 Coordinate System                    |      12 |    392 |
| G112   | #9 Coordinate System                    |      12 |    392 |
| G113   | #10 Coordinate System                   |      12 |    392 |
| G114   | #11 Coordinate System                   |      12 |    392 |
| G115   | #12 Coordinate System                   |      12 |    392 |
| G116   | #13 Coordinate System                   |      12 |    392 |
| G117   | #14 Coordinate System                   |      12 |    392 |

| Code   | Description                              |   Group |   Page |
|--------|------------------------------------------|---------|--------|
| G118   | #15 Coordinate System                    |      12 |    392 |
| G119   | #16 Coordinate System                    |      12 |    392 |
| G120   | #17 Coordinate System                    |      12 |    392 |
| G121   | #18 Coordinate System                    |      12 |    392 |
| G122   | #19 Coordinate System                    |      12 |    392 |
| G123   | #20 Coordinate System                    |      12 |    392 |
| G124   | #21 Coordinate System                    |      12 |    392 |
| G125   | #22 Coordinate System                    |      12 |    392 |
| G126   | #23 Coordinate System                    |      12 |    392 |
| G127   | #24 Coordinate System                    |      12 |    392 |
| G128   | #25 Coordinate System                    |      12 |    392 |
| G129   | #26 Coordinate System                    |      12 |    392 |
| G136   | Automatic Work Offset Center Measurement |      00 |    392 |
| G141   | 3D+ Cutter Compensation                  |      07 |    394 |
| G143   | 5-Axis Tool Length Compensation +        |      08 |    397 |
| G150   | General Purpose Pocket Milling           |      00 |    399 |
| G154   | Select Work Coordinates P1-P99           |      12 |    407 |
| G156   | Broaching Canned Cycle                   |      09 |    409 |
| G167   | Modify Setting                           |      00 |    412 |
| G174   | CCW Non-Vertical Rigid Tap               |      00 |    413 |
| G184   | CW Non-Vertical Rigid Tap                |      00 |    413 |
| G187   | Setting the Smoothness Level             |      00 |    413 |
| G234   | Tool Center Point Control (TCPC)         |      08 |    414 |

| Code   | Description                                             |   Group |   Page |
|--------|---------------------------------------------------------|---------|--------|
| G253   | G253 Orient Spindle Normal To Feature Coordinate System |      00 |    419 |
| G254   | Dynamic Work Offset (DWO)                               |      23 |    419 |
| G255   | Cancel Dynamic Work Offset (DWO)                        |      23 |    423 |
| G266   | Visible Axes Linear Rapid % Motion                      |      00 |    424 |
| G268 / | Enable Feature Coordinate System                        |      14 |    424 |
| G269   | Disable Feature Coordinate System                       |      14 |    424 |
| G280   | Turn off safe run                                       |      00 |    426 |
| G281   | Turn on safe run                                        |      00 |    426 |

## 7.1.1 G00 Rapid Motion Positioning (Group 01)

* X - Optional X-Axis motion command
* Y - Optional Y-Axis motion command
* Z - Optional Z-Axis motion command
* A - Optional A-Axis motion command
* B - Optional B-Axis motion command
* C - Optional C-axis motion command
* E - Optional code to specify the rapid rate of the block as a percent.

## *indicates optional

G00 is used to move the machine axes at the maximum speed. It is primarily used to quickly position the machine to a given point before each feed (cutting) command. This G code is modal, so a block with G00 causes all following blocks to be rapid motion until another Group 01 code is specified.

A rapid move also cancels an active canned cycle, just like G80 does.

Generally, rapid motion will not be in a single straight line. Each axis specified moves  at  its  maximum  speed,  but  all  axes  will  not necessarily  complete their  motions  at the same  time. The  machine waits until all motions are complete before starting the next command.

<!-- image -->

NOTE:

## F7.1: G00 Multi-linear Rapid Motion

<!-- image -->

Setting  57  (Exact  Stop  Canned  X-Y)  can  change  how  closely  the  machine  waits  for  a precise stop before and after a rapid move.

## 7.1.2 G01 Linear Interpolation Motion (Group 01)

- F - Feedrate
* X - X-Axis motion command
* Y - Y-Axis motion command
* Z - Z-Axis motion command
* A - A-Axis motion command
* B - B-Axis motion command
* C - C-axis motion command
* ,R - Radius of the arc
* ,C - Chamfer distance

*indicates optional

G01 moves the axes at a commanded feed rate. It is primarily used to cut the workpiece. A G01 feed  can  be  a  single  axis  move  or  a  combination  of  the  axes.  The  rate  of  axes movement is controlled by feedrate ( F ) value. This F value can be in units (inch or metric) per minute ( G94 ) or per spindle revolution ( G95 ), or time to complete the motion ( G93 ). The feedrate value ( F ) can be on the current program line, or a previous line. The control will always use the most recent F value until another F value is commanded. If in G93 , an F value is used on each line. Refer also to G93 .

G01 is a modal command, which means that it will stay in effect until canceled by a rapid command such as G00 or a circular motion command like G02 or G03 .

Once a G01 is started all programmed axes move and reach the destination at the same time. If an axis is not capable of the programmed feedrate the control will not proceed with the G01 command and an alarm (max feedrate exceeded) will be generated.

## Corner Rounding and Chamfering Example

F7.2: Corner Rounding and Chamfering Example #1

<!-- image -->

```
% O60011 (G01 CORNER ROUNDING & CHAMFER) ; (G54 X0 Y0 is at the top-right of part) ; (Z0 is on top of the part) ; (T1 is an end mill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-0.5 F20. (Feed to cutting depth) ; Y-5. ,C1. (Chamfer) ; X-5. ,R1. (Corner-round) ; Y0 (Feed to Y0.) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; % 5.000 R1.000 X0. Y0. 1.000 x 45° 5.000
```

A chamfer block or a corner-rounding block can be automatically inserted between two linear interpolation blocks by specifying ,C (chamfering) or ,R (corner rounding). There must be a terminating linear interpolation block after the beginning block (a G04 pause may intervene).

<!-- image -->

These two linear interpolation blocks specify a corner of intersection. If the beginning block specifies a ,C , the value after the ,C is the distance from the intersection to where the chamfer begins, and also the distance from the intersection to where the chamfer ends. If the beginning block specifies an ,R , the value after the ,R is the radius of a circle tangent to the corner at two points: the beginning of the corner-rounding arc and the endpoint of that arc. There can be consecutive blocks with chamfering or corner rounding specified. There must be movement on the two axes specified by the selected plane, whether the active plane is XY ( G17 ), XZ ( G18 ) or YZ ( G19 ).

## 7.1.3 G02 CW / G03 CCW Circular Interpolation Motion (Group 01)

- F
- Feedrate
* I - Distance along X Axis to center of circle
* J - Distance along Y Axis to center of circle
* K - Distance along Z Axis to center of circle
* R - Radius of circle
* X - X-Axis motion command
* Y - Y-Axis motion command
* Z - Z-Axis motion command
* A - A-Axis motion command

*indicates optional

I , J and K is the preferred method to program a radius. R is suitable for general radii.

These G codes are used to specify circular motion. Two axes are necessary to complete circular motion and the correct plane, G17 - G19 , must be used. There are two methods of commanding a G02 or G03 , the first is using the I , J , K addresses and the second is using the R address.

## Using I, J, K addresses

I , J and K address are used to locate the arc center in relation to the start point. In other words, the I , J , K addresses are the distances from the starting point to the center of the circle. Only the I , J , or K specific to the selected plane are allowed ( G17 uses IJ , G18 uses IK and G19 uses JK ). The X , Y , and Z commands specify the end point of the arc. If the X , Y , and Z location for the selected plane is not specified, the endpoint of the arc is the same as the starting point for that axis.

To cut a full circle the I , J , K addresses must be used; using an R address will not work. To cut a full circle, do not specify an ending point ( X , Y , and Z ); program I , J , or K to define the center of the circle. For example:

```
G02 I3.0 J4.0 (Assumes G17; XY plane) ;
```

## Using the R address

The R -value defines the distance from the starting point to the center of the circle. Use a positive R -value for radii of 180° or less, and a negative R -value for radii more than 180°.

## Programming Example

## F7.3: Positive R Address Programming Example

<!-- image -->

```
% O60021 (G02 POSITIVE R ADDRESS) ; (G54 X0 Y0 is at the bottom-left of part) ; (Z0 is on top of the part) ; (T1 is a .5 in dia endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X-0.25 Y-0.25 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-0.5 F20. (Feed to cutting depth) ; G01 Y1.5 F12. (Feed to Y1.5) ; G02 X1.884 Y2.384 R1.25 (CW circular motion) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; % 1.5 135 O R 1.00 .5Ø
```

## F7.4: Negative R Address Programming Example

```
% O60022 (G02 NEGATIVE R ADDRESS) ; (G54 X0 Y0 is at the bottom-left of part) ; (Z0 is on top of the part) ; (T1 is a .5 in dia endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X-0.25 Y-0.25 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-0.5 F20. (Feed to cutting depth) ; G01 Y1.5 F12. (Feed to Y1.5) ; G02 X1.884 Y0.616 R-1.25 (CW circular motion) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; % 225 O .5Ø 1.5 R 1.00
```

## Thread Milling

Thread milling uses a standard G02 or G03 move to create the circular move in X-Y, then adds a Z move on the same block to create the thread pitch. This generates one turn of the thread; the multiple teeth of the cutter generate the rest. Typical block of code:

```
N100 G02  I-1.0 Z-.05  F5. (generates  1-inch radius  for 20-pitch thread) ;
```

<!-- image -->

<!-- image -->

NOTE:

Thread milling notes:

Internal holes smaller than 3/8 inch may not be possible or practical. Always climb cut the cutter.

Use a G03 to cut I.D. threads or a G02 to cut O.D. threads. An I.D. right hand thread will move up in the Z-Axis by the amount of one thread pitch. An O.D. right hand thread will move down in the Z-Axis by the amount of one thread pitch. PITCH = 1/Threads per inch (Example - 1.0 divided by 8 TPI = .125)

This program I.D. thread mills a 1.5 diameter x 8 TPI hole with a 0.750" diameter x 1.0" thread hob.

1. To start, take the hole diameter (1.500). Subtract the cutter diameter .750 and then divide by 2. (1.500 - .75) / 2 = .375
2. The result (.375) is the distance the cutter starts from the I.D. of the part.
2. After the initial positioning, the next step of the program is to turn on cutter compensation and move to the I.D. of the circle.
3. The next step is to program a complete circle ( G02 or G03 ) with a Z-Axis command of the amount of one full pitch of the thread (this is called Helical Interpolation).
4. The last step is to move away from the I.D. of the circle and turn off cutter compensation.

You cannot turn cutter compensation off or on during an arc movement. You must program a linear move, either in the X or Y Axis, to move the tool to and from the diameter to cut. This move will be the maximum compensation amount that you can adjust.

## Thread Milling Example

## F7.5: Thread Milling Example, 1.5 Diameter X 8 TPI: [1]Tool Path, [2] Turn on and off cutter compensation.

<!-- image -->

Many thread mill manufacturers offer free online software to help you create your threading programs.

```
% O60023 (G03 THREAD MILL 1.5-8 UNC) ; (G54 X0 Y0 is at the center of the bore) ; (Z0 is on top of the part) ;
```

<!-- image -->

NOTE:

```
(T1 is a .5 in dia thread mill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-0.5156 F50. (Feed to starting depth) ; (Z-0.5 minus 1/8th of the pitch = Z-0.5156) ; G41 X0.25 Y-0.25 F10. D01 (cutter comp on) ; G03 X0.5 Y0 I0 J0.25 Z-0.5 (Arc into thread) ; (Ramps up by 1/8th of the pitch) ; I-0.5 J0 Z-0.375 F20. (Cuts full thread) ; (Z moving up by the pitch value to Z-0.375) ; X0.25 Y0.25 I-0.25 J0 Z-0.3594 (Arc out of thread) ; (Ramp up by 1/8th of the pitch) ; G40 G01 X0 Y1 (cutter comp off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; % N5 = XY at the center of the hole N7 = Thread depth, minus 1/8 pitch N8 = Enable Cutter Compensation N9 = Arcs into thread, ramps up by 1/8 pitch N10 = Cuts full thread, Z moving up by the pitch value N11 = Arcs out of thread, ramps up 1/8 pitch
```

- N12 = Cancel Cutter Compensation

Maximum cutter compensation adjustability is 0.175.

Outside Diameter (O.D.) Thread Milling

F7.6: O.D. Thread Milling Example, 2.0 diameter post x 16 TPI: [1] Tool Path [2] Rapid Positioning, Turn on and off cutter compensation, [3] Start Position, [4] Arc with Z.

<!-- image -->

```
% O60024 (G02 G03 THREAD MILL 2.0-16 UNC) ; (G54 X0 Y0 is at the center of the post) ; (Z0 is on top of the opost) ; (T1 is a .5 in dia thread mill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y2.4 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G00 Z-1. (Rapids to Z-1.) ; G01 G41 D01 X-0.5 Y1.4 F20. (Linear move) ; (Cutter comp on) ; G03 X0 Y0.962 R0.5 F25. (Arc into thread) ; G02 J-0.962 Z-1.0625 (Cut threads while lowering Z) ; G03 X0.5 Y1.4 R0.5 (Arc out of thread) ; G01 G40 X0 Y2.4 F20. (Linear move) ; (Cutter comp off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

A cutter compensation move can consist of any X or Y move from any position  as  long  as  the  move  is  greater  than  the  amount  being compensated.

## Single-Point Thread Milling

<!-- image -->

NOTE:

This program is for a 1.0" diameter hole with a cutter diameter of 0.500" and a thread pitch of 0.125 (8TPI). This program positions itself in Absolute G90 and then switches to G91 Incremental mode on line N7 .

The use of an Lxx value on line N10 allows us to repeat the thread milling arc multiple times, with a Single-Point Thread Mill.

```
% O60025 (G03 SNGL PNT THREAD MILL 1.5-8 UNC) ; (G54 X0 Y0 is at the center of the bore) ; (Z0 is on top of the part) ; (T1 is a .5 in dia thread mill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G91 G01 Z-0.5156 F50. (Feed to starting depth) ; (Z-0.5 minus 1/8th of the pitch = Z-0.5156) ; G41 X0.25 Y-0.25 F20. D01 (Cutter comp on) ; G03 X0.25 Y0.25 I0 J0.25 Z0.0156 (Arc into thread) ; (Ramps up by 1/8th of the pitch) ; I-0.5 J0 Z0.125 L5 (Thread cut, repeat 5 times) ; X-0.25 Y0.25 I-0.25 J0 Z0.0156 (Arc out of thread) ; (Ramps up by 1/8th of the pitch) ; G40 G01 X-0.25 Y-0.25 (Cutter comp off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## Specific line description:

```
N5 = XY at the center of the hole N7 = Thread depth, minus 1/8 pitch. Switches to G91 N8 = Enable Cutter Compensation N9 = Arcs into thread, ramps up by 1/8 pitch
```

- N10 = Cuts full thread, Z moving up by the pitch value

<!-- image -->

NOTE:

<!-- image -->

NOTE:

- N11 = Arcs out of thread, ramps up 1/8 pitch
- N12 = Cancel Cutter Compensation
- N13 = Switches back to G90 Absolute positioning

## Helical Motion

Helical (spiral) motion is possible with G02 or G03 by programming the linear axis that is not in the selected plane. This third axis will be moved along the specified axis in a linear manner, while the other two axes will be moved in the circular motion. The speed of each axis will be controlled so that the helical rate matches the programmed feedrate.

## 7.1.4 G04 Dwell (Group 00)

- P - The dwell time in seconds or milliseconds

The P values are modal. This means if you are in the middle of a canned cycle and a G04 Pnn or an M97 Pnn is used the P value will be used for the dwell / subprogram as well as the canned cycle.

G04 specifies  a  delay  or  dwell  in  the  program.  The  block  with G04 delay  for  the  time specified by the P address code. For example:

G04 P10.0. ;

Delays the program for 10 seconds.

G04  P10. is  a  dwell  of  10  seconds; G04  P10 is  a  dwell  of  10 milliseconds. Make sure you use decimal points correctly so that you specify the correct dwell time.

## 7.1.5 G09 Exact Stop (Group 00)

G09 code is used to specify a controlled axes stop. It affects only the block in which it is commanded. It is non-modal and does not affect the blocks that come after the block where it is commanded. Machine moves decelerate to the programmed point before the control processes the next command.

## 7.1.6 G10 Set Offsets (Group 00)

G10 lets  you set offsets within the program. G10 replaces manual offset entry (i.e. Tool length and diameter, and work coordinate offsets).

```
L - Selects offset category. L2 Work coordinate origin for G52 and G54-G59 L10 Length offset amount (for H code) L1 or L11 Tool wear offset amount (for H code) L12 Diameter offset amount (for D code) L13 Diameter wear offset amount (for D code) L14 Sets max tool speed (for P code and R code) L20 Auxiliary work coordinate origin for G110 - G129 P - Selects a specific offset. P1 - P200 Used to reference D or H code offsets ( L10 - L13 ) or Specifies Tool Number ( L14 ) P0 G52 references work coordinate ( L2 ) P1 - P6 G54 - G59 references work coordinates ( L2 ) P1 - P20 G110 - G129 references auxiliary coordinates ( L20 ) P1 - P99 G154 reference auxiliary coordinate ( L20 ) * R Offset value or increment for length and diameter. * X X-Axis zero location. * Y Y-Axis zero location. * Z Z-Axis zero location. * A A-Axis zero location. * B B-Axis zero location. * C C-Axis zero location. *indicates optional % O60100 (G10 SET OFFSETS) ; G10 L2 P1 G91 X6.0 ; (Move coordinate G54 6.0 to the right) ; ; G10 L20 P2 G90 X10. Y8. ; (Set work coordinate G111 to X10.0 Y8.0) ; ; G10 L10 G90 P5 R2.5 ; (Set offset for Tool #5 to 2.5) ; ; G10 L12 G90 P5 R.375 ; (Set diameter for Tool #5 to .375') ; ; G10 L14 P5 R500 ; (Set max RPM for Tool #5 to 500) ; ;
```

<!-- image -->

NOTE:

```
G10 L20 P50 G90 X10. Y20. ; (Set work coordinate G154 P50 to X10. Y20.) ; %
```

## 7.1.7 G12 Circular Pocket Milling CW / G13 Circular Pocket Milling CCW (Group 00)

These G-codes mill circular shapes. They are different only in that G12 uses a clockwise direction  and G13 uses a counterclockwise direction. Both G-codes use the  default XY circular plane ( G17 ) and imply the use of G42 (cutter compensation) for G12 and G41 for G13 . G12 and G13 are non-modal.

* D - Tool radius or diameter selection**
- F - Feedrate
- I - Radius of first circle (or finish if no K ). I value must be greater than Tool Radius, but less than K value.
* K - Radius of finished circle (if specified)
* L - Loop count for repeating deeper cuts
* Q - Radius increment, or stepover (must be used with K)
- Z - Depth of cut or increment

*indicates optional

**To get the programmed circle diameter, the control uses the selected D code tool size. To program tool centerline select D0 .

Specify D00 if you do not want to use cutter compensation. If you do not specify a D value in the G12 / G13 block, the control uses the last commanded D value, even if it was previously canceled with a G40 .

Rapid-position the tool to the center of the circle. To remove all the material inside the circle, use I and Q values less than the tool diameter and a K value equal to the circle radius. To cut a circle radius only, use an I value set to the radius and no K or Q value.

```
% O60121(SAMPLE G12 AND G13) ; (G54 X0 Y0 is center of first pocket) ; (Z0 is on top of the part) ; (T1 is a .25 in. dia endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ;
```

```
G43 H01 Z0.1 (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G12 I0.75 F10. Z-1.2 D01 (Finish pocket CW) ; G00 Z0.1 (Retract) ; X5.(Move to center of next pocket) ; G12 I0.3 K1.5 Q1. F10. Z-1.2 D01 ; (Rough & finish CW) ; G00 Z0.1 (Retract) ; X10.(Move to center of next pocket) ; G13 I1.5 F10. Z-1.2 D01 (Finish CCW) ; G00 Z0.1 (Retract) ; X15. (Move to center of the last pocket) ; G13 I0.3 K1.5 Q0.3 F10. Z-1.2 D01 ; (Rough & finish CCW) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## F7.7: Circular Pocket Milling, G12 Clockwise shown: [1] I only, [2] I, K and Q only.

<!-- image -->

These G codes assume cutter compensation, so you do not need to program G41 or G42 in the program block. However, you must include a D offset number, for cutter radius or diameter, to adjust the circle diameter.

These program examples show the G12 and G13 format, and the different ways that you can write these programs.

Single Pass: Use I only.

Applications:  One-pass counter  boring;  rough  and  finish  pocketing  of smaller  holes,  ID cutting of O-ring grooves.

Multiple Pass: Use I , K , and Q .

Applications: Multiple-pass counter boring; rough and finish pocketing of large holes with cutter overlap.

Multiple Z-Depth Pass: Using I only, or I , K , and Q ( G91 and L may also be used).

Applications: Deep rough and finish pocketing.

The previous figures show the tool path during the pocket milling G-codes.

Example G13 multiple-pass using I , K , Q , L , and G91 :

This program uses G91 and an L count of 4 , so this cycle will execute a total of four times. The Z depth increment is 0.500. This is multiplied by the L count, making the total depth of this hole 2.000.

```
% O60131 (G13 G91 CCW EXAMPLE) ; (G54 X0 Y0 is center of 1st pocket) ; (Z0 is on top of the part) ; (T1 is a 0.5 in. dia endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G13 G91 Z-.5 I.400 K2.0 Q.400 L4 D01 F20. ; (Rough & finish CCW) ; (BEGIN COMPLETION BLOCKS) ; G00 G90 Z0.1 M09 (Rapid retract, coolant off) ; G53 G49 Z0 M05 (Z home, spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

The G91 and L count can also be used in a G13 I only line.

## 7.1.8 G17 XY / G18 XZ / G19 YZ Plane Selection (Group 02)

The face of the workpiece to have a circular milling operation ( G02 , G03 , G12 , G13 ) done to it must have two of the three main axes ( X , Y and Z ) selected. One of three G codes is used to select the plane, G17 for XY , G18 for XZ , and G19 for YZ . Each is modal and applies to all subsequent circular motions. The default plane selection is G17 , which means that a circular motion in the XY plane can be programmed without selecting G17 . Plane selection also applies to G12 and G13 , circular pocket milling, (always in the XY plane).

If cutter radius compensation is selected ( G41 or G42 ), only use the XY plane ( G17 )  for circular motion.

G17 Defined - Circular motion with the operator looking down on the XY table from above. This defines the motion of the tool relative to the table.

G18 Defined - Circular motion is defined as the motion for the operator looking from the rear of the machine toward the front control panel.

G19 Defined - Circular motion is defined as the motion for the operator looking across the table from the side of the machine where the control panel is mounted.

F7.8: G17 , G18 , and G19 Circular Motion Diagrams: [1] Top view, [2] Front view, [3] Right view.

<!-- image -->

## 7.1.9 G20 Select Inches / G21 Select Metric (Group 06)

Use G20 (inch) and G21 (mm) codes are to make sure that the inch/metric selection is set correctly for the program. Use Setting 9 to select between inch and metric programming. G20 in a program causes an alarm if Setting 9 is not set to inch.

## 7.1.10 G28 Return to Machine Zero Point (Group 00)

The G28 code  returns  all  axes  ( X , Y , Z , A and B )  simultaneously  to  the  machine  zero position when no axis is specified on the G28 line.

Alternatively, when one or more axes locations are specified on the G28 line, G28 will move to the specified locations and then to machine zero. This is called the G29 reference point; it is saved automatically for optional use in G29 .

Setting 108 affects the way that rotary axes return when you command a G28 . Refer to page 488 for more information.

```
% G28 G90 X0 Y0 Z0 (moves to X0 Y0 Z0) ; G28 G90 X1. Y1. Z1. (moves to X1. Y1. Z1.) ; G28 G91 X0 Y0 Z0 (moves directly to machine zero) ; G28 G91 X-1. Y-1. Z-1 (moves incrementally -1.) ; %
```

## 7.1.11 G29 Return From Reference Point (Group 00)

G29 moves the axes to a specific position. The axes selected in this block are moved to the G29 reference point saved in G28 ,  and then moved to the location specified in the G29 command.

## 7.1.12 G31 Feed Until Skip (Group 00)

(This G-code is optional and requires a probe)

This G-code is used to record a probed location to a macro variable.

```
F - Feedrate * X - X-Axis absolute motion command * Y - Y-Axis absolute motion command * Z - Z-Axis absolute motion command * A - A-Axis absolute motion command * B - B-Axis absolute motion command
```

* C - C-axis absolute motion command (UMC)

*indicates optional

This G-code moves the programmed axes while looking for a signal from the probe (skip signal). The specified move is started and continues until the position is reached or the probe receives a skip signal. If the probe receives a skip signal during the G31 move, axis motion stops, the control beeps and records the skip signal position to macro variables. The program will then execute the next line of code. If the probe does not receive a skip signal during the G31 move, the control will not beep and the skip signal position will be recorded at the end of the programmed move. The program will continue. This G-code requires at least  one  Axis  specified  and  a  feedrate.  If  the  command  contains  neither,  an  alarm  is generated.

Macro variables #5061 through #5066 are designated to store skip signal positions for each axis. For more information about these skip signal variables see the macro section of this manual.

Notes:

This code is non-modal and only applies to the block of code in which G31 is specified.

Do not use Cutter Compensation ( G41 , G42 ) with a G31 .

The G31 line must have a Feed command. To avoid damaging the probe, use a feed rate below F100 . (inch) or F2500 . (metric).

Turn on the probe before using G31 .

If your mill has the standard Renishaw probing system, use the following commands to turn on the probe.

Use the following code to turn on the spindle probe.

```
M59 P3 ;
```

Use the following code to turn on the tool-setting probe.

```
M59 P2 ; G04 P1.0 ; M59 P3 ;
```

Use the following code to turn off either probe.

```
M69 P3 ;
```

Also see M75 , M78 and M79 ;

Sample program:

This sample program measures the top surface of a part with the spindle probe traveling in the Z negative direction. To use this program, the G54 part location must be set at, or close to the surface to be measured.

```
% O60311 (G31 SPINDLE PROBE) ; (G54 X0. Y0. is at the center of the part) ; (Z0. is at, or close to the surface) ; (T1 is a Spindle probe) ; (PREPARATION) ; T1 M06 (Select Tool 1) ; G00 G90 G54 X0 Y0 (Rapid to X0. Y0.) ; M59 P3 (Spindle probe on) ; G43 H1 Z1. (Activate tool offset 1) ; (PROBING) ;
```

```
G31 Z-0.25 F50. (Measure top surface) ; Z1. (Retract to Z1.) ; M69 P3 (Spindle probe off) ; (COMPLETION) ; G00 G53 Z0. (Rapid retract to Z home) ; M30 (End program) ; %
```

## 7.1.13 G35 Automatic Tool Diameter Measurement (Group 00)

(This G-code is optional and requires a probe)

This G-code is used to set a tool diameter offset.

```
F - Feedrate * D - Tool diameter offset number * X - X-Axis command * Y - Y-Axis command
```

*indicates optional

Automatic  Tool  Diameter  Offset  Measurement  function  ( G35 )  is  used  to  set  the  tool diameter (or radius) using two touches of the probe; one on each side of the tool. The first point is set with a G31 block using an M75 , and the second point is set with the G35 block. The distance between these two points is set into the selected (non-zero) Dnnn offset.

Setting 63 Tool Probe Width is used to reduce the measurement of the tool by the width of the tool probe. See the settings section of this manual for more information about Setting 63.

This G-code moves the axes to the programmed position. The specified move is started and continues until the position is reached or the probe sends a signal (skip signal).

## NOTES:

This code is non-modal and only applies to the block of code in which G35 is specified.

Do not use Cutter Compensation ( G41 , G42 ) with a G35 .

To avoid damaging the probe, use a feed rate below F100 . (inch) or F2500 . (metric).

Turn on the tool-setting probe before using G35 .

If your mill has the standard Renishaw probing system, use the following commands to turn on the tool-setting probe.

```
M59 P2 ; G04 P1.0 ; M59 P3 ;
```

Use the following commands to turn off the tool-setting probe.

```
M69 P3 ;
```

Turn on the spindle in reverse ( M04 ), for a right handed cutter.

```
Also see M75 , M78 , and M79 . Also see G31 .
```

Sample program:

This sample program measures the diameter of a tool and records the measured value to the tool offset page. To use this program, the G59 Work Offset location must be set to the tool-setting probe location.

```
% O60351 (G35 MEASURE AND RECORD TOOL DIA OFFSET) ; (G59 X0 Y0 is the tool setting probe location) ; (Z0 is at the surface of tool-setting probe) ; (T1 is a spindle probe) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G59 X0 Y-1. (Rapid tool next to probe) ; M59 P2 (Select tool-setting probe) ; G04 P1. (Dwell for 1 second) ; M59 P3 (Probe on) ; G43 H01 Z1. (Activate tool offset 1) ; S200 M04 (Spindle on CCW) ; (BEGIN PROBING BLOCKS) ; G01 Z-0.25 F50. (Feed tool below surface of probe) ; G31 Y-0.25 F10. M75 (Set reference point) ; G01 Y-1. F25. (Feed away from the probe) ; Z0.5 (Retract above the probe) ; Y1. (Move over the probe in Y-axis) ; Z-0.25 (Move tool below surface of the probe) ; G35 Y0.205 D01 F10. ; (Measure & record tool diameter) ; (Records to tool offset 1); G01 Y1. F25. (Feed away from the probe) ; Z1. (Retract above the probe) ; M69 P3 (Probe off) ; (BEGIN COMPLETION BLOCKS) ; G00 G53 Z0. (Rapid retract to Z home) ; M30 (End program) ;
```

%

## 7.1.14 G36 Automatic Work Offset Measurement (Group 00)

(This G-code is optional and requires a probe)

This G-code is used to set work offsets with a probe.

- F - Feedrate
* I - Offset distance along X-Axis
* J - Offset distance along Y-Axis
* K - Offset distance along Z-Axis
* X - X-Axis motion command
* Y - Y-Axis motion command
* Z - Z-Axis motion command

*indicates optional

Automatic  Work  Offset  Measurement  ( G36 )  is  used  to  command  a  probe  to  set  work coordinate offsets. A G36 will feed the axes of the machine in an effort to probe the work piece with a spindle mounted probe. The axis (axes) will move until a signal from the probe is received or the end of the programmed move is reached. Tool compensation ( G41 , G42 , G43 , or G44 ) must not be active when this function is performed. The point where the skip signal is received becomes the zero position for the currently active work coordinate system of each axis programmed. This G-code requires at least one Axis specified, if neither are found, an alarm is generated.

If an I , J , or K is specified, the appropriate axis work offset is shifted by the amount in the I , J , or K command. This allows the work offset to be shifted away from where the probe actually contacts the part.

## NOTES:

This code is non-modal and only applies to the block of code in which G36 is specified.

The points probed are offset by the values in Settings 59 through 62. See the settings section of this manual for more information.

Do not use Cutter Compensation ( G41 , G42 ) with a G36 .

Do not use tool length Compensation ( G43 , G44 ) with G36

To avoid damaging the probe, use a feed rate below F100 . (inch) or F2500 . (metric).

Turn on the spindle probe before using G36 .

If your mill has the standard Renishaw probing system, use the following commands to turn on the spindle probe.

Use the following commands to turn off the spindle probe.

```
M69 P3 ; Also see M78 , and M79 . % O60361 (G36 AUTO WORK OFFSET MEASUREMENT) ; (G54 X0 Y0 is at the top-center of the part) ; (Z0 is at the surface of part) ; (T1 is a Spindle probe) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 20) ; G00 G90 G54 X0 Y1. (Rapid to 1st position) ; (BEGIN PROBING BLOCKS) ; M59 P3 (Spindle probe on) ; Z-.5 (Move the probe below surface of part) ; G01 G91 Y-0.5 F50. (Feed towards the part) ; G36 Y-0.7 F10. (Measure and record Y offset) ; G91 Y0.25 F50. (Move incrementally away from part) ; G00 Z1. (Rapid retract above part) ; M69 P3 (Spindle probe off) ; (BEGIN COMPLETION BLOCKS) ; G00 G90 G53 Z0. (Rapid retract to Z home) ; M30 (End program) ; %
```

## 7.1.15 G37 Automatic Tool Offset Measurement (Group 00)

(This G-code is optional and requires a probe)

This G-code is used to set tool length offsets.

- F - Feed rate
- H - Tool offset number
- Z - Required Z-Axis offset

Automatic Tool Length Offset Measurement ( G37 ) is used to command a probe to set tool length offsets. A G37 will feed the Z-Axis in an effort to probe a tool with a tool-setting probe. The Z-Axis will move until a signal from the probe is received or the travel limit is reached. A non-zero H code and either G43 or G44 must be active. When the signal from the probe is received (skip signal) the Z position is used to set the specified tool offset ( Hnnn ). The resulting tool offset is the distance between the current work coordinate zero point and the point where the probe is touched. If a non-zero Z value is on the G37 line  of  code  the resulting tool offset will be shifted by the non-zero amount. Specify Z0 for no offset shift.

The work coordinate system ( G54 , G55 , etc.) and the tool length offsets

( H01 - H200 ) may be selected in this block or the previous block.

## NOTES:

This code is non-modal and only applies to the block of code in which G37 is specified.

A non-zero H code and either G43 or G44 must be active.

To avoid damaging the probe, use a feed rate below F100 . (inch) or F2500 . (metric).

Turn on the tool-setting probe before using G37 .

If your mill has the standard Renishaw probing system, use the following commands to turn on the tool-setting probe.

```
M59 P2 ; G04 P1. ; M59 P3 ;
```

Use the following command to turn off the tool-setting probe.

```
M69 P3 ;
```

Also see M78 and M79 .

Sample program:

This sample program measures the length of a tool and records the measured value on the tool  offset  page.  To  use  this  program,  the G59 work  offset  location  must  be  set  to  the tool-setting probe location.

```
% O60371 (G37 AUTO TOOL OFFSET MEASUREMENT) ; (G59 X0 Y0 is center of tool-setting probe) ; (Z0 is at the surface of tool-setting probe) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G59 X0 Y0 (Rapid to center of the probe) ; G00 G43 H01 Z5. (Activate tool offset 1) ; (BEGIN PROBING BLOCKS) ; M59 P2 (Select tool-setting probe) ; G04 P1. (Dwell for 1 second) ; M59 P3 (Probe on) ; G37 H01 Z0 F30. (Measure & record tool offset) ; M69 P3 (Probe off) ; (BEGIN COMPLETION BLOCKS) ; G00 G53 Z0. (Rapid retract to Z home) ; M30 (End program) ; %
```

## 7.1.16 G40 Cutter Comp Cancel (Group 07)

G40 cancels G41 or G42 cutter compensation.

## 7.1.17 G41 2D Cutter Compensation Left / G42 2D Cutter Comp. Right (Group 07)

G41 will  select  cutter  compensation  left;  that  is,  the  tool  is  moved  to  the  left  of  the programmed path to compensate for the size of the tool. A D address must be programmed to  select  the correct  tool  radius  or  diameter  offset.  If  the  value  in  the  selected  offset  is negative,  cutter  compensation  will  operate  as  though G42 (Cutter  Comp  Right.)  was specified.

The right or left side of the programmed path is determined by looking at the tool as it moves away. If the tool needs to be on the left of the programmed path as it moves away, use G41 . If it needs to be on the right of the programmed path as it moves away, use G42 . For more information, refer to the Cutter Compensation section.

## 7.1.18 G43 Tool Length Compensation + (Add) / G44 Tool Length Comp - (Subtract) (Group 08)

A G43 code selects tool length compensation in the positive direction; the tool length in the offsets page is added to the commanded axis position. A G44 code selects tool length compensation in the negative direction; the tool length in the offsets page is subtracted from the commanded axis position. A non-zero H address must be entered to select the correct entry from the offsets page.

<!-- image -->

NOTE:

Starting  in  NGC Software Version 100.21.000.1100, the tool length offset behavior has been modified on Haas machines in the following ways: By default, tool length offsets will now always be applied, unless a G49/H00 (Mill)  or Txx00 offset  (Lathe)  is  explicitly  specified.  On mills, when  a  tool change  occurs, the tool length offset will automatically update to match the new tool. The current tool length offset and mill group 8 code will now persist through power cycles.

## 7.1.19 G47 Text Engraving (Group 00)

G47 lets you engrave a line of text, or sequential serial numbers, with a single G-code. To use G47, Settings 29 (G91 Non-Modal) and 73 (G68 Incremental Angle) must be OFF .

<!-- image -->

NOTE:

Engraving along an arc is not supported.

<!-- image -->

NOTE:

* D - Controls the smoothness level, D1 (rough), D2 (medium), or D3 (finish). If D is not used then default is D3.
* E - Plunge feed rate (units/min)
- F - Engraving feed rate (units/min)
* I - Angle of rotation (-360. to +360.); default is 0
* K - Sets the max corner rounding value. If K is not used then default is K 0.002 inch or 0.002 mm depending on how setting 9 is set.
* J - Height of text in in/mm (minimum = 0.001 inch); default is 1.0 inch (1.0 mm)
- P - 0 for literal text engraving
- 1 for sequential serial number engraving
- 2 for the date and time formated as (MM/DD/YYYY HH:MM:SS)
- 32-126 for ASCII characters
* R - Return plane
* X - X start of engraving (When using G17 plane)
* Y - Y start of engraving (When using G17 plane)
* Z - Depth of cut (When using G17 plane)
* Y - Y start of engraving (When using G19 plane)
* Z - Z start of engraving (When using G19 plane)
* X - Depth of cut (When using G19 plane)
- *indicates optional

## Literal Text Engraving

This method is used to engrave text on a part. The text should be in the form of a comment on the same line as the G47 command. For example, G47 P0 (TEXT TO ENGRAVE) , will engrave TEXT TO ENGRAVE on the part.

On Mills G47 can only be used on the G17 plane while on Lathes G47 can be used on either the G17 or G19 plane. G47 can not be used on the G18 plane.

<!-- image -->

## NOTE:

Corner rounding can cause engraved characters to appear rounded and  make  them  harder  to  read.  To  improve  the  sharpness  and readability  of  engraved  text,  consider  lowering  the  corner-rounding values  with  a G187 E.xxx value  before  the G47 command. Suggested starting E values  are E0.002 (inch)  or E0.05 (metric). Command  a  G187  alone  after  the  engraving  cycle  to  restore  the default corner-rounding level. Refer to the example below:

```
G187 E.002 (PREFACE ENGRAVING WITH A G187 E.xxx); G47 P0 X.15 Y0. I0. J.15 R.1 Z-.004 F80. E40. (Engraving Text); G00 G80 Z0.1; G187 (RESTORE NORMAL CORNER ROUNDING FOR SMOOTHNESS);
```

The characters available for engraving are:

```
A-Z, a-z 0-9, and ` ~ ! @ # $ % ^ & * - _ = + [ ] { } \ | ; : ' ' , . / < > ?
```

Not all of these characters can be entered from the control. When programming from the mill  keypad,  or  engraving  parenthesis  (),  refer  to  the  following  Engraving  Special Characters section.

This example creates the figure shown.

```
% O60471 (G47 TEXT ENGRAVING) ; (G54 X0 Y0 is at the bottom-left of part) ; (Z0 is on top of the part) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y2. (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G47 P0 (TEXT TO ENGRAVE) X2. Y2. I45. J0.5 R0.05 Z-0.005 F15. E10. ; (Starts at X2. Y2., engraves text at 45 deg) ; (BEGIN COMPLETION BLOCKS) ; G00 G80 Z0.1 (Cancel canned cycle) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ;
```

<!-- formula-not-decoded -->

## F7.9: Engraving Program Example

<!-- image -->

In this example, G47 P0 selects literal string engraving. X2.0 Y2.0 sets the starting point for the text at the bottom left corner of first letter. I45. places the text at a positive 45° angle. J.5 sets the text height to 0.5 units-in/mm. R.05 retracts cutter to 0.05 units above part after engraving. Z-0.005 sets an engraving depth of -0.005 units. F15.0 sets an engraving,  XY  move,  feedrate  of  15  units  per  minute. E10.0 sets  a  plunge,  -Z  move, feedrate of 10 units per minute.

## Special Characters

Engraving Special Characters involves using G47 with specific P values ( G47 P32-126 ).

P - values to engrave specific characters

## T7.1: G47 P Values for Special Characters

|   32 |    | space                 | 59    | ;   | semicolon           |
|------|----|-----------------------|-------|-----|---------------------|
|   33 | !  | exclamation mark      | 60    | <   | less than           |
|   34 | "  | double quotation mark | 61    | =   | equals              |
|   35 | #  | number sign           | 62    | >   | greater than        |
|   36 | $  | dollar sign           | 63    | ?   | question mark       |
|   37 | %  | percent sign          | 64    | @   | at sign             |
|   38 | &  | ampersand             | 65-90 | A-Z | capitol letters     |
|   39 | '  | closed single quote   | 91    | [   | open square bracket |

| 40    | (   | open parenthesis   | 92     | \      | backslash             |
|-------|-----|--------------------|--------|--------|-----------------------|
| 41    | )   | close parenthesis  | 93     | ]      | closed square bracket |
| 42    | *   | asterisk           | 94     | ^      | caret                 |
| 43    | +   | plus sign          | 95     | _      | underscore            |
| 44    | ,   | comma              | 96     | '      | open single quote     |
| 45    | -   | minus sign         | 97-122 | a-z    | lowercase letters     |
| 46    | .   | period             | 123    | {      | open curly bracket    |
| 47    | /   | slash              | 124    | &#124; | vertical bar          |
| 48-57 | 0-9 | numbers            | 125    | }      | closed curly bracket  |
| 58    | :   | colon              | 126    | ~      | tilde                 |

## Example:

To engrave $2.00, you need (2) blocks of code. The first block uses a P36 to engrave the dollar sign ($), and the second block uses P0 (2.00) .

Shift the X/Y start location between the first and second line of code to make a space between the dollar sign and the 2.

This is the only method to engrave parenthesis ().

## Engraving Sequential Serial Numbers

This  method  is  used  to  engrave  numbers  on  a  series  of  parts  with  the  number  being increased by one each time. The # symbol is used to set the number of digits in the serial number. For example, G47 P1 (####) , limits the number to four digits while ( ## ) would limit the serial number to two digits.

This program engraves a four digit serial number.

```
% O00037 (SERIAL NUMBER ENGRAVING) ; T1 M06 ; G00 G90 G98 G54 X0. Y0. ; S7500 M03 ; G43 H01 Z0.1 ;
```

<!-- image -->

NOTE:

```
G47 P1 (####) X2. Y2. I0. J0.5 R0.05 Z-0.005 F15. E10. ; G00 G80 Z0.1 ; M05 ; G28 G91 Z0 ; M30 ; %
```

## Initial Serial Number

There  are  two  ways  to  set  the  initial  serial  number  to  be  engraved.  The  first  requires replacing the # symbols within the parenthesis with the first number to be engraved. With this method, nothing is engraved when the G47 line is executed (it is only setting the initial serial number). Execute this once and then change the value within the parenthesis back to # symbols to engrave normally.

The following example will set the initial serial number to be engraved to 0001. Run this code once and then change (0001) to (####).

```
G47 P1 (0001) ;
```

The second method for setting the initial serial number to be engraved is to change the Macro Variable where this value is stored (Macro Variable 599 ). The Macros option does not need to be enabled.

Press [CURRENT COMMANDS] then press [PAGE UP] or [PAGE DOWN] as needed to display the MACRO VARIABLES page. From that screen, enter 599 and press Down cursor.

Once 599 is highlighted on the screen, type in the initial serial number to engrave, [1] for example, then press [ENTER] .

The same serial number can be engraved multiple times on the same part with the use of a macro statement. The macros option is required. A macro statement as shown below could  be  inserted  between  two G47 engraving  cycles  to  keep  the  serial  number  from incrementing to the next number. For more details, see the Macros section of this manual.

```
Macro Statement: #599=[#599-1]
```

## Engraving Around the Outside of a Rotary Part (G47, G107)

You can combine a G47 Engraving cycle with a G107 Cylindrical Mapping cycle to engrave text (or a serial number) along the outside diameter of a rotary part.

This code engraves a four digit serial number along the outer diameter of a rotary part.

```
% O01832 (CHANNEL ON 1.5 ROTARY PART); (MOUNT ROTARY ON RIGHT SIDE OF TABLE);
```

```
(X ZERO IS FACE OF STOCK); (Y ZERO IS ROTARY CL)(TOUCH OFF TOOLS ON TOP OF PART); (STOCK IS 1.5 DIA); (T11 = ENGRAVING TOOL); (WRAP ENGRAVING AROUND CYLINDER, G107 G47); T11 M06; M11; M03 S12000; G57 G90 G00 G17 G40 G80; X0.323 Y0. A0. (START POINT OF ENGRAVE); G43 H11 Z0.1; / G107 A0. Y0. R0.75; G187 P3 E0.002; G47 P0 (ROTARY) X0.323 Y0.177 I45. J0.15 R0.05 Z-0.004 F30. E10.; G00 Z0.1; G187; G107; T11 M06; M11; M03 S12000; G57 G90 G00 G17 G40 G80; X0.323 Y0. A0. (START POINT OF ENGRAVE); G43 H11 Z0.1; / G107 A0. Y0. R0.75; G187 P3 E0.002; G47 P1 (S/N ####) X0.79 Y-0.28 I45. J0.15 R0.05 Z-0.004 F30. E10.; G00 Z2. M09; G107; G90 G00 A70.; G53 G00 G90 Y0; G187; M30; %
```

## Engraving Date and time

Using the address code P2 with G47 will engrave the Date and time the engraving is being done. The date and time format will be MM/DD/YYYY HH:MM:SS

This code engraves the date and time.

```
% O62649 (DATE AND TIME ENGRAVING - DEFAULT P2 TEXT) (G54 X0. Y0. IS BOTTOM LEFT CORNER)
```

<!-- image -->

## NOTE:

```
(G54 Z0. IS TOP OF PART) (T1 - ENGRAVING TOOL) G20 G40 G49 G54 G90  (SAFE START UP); T1 M06;G00 G54 X2. Y1.  (ENGRAVING START POSITION); S10000 M03  (START SPINDLE CW); G43 H01 Z0.1  (ACTIVATE TOOL OFFSET 1); M08  (COOLANT ON); (ENGRAVING WILL BE FORMATTED AS MM/DD/YYYY HH:MM:SS); G47 P2 X2. Y1. I35. J0.4 R0.05 Z-0.002 F40. E15.;G00 Z1. M09 (BACK OFF PART); G28; M30; %
```

For more details on this cycle, refer to the G107 section.

## 7.1.20 G49 Tool Length Compensation Cancel (Group 08)

This G code cancels tool length compensation.

An H0 , M30 , and [RESET] will also cancel tool length compensation.

## 7.1.21 G50 Cancel Scaling (Group 11)

G50 cancels the optional scaling feature. Any axis scaled by a previous G51 command is no longer in effect.

## 7.1.22 G51 Scaling (Group 11)

<!-- image -->

NOTE:

You  must  purchase  the  Rotation  and  Scaling  option  to  use  this G-code. A 200-hour option tryout is also available; refer to page 238 for instructions.

```
* X - Center of scaling for the X Axis * Y - Center of scaling for the Y Axis * Z - Center of scaling for the Z Axis
```

* P - Scaling factor for all axes; three-place decimal from 0.001 to 999.999

*indicates optional

```
G51 [X...] [Y...] [Z...] [P...] ;
```

The control always uses a scaling center to determine the scaled position. If you do not specify  a  scaling  center  in  the G51 command  block,  then  the  control  uses  the  last commanded position as the scaling center.

With a scaling ( G51 ) command, the control multiplies by a scaling factor ( P ) all X , Y , Z , A , B , and C end points for rapids, linear feeds, and circular feeds. G51 also scales I , J , K , and R for G02 and G03 . The control offsets all of these positions relative to a scaling center.

There are (3) ways to specify the scaling factor:

- A P address code in the G51 block applies the specified scaling factor to all axes.
- Setting 71 applies its value as a scaling factor to all axes if it has a nonzero value and you do not use a P address code.
- Settings 188, 189, and 190 apply their values as scaling factors to the X, Y, and Z axes independently if you do not specify a P value and Setting 71 has a value of zero. These settings must have equal values to use them with G02 or G03 commands.

G51 affects all appropriate positioning values in the blocks after the G51 command.

These example programs show how different scaling centers affect the scaling command.

## F7.10: G51 No Scaling Gothic Window: [1] Work coordinate origin.

<!-- image -->

```
% O60511 (G51 SCALING SUBPROGRAM) ; (G54 X0 Y0 is at the bottom left of window) ; (Z0 is on top of the part) ; (Run with a main program) ; (BEGIN CUTTING BLOCKS) ; G01 X2. ; Y2. ; G03 X1. R0.5 ; G01 Y1. ; M99 ; %
```

The first example illustrates how the control uses the current work coordinate location as a scaling center. Here, it is X0 Y0 Z0 .

- F7.11: G51 Scaling Current Work Coordinates: The Origin [1] is the work origin and the center of scaling.

<!-- image -->

```
% o60512 (G51 SCALING FROM ORIGIN) ; (G54 X0 Y0 is at the bottom left of part) ; (Z0 is on top of the part) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 M08 (Activate tool offset 1) ; (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-0.1 F25. (Feed to cutting depth) ; M98 P60511 (Cuts shape without scaling) ; G00 Z0.1 (Rapid Retract) ; G00 X2. Y2. (Rapid to new scale position) ; G01 Z-.1 F25. (Feed to cutting depth) ; G51 X0 Y0 P2. (2x scale from origin) ; M98 P60511 (run subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09(Rapid retract, Coolant off) ; G50 (CANCELS G51); G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

The next example specifies the center of the window as the scaling center.

## F7.12: G51 Scaling Center of Window: [1] Work coordinate origin, [2] Center of scaling.

<!-- image -->

```
% o60513 (G51 SCALING FROM CENTER OF WINDOW) ; (G54 X0 Y0 is at the bottom left of part) ; (Z0 is on top of the part) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 M08 (Activate tool offset 1) ; (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-0.1 F25. (Feed to cutting depth) ; M98 P60511 (Cuts shape without scaling) ; G00 Z0.1 (Rapid Retract) ; G00 X0.5 Y0.5 (Rapid to new scale position) ; G01 Z-.1 F25. (Feed to cutting depth) ; G51 X1.5 Y1.5 P2. (2x scale from center of window) ; M98 P60511 (run subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09(Rapid retract, Coolant off) ; G50 (CANCELS G51); G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

The last example illustrates how scaling can be placed at the edge of tool paths as if the part was being set against locating pins.

F7.13: G51 Scaling Edge of Tool Path: [1] Work coordinate origin, [2] Center of scaling.

<!-- image -->

```
% O60514 (G51 SCALING FROM EDGE OF TOOLPATH) ; (G54 X0 Y0 is at the bottom left of part) ; (Z0 is on top of the part) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 M08 (Activate tool offset 1) ; (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-0.1 F25. (Feed to cutting depth) ; M98 P60511 (Cuts shape without scaling) ; G00 Z0.1 (Rapid Retract) ; G00 X1. Y1. (Rapid to new scale position) ; G01 Z-.1 F25. (Feed to cutting depth) ; G51 X1. Y1. P2. (2x scale from edge of toolpath) ; M98 P60511 (run subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09(Rapid retract, Coolant off) ; G50 (CANCELS G51); G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ;
```

```
% 1 2
```

Tool offsets and cutter compensation values are not affected by scaling.

For canned cycles, G51 scales the initial point, depth, and return plane relative to the center of scaling.

To retain the functionality of canned cycles, G51 does not scale these:

- In G73 and G83:
- Peck depth ( Q )
- Depth of first peck ( I )
- Amount to reduce peck depth per pass ( J )
- Minimum peck depth ( K )
- In G76 and G77:
- The shift value ( Q )

The control rounds the final results of scaling to the lowest fractional value of the variable being scaled.

## 7.1.23 G52 Set Work Coordinate System (Group 00 or 12)

G52 works differently depending on the value of Setting 33. Setting 33 selects the Fanuc or Haas style of coordinates.

If FANUC is selected, G52 is a group 00 G-code. This is a global work coordinate shift. The values entered into the G52 line of the work offset page are added to all work offsets. All of the G52 values in the work offset page will be set to zero (0) when powered on, reset is pressed, changing modes, at the end of the program, by an M30 , G92 or a G52 X0 Y0 Z0 A0 B0 . When using a G92 (Set Work Coordinate Systems Shift Value), in Fanuc format, the current position in the current work coordinate system is shifted by the values of G92 ( X , Y , Z , A , and B ). The values of the G92 work offset are the difference between the current work offset and the shifted amount commanded by G92 .

If HAAS is selected, G52 is a group 00 G-code. This is a global work coordinate shift. The values entered into the G52 line of the work offset page are added to all work offsets. All of the G52 values will be set to zero (0) by a G92 . When using a G92 (Set Work Coordinate Systems Shift Value), in Haas format, the current position in the current work coordinate system is shifted by the values of G92 ( X , Y , Z , A , and B ). The values of the G92 work offset are the difference between the current work offset and the shifted amount commanded by G92 (Set Work Coordinate Systems Shift Value).

## 7.1.24 G53 Non-Modal Machine Coordinate Selection (Group 00)

This code temporarily cancels work coordinate offsets and uses the machine coordinate system. This code will also ignore tool offsets. In the machine coordinate system, the zero point  for  each  axis  is  the  position  where  the  machine  goes  when  a  Zero  Return  is performed. G53 will revert to this system for the block in which it is commanded.

## 7.1.25 G54-G59 Select Work Coordinate System #1 - #6 (Group 12)

These codes select one of more than six user coordinate systems. All future references to axes positions will be interpreted using the new ( G54 G59 ) coordinate system. See also 407 for additional work offsets.

## 7.1.26 G60 Uni-Directional Positioning (Group 00)

This G code is used to provide positioning only from the positive direction. It is provided only for compatibility with older systems. It is non-modal, so does not affect the blocks that follow it. Also refer to Setting 35.

## 7.1.27 G61 Exact Stop Mode (Group 15)

The G61 code is used to specify an exact stop. It is modal; therefore, it affects the blocks that follow it. The machine axes will come to an exact stop at the end of each commanded move.

## 7.1.28 G64 Cancels Exact Stop Mode (Group 15)

G64 code cancels exact stop ( G61 ).

## 7.1.29 G65 Macro Subprogram Call Option (Group 00)

G65 is the command that calls a subprogram with the ability to pass arguments to it. The format follows:

```
G65 Pnnnnn [Lnnnn] [arguments] ;
```

Arguments italicized in square  brackets  are optional. See  the Programming section  for more details on macro arguments.

The G65 command requires a P address corresponding to a program number currently located in the control's drive or path to a program. When the L address is used the macro call is repeated the specified number of times.

When a subprogram is called, the control looks for the subprogram on the active drive or the path to the program. If the subprogram cannot be located on the active drive, the control looks in the drive designated by Setting 251. Refer to the Setting Up Search Locations section for more information on subprogram searching. An alarm occurs if the control does not find the subprogram.

In  Example  1,  subprogram  1000  is  called  once  without  conditions  passed  to  the subprogram. G65 calls are similar to, but not the same as, M98 calls. G65 calls can be nested up to 9 times, which means, program 1 can call program 2, program 2 can call program 3 and program 3 can call program 4.

<!-- image -->

## NOTE:

<!-- image -->

## NOTE:

If an M-code is placed on the same line as a G65 it must go after G65. For  example: M14  G65  P1000 will  generate Alarm 339 Multiple codes while G65 P1000 M14 will work.

## Example 1:

```
% G65 P1000 (Call subprogram O01000 as a macro) ; M30 (Program stop) ; O01000 (Macro Subprogram) ; ... M99 (Return from Macro Subprogram) ; %
```

In Example 2, the program LightHousing.nc is called using the path that it is in.

## Example 2:

```
% G65 P15 A1. B1.; G65 (/Memory/LightHousing.nc) A1. B1.;
```

Paths are case sensitive.

<!-- image -->

NOTE:

In Example 3, subprogram 9010 is designed to drill a sequence of holes along a line whose slope is determined by the X and Y arguments that are passed to it in the G65 command line. The Z drill depth is passed as Z , the feed rate is passed as F , and the number of holes to be drilled is passed as T . The line of holes is drilled starting from the current tool position when the macro subprogram is called.

## Example 3:

The subprogram program O09010 should reside on the active drive or on a drive designated by Setting 252.

```
% G00 G90 X1.0 Y1.0 Z.05 S1000 M03 (Position tool) ;
```

```
G65 P9010 X.5 Y.25 Z.05 F10. T10 (Call O09010) ; M30 ; O09010 (Diagonal hole pattern) ; F#9 (F=Feedrate) ; WHILE [#20 GT 0] DO1 (Repeat T times) ; G91 G81 Z#26 (Drill To Z depth) ; #20=#20-1 (Decrement counter) ; IF [#20 EQ 0] GOTO5 (All holes drilled) ; G00 X#24 Y#25 (Move along slope) ; N5 END1 ; M99 (Return to caller) ; %
```

## 7.1.30 G66 Modal Macro Subprogram Call Option / G67 Modal Macro Subprogram Call Cancel(Group 00)

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

```
Example 1: % G66 P9010 a b d f r;M30 (Program stop) ; XY (Call O09010); XY (Call O09010);
```

```
XY (Call O09010); XY (Call O09010); %
```

Paths are case sensitive. In Example 2, In this example O01066 is the Main Program which makes use of a G66 P1067 call, which calls up subprogram O01067 which is embedded in this same script example.

```
O01066 (G81 TO G66 DRILL CYCLE); (G66 AVAILABLE IN NGC SW 100.23.000.1201); M06 T1 (DRILL); M03 S1500; G54 G00 G90 X1. Y-1.5 (HOLE 1 XY); G54 G00 G90 X1. Y-1.5 (HOLE 1 XY); G54 G00 G90 X1. Y-1.5 (HOLE 1 XY); G43 H01 Z0.1; / G66 P1067 Z-2.25 R0.1 F15. I0.125 J1. (MODAL MACRO CALL); X2. (HOLE 2); X3. (HOLE 3); G67 (MODAL MACRO OFF); G00 Z2.; G00 Z2.; M30; (G66: Modal Macro Call); Z = #26 = Drill Cycle Maximum Depth); (R = #18 = Clearance Plane); (F = #9  = Feedrate); (I = #4  = Extrusion Wall Thickness); (J = #5  = Extrusion Height); O01067(G66 SUBPROGRAM, DRILL-RAPID-DRILL); (NOTE THAT A / BLOCKS LOOKAHEAD, MAKES LOCAL VARIABLES EASIER TO SEE ON MACRO PAGE); / G01 G91 Z - [ 0.2 + #4 ] F#9; / G00 G90 Z - [ #5 - #4 - 0.1 ]; / G01 G90 Z - [ #5 + 0.1 ]; / G00 G90 Z#18; (COPY LOCAL VAR. TO GLOBAL VAR.) (JUST FOR TROUBLESHOOTING) #100= #9 (F); #101= #18 (R); #102= #26 (Z); #103= #4 (I); #104= #5 (J); M99 (RETURN TO MAIN PROGRAM); (G66: Modal Macro Call); (Z = #26 = Drill Cycle Maximum Depth); (R = #18 = Clearance Plane);
```

```
(F = #9  = Feedrate); (I = #4  = Extrusion Wall Thickness); (J = #5  = Extrusion Height); %
```

## F7.14: In the above example J is the height of the extrusion, I is the wall thickness of the extrusion, and H is the height of the clearance plane.

<!-- image -->

## 7.1.31 G68 Rotation (Group 16)

<!-- image -->

## NOTE:

You  must  purchase  the  Rotation  and  Scaling  option  to  use  this G-code. A 200-hour option tryout is also available; refer to page 238 for instructions.

* G17, G18, G19 - Plane of rotation, default is current * X/Y, X/Z, Y/Z - Center of rotation coordinates on the selected plane** * R - Angle of rotation, in degrees. Three-place decimal, -360.000 to 360.000.

*indicates optional

**The axis designation you use for these address codes corresponds to the axes of the current plane. For example, in the G17 (XY plane), you would use X and Y to specify the center of rotation.

When you command a G68 , the control rotates all X , Y , Z , I , J , and K values about a center of rotation to a specified angle ( R ),.

You can designate a plane with G17 , G18 , or G19 before G68 to establish the axis plane to rotate. For example:

```
G17 G68 Xnnn Ynnn Rnnn ;
```

If you do not designate a plane in the G68 block, the control uses the currently active plane.

The  control  always  uses  a  center  of  rotation  to  determine  the  positional  values  after rotation. If you do not specify a center of rotation, the control uses the current location.

G68 affects all appropriate positional values in the blocks after the G68 command. Values in the line that contains the G68 command are not rotated. Only the values in the plane of rotation are rotated; therefore, if G17 is the current plane of rotation, the command affects only the X and Y values.

A positive number (angle) in the R address rotates the feature counterclockwise.

If you do not specify the angle of rotation ( R ), then the control uses the value in Setting 72.

In G91 mode (incremental) with Setting 73 ON , the rotation angle changes by the value in R . In other words, each G68 command changes the rotation angle by the value specified in R .

The rotational angle is set to zero at the beginning of the program, or you can set it to a specific angle with G68 in G90 mode.

These examples illustrate rotation with G68 .  The first program defines a Gothic window shape to cut. The rest of the programs use this program as a subprogram.

## F7.15: G68 Start Gothic Window, No rotation: [1] Work coordinate origin.

<!-- image -->

```
% O60681 (GOTHIC WINDOW SUBPROGRAM) ; F50. S15000 (SET FEED AND SPINDLE SPEED) ; G00 X1. Y1. Z0.1(RAPID TO LOWER-LEFT WINDOW CORNER) ; Z-.005; G01 X2. (BOTTOM OF WINDOW) ; Y2. (RIGHT SIDE OF WINDOW); G03 X1. R0.5 (TOP OF WINDOW) ; G01 Y1. (FINISH WINDOW) ;
```

```
Z0.1 (RETRACT Z BEFORE GOING TO THE NEXT WINDOW); M99; %
```

The first example illustrates how the control uses the current work coordinate location as a rotation center ( X0 Y0 Z0 ).

## F7.16: G68 Rotation Current Work Coordinate: [1] Work coordinate origin and center of rotation.

<!-- image -->

```
% O60682 (ROTATE ABOUT WORK COORDINATE) ; G59 (OFFSET) ; G00 G90 X0 Y0 Z0.1 (WORK COORDINATE ORIGIN) ; M98 P60681 (CALL SUBPROGRAM) ; G90 G00 X0 Y0 (LAST COMMANDED POSITION) ; G68 R60. (ROTATE 60 DEGREES) ; M98 P60681 (CALL SUBPROGRAM) ; G69 G90 X0 Y0 (CANCEL G68) ; M30; %
```

The next example specifies the center of the window as the rotation center.

## F7.17: G68 Rotation Center of Window: [1] Work coordinate origin, [2] Center of rotation.

<!-- image -->

```
% O60683 (ROTATE ABOUT CENTER OF WINDOW) ; G59 (OFFSET) ; G00 G90 X0 Y0 Z0.1 (WORK COORDINATE ORIGIN) ; G68 X1.5 Y1.5 R60. ; (ROTATE SHAPE 60 DEGREES ABOUT CENTER) ; M98 P60681 (CALL SUBPROGRAM) ; G69 G90 G00 X0 Y0 (CANCEL G68, LAST COMMANDED POSITION) ; M30 ; %
```

This next example shows how the G91 mode can be used to rotate patterns about a center. This is often useful for making parts that are symmetric about a given point.

## F7.18: G68 Rotate Patterns About Center: [1] Work coordinate origin and center of rotation.

<!-- image -->

```
% O60684 (ROTATE PATTERN ABOUT CENTER) ; G59 (OFFSET) ; G00 G90 X0 Y0 Z0.1 (WORK COORDINATE ORIGIN) ; M97 P1000 L6 (CALL LOCAL SUBPROGRAM, LOOP 6 TIMES) ; M30 (END AFTER SUBPROGRAM LOOP) ; N1000 (BEGIN LOCAL SUBPROGRAM) ; G91 G68 R60. (ROTATE 60 DEGREES) ; G90 M98 P60681 (CALL WINDOW SUBPROGRAM) ; G90 G00 X0 Y0 (LAST COMMANDED POSITION) ; M99; %
```

Do not change the plane of rotation while G68 is in effect.

## Rotation with Scaling:

If you use scaling and rotation at the same time, you should turn on scaling before rotation, and use separate blocks. Use this template:

```
% G51 ... (SCALING) ; ... ; G68 ... (ROTATION) ; ... program ; G69 ... (ROTATION OFF) ; ... ; G50 ... (SCALING OFF) ; %
```

## Rotation with Cutter Compensation:

Turn on cutter compensation after the rotation command. Turn off cutter compensation before you turn off rotation.

## 7.1.32 G69 Cancel Rotation (Group 16)

(This G-code is optional and requires Rotation and Scaling.)

G69 cancels rotation mode.

## 7.1.33 G70 Bolt Hole Circle (Group 00)

- I - Radius
* J - Starting angle (0 to 360.0 degrees CCW from horizontal; or 3 o'clock position)
- L - Number of holes evenly spaced around the circle

*indicates optional

This non-modal G code must be used with one of the canned cycles G73 , G74 , G76 , G77 , or G81 - G89 . A canned cycle must be active so that at each position, a drill or tap function is performed. See also G-code Canned Cycles section.

```
% O60701 (G70 BOLT HOLE CIRCLE) ; (G54 X0 Y0 is center of the circle ) ; (Z0 is on the top of the part) ; (T1 is a drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ;
```

```
G81 G98 Z-1. R0.1 F15. L0 (Begin G81) ; (L0 skip drilling X0 Y0 position) ; G70 I5. J15. L12 (Begin G70) ; (Drills 12 holes on a 10.0 in. diameter circle) ; G80 (Canned Cycles off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home and Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.1.34 G71 Bolt Hole Arc (Group 00)

- I - Radius * J - Starting angle (degrees CCW from horizontal) K - Angular spacing of holes (+ or -) L - Number of holes

*indicates optional

This non-modal G code is similar to G70 except that it is not limited to a complete circle. G71 belongs to Group 00 and thus is non-modal. A canned cycle must be active so that at each position, a drill or tap function is performed.

## 7.1.35 G72 Bolt Holes Along an Angle (Group 00)

- I - Distance between holes
* J - Angle of line (degrees CCW from horizontal)
- L - Number of holes

*indicates optional

This non-modal G code drills L number of holes in a straight line at the specified angle. It operates similarly to G70 . For a G72 to work correctly, a canned cycle must be active so that at each position, a drill or tap function is performed.

F7.19: G70 , G71 , and G72 Bolt Holes: [I] Radius of bolt circle (G70, G71), or distance between holes (G72), [J] Starting angle from the 3 o'clock position, [K] Angular spacing between holes, [L] Number of holes.

<!-- image -->

## 7.1.36 G73 High-Speed Peck Drilling Canned Cycle (Group 09)

- F - Feedrate
* I - First peck depth
* J - Amount to reduce pecking depth for pass
* K - Minimum peck depth (The control calculates the number of pecks)
* L - Number of loops (Number of holes to drill) if G91 (Incremental Mode) is used
* P - Pause at the bottom of the hole (in seconds)
* Q - Peck Depth (always incremental)
* R - Position of the R plane (Distance above part surface)
* X - X-Axis location of hole
* Y - Y-Axis location of hole
- Z - Position of the Z-Axis at the bottom of hole
* indicates optional

The P values are modal. This means if you are in the middle of a canned cycle and a G04 Pnn or an M97 Pnn is used the P value will be used for the dwell / subprogram as well as the canned cycle.

<!-- image -->

NOTE:

F7.20: G73 Peck Drilling. Left: Using I , J , and K Addresses. Right: Using Only the Q Address. [#22] Setting 22.

<!-- image -->

I , J , K , and Q are always positive numbers.

There are three methods to program a G73 : using the I , J , K addresses, using the K and Q addresses, and using only a Q address.

If I , J , and K are specified, The first pass will cut in by the value I , each succeeding cut will be reduced by the value of J , and the minimum cutting depth is K . If P is specified, the tool will pause at the bottom of the hole for that amount of time.

If K and Q are both specified, a different operating mode is selected for this canned cycle. In this mode, the tool is returned to the R plane after the number of passes totals up to the K amount.

If only Q is specified, a different operating mode is selected for this canned cycle. In this mode, the tool is returned to the R plane after all pecks are completed, and all pecks will be equal to the Q value.

## F7.21: G73 Peck Drilling Canned Cycles using the K and Q Addresses: [#22] Setting 22.

<!-- image -->

## 7.1.37 G74 Reverse Tap Canned Cycle (Group 09)

- F - Feedrate. Use the formula described in the canned cycle introduction to calculate feedrate and spindle speed.
* J - Retract Multiple (How fast to retract - see Setting 130)
* L - Number of loops (How many holes to tap) if G91 (Incremental Mode) is used
* R - Position of the R plane (position above the part) where tapping starts
* X - X-Axis location of hole
* Y - Y-Axis location of hole
* Q - Peck Depth (always incremental)
- Z - Position of the Z-Axis at the bottom of hole

*indicates optional

## F7.22: G74 Tapping Canned Cycle

<!-- image -->

## 7.1.38 G76 Fine Boring Canned Cycle (Group 09)

- F - Feedrate
* I - Shift value along the X-Axis before retracting, if Q is not specified
* J - Shift value along the Y-Axis before retracting, if Q is not specified
* L - Number of holes to bore if G91 (Incremental Mode) is used
* P - The dwell time at the bottom of the hole
* Q - The shift value, always incremental
* R - Position of the R plane (position above the part)
* X - X-Axis location of hole
* Y - Y-Axis location of hole
- Z - Position of the Z-Axis at the bottom of hole
* indicates optional

<!-- image -->

NOTE:

<!-- image -->

CAUTION:

The P values are modal. This means if you are in the middle of a canned cycle and a G04 Pnn or an M97 Pnn is used the P value will be used for the dwell / subprogram as well as the canned cycle.

Unless  you  specify  otherwise,  this  canned  cycle  uses  the  most recently  commanded  spindle  direction  ( M03 , M04 ,  or M05 ).  If  the program did not specify a spindle direction before it commands this canned cycle, the default is M03 (clockwise). If you command M05 , the canned  cycle  will  run  as  a  'no-spin'  cycle.  This  lets  you  run applications with self-driven tools, but it can also cause a crash. Be sure  of  the  spindle  direction  command  when  you  use  this  canned cycle.

## F7.23: G76 Fine Boring Canned Cycles

<!-- image -->

In addition to boring the hole, this cycle will shift the X and/or Y Axis prior to retracting in order to clear the tool while exiting the part. If Q is used Setting 27 determines the shift direction. If Q is not specified, the optional I and J values are used to determine the shift direction and distance.

## 7.1.39 G77 Back Bore Canned Cycle (Group 09)

- F - Feedrate
* I - Shift value along the X Axis before retracting, if Q is not specified
* J - Shift value along the Y Axis before retracting, if Q is not specified
* L - Number of holes to bore if G91 (Incremental Mode) is used
* Q - The shift value, always incremental
* R - Position of the R plane
* X - X-Axis location of hole
* Y - Y-Axis location of hole
- Z - Z-Axis position to cut to
* indicates optional

Unless  you  specify  otherwise,  this  canned  cycle  uses  the  most recently  commanded  spindle  direction  ( M03 , M04 ,  or M05 ).  If  the program did not specify a spindle direction before it commands this canned cycle, the default is M03 (clockwise). If you command M05 , the canned  cycle  will  run  as  a  'no-spin'  cycle.  This  lets  you  run applications with self-driven tools, but it can also cause a crash. Be sure  of  the  spindle  direction  command  when  you  use  this  canned cycle.

<!-- image -->

## CAUTION:

In addition to boring the hole, this cycle shifts the X and Y Axis before and after the cut, to clear the tool while it enters and exits the workpiece (refer to G76 for an example of a shift move). Setting 27 defines the shift direction. If you do not specify a Q value, the control uses the optional I and J values to determine the shift direction and distance.

F7.24: G77 Back Boring Canned Cycle Example

<!-- image -->

Program Example

```
% O60077 (G77 CYCLE-WORKPIECE IS 1.0" THICK) ; T5 M06 (BACK COUNTERBORE TOOL) ; G90 G54 G00 X0 Y0 (INITIAL POSITION) ; S1200 M03 (SPINDLE START) ; G43 H05 Z.1 (TOOL LENGTH COMPENSATION) ; G77 Z-1. R-1.6 Q0.1 F10. (1ST HOLE) ; X-2. (2ND HOLE) ; G80 G00 Z.1 M09 (CANCEL CANNED CYCLE) ; G28 G91 Z0. M05 ; M30 ; %
```

## F7.25: G77 Approximate Toolpath Example. This example shows the entrance motion only. Dimensions are not to scale.

<!-- image -->

<!-- image -->

NOTE:

For this example, the 'top' of the workpiece is the surface defined as Z0. in the current work offset. The 'bottom' of the workpiece is the opposite surface.

In this example, when the tool reaches the R depth, it then moves 0.1" in X (the Q value and Setting 27 define this movement; in this example, Setting 27 is X+ ). The tool then feeds to the Z value at the given feedrate. When the cut is finished, the tool shifts back toward the center of the hole and retracts out of it. The cycle repeats at the next commanded position until the G80 command.

<!-- image -->

## NOTE:

<!-- image -->

NOTE:

The R value is negative, and it must go past the bottom of the part for clearance.

The Z value is commanded from the active Z work offset.

<!-- image -->

NOTE:

You do not need to command an initial point return ( G98 ) after a G77 cycle; the control assumes this automatically.

## 7.1.40 G80 Canned Cycle Cancel (Group 09)

G80 cancels all active canned cycles.

<!-- image -->

## NOTE:

G00 or G01 also cancel canned cycles.

## 7.1.41 G81 Drill Canned Cycle (Group 09)

* E - Chip-clean RPM (Spindle reverses to remove chips after each cycle)
- F - Feedrate
* L - Number of holes to drill if G91 (Incremental Mode) is used
* R - Position of the R plane (position above the part)
* X - X-Axis motion command
* Y - Y-Axis motion command
- Z - Position of the Z Axis at the bottom of hole

* indicates optional

Unless  you  specify  otherwise,  this  canned  cycle  uses  the  most recently  commanded  spindle  direction  ( M03 , M04 ,  or M05 ).  If  the program did not specify a spindle direction before it commands this canned cycle, the default is M03 (clockwise). If you command M05 , the canned  cycle  will  run  as  a  'no-spin'  cycle.  This  lets  you  run applications with self-driven tools, but it can also cause a crash. Be sure  of  the  spindle  direction  command  when  you  use  this  canned cycle.

<!-- image -->

## CAUTION:

## F7.26: G81 Drill Canned Cycle

<!-- image -->

This is a program to drill through an aluminum plate:

```
% O60811 (G81 DRILLING CANNED CYCLE) ; (G54 X0 Y0 is at the top-left of part) ; (Z0 is on top of the part) ; (T1 is a .5 in drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y-2. (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G81 Z-0.720 R0.1 F15.(Begin G81) ; (Drill 1st hole at current X Y location) ; X2. Y-4. (2nd hole) ; X4. Y-4. (3rd hole) ; X4. Y-2. (4th hole) ; (BEGIN COMPLETION BLOCKS) ; G00 G90 Z1. M09 (Rapid retract,coolant off) ; G53 G49 Z0 M05 (Z home, spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.1.42 G82 Spot Drill Canned Cycle (Group 09)

* E - Chip-clean RPM (Spindle reverses to remove chips after each cycle)
- F - Feedrate
* L - Number of holes if G91 (Incremental Mode) is used.
* P - The dwell time at the bottom of the hole
* R - Position of the R plane (position above the part)
* X - X-Axis location of hole
* Y - Y-Axis location of hole
- Z - Position of bottom of hole
* indicates optional

The P values are modal. This means if you are in the middle of a canned cycle and a G04 Pnn or an M97 Pnn is used the P value will be used for the dwell / subprogram as well as the canned cycle.

Unless  you  specify  otherwise,  this  canned  cycle  uses  the  most recently  commanded  spindle  direction  ( M03 , M04 ,  or M05 ).  If  the program did not specify a spindle direction before it commands this canned cycle, the default is M03 (clockwise). If you command M05 , the canned  cycle  will  run  as  a  'no-spin'  cycle.  This  lets  you  run applications with self-driven tools, but it can also cause a crash. Be sure  of  the  spindle  direction  command  when  you  use  this  canned cycle.

G82 is similar to G81 except that there is the option to program a dwell ( P ).

```
% O60821 (G82 SPOT DRILLING CANNED CYCLE) ; (G54 X0 Y0 is at the top-left of part) ; (Z0 is on top of the part) ; (T1 is a 0.5 in 90 degree spot drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y-2. (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ;
```

<!-- image -->

## NOTE:

<!-- image -->

CAUTION:

<!-- image -->

NOTE:

```
M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G82 Z-0.720 P0.3 R0.1 F15.(Begin G82) ; (Drill 1st hole at current X Y location) ; X2. Y-4. (2nd hole) ; X4. Y-4. (3rd hole) ; X4. Y-2. (4th hole) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## F7.27: G82 Spot Drilling Example

<!-- image -->

## 7.1.43 G83 Normal Peck Drilling Canned Cycle (Group 09)

* E - Chip-clean RPM (Spindle reverses to remove chips after each cycle)
- F - Feedrate
* I - Size of first peck depth
* J - Amount to reduce peck depth each pass
* K - Minimum depth of peck
* L - Number of holes if G91 (Incremental Mode) is used, also G81 through G89.
* P - Pause at end of last peck, in seconds (Dwell)
* Q - Peck depth, always incremental
* R - Position of the R plane (position above the part)
* X - X-Axis location of hole
* Y - Y-Axis location of hole
- Z - Position of the Z-Axis at the bottom of hole

* indicates optional

If I , J , and K are specified, the first pass will cut in by the amount of I, each succeeding cut will be reduced by amount J, and the minimum cutting depth is K . Do not use a Q value when programming with I , J , and K .

If P is specified, the tool will pause at the bottom of the hole for that amount of time. The following example will peck several times and dwell for 1.5 seconds:

<!-- formula-not-decoded -->

The same dwell time will apply to all subsequent blocks that do not specify a dwell time.

## F7.28: G83 Peck Drilling with I , J , K and Normal Peck Drilling: [#22] Setting 22.

<!-- image -->

Setting 52 changes the way G83 works when it returns to the R plane. Usually the R plane is set well above the cut to ensure that the peck motion allows the chips to get out of the hole. This wastes time as the drill starts by drilling empty space. If Setting 52 is set to the distance required to clear chips, you can set the R plane much closer to the part. When the chip-clearing move to R occurs, Setting 52 determines the Z-Axis distance above R.

## F7.29: G83 peck Drilling Canned Cycle with Setting 52 [#52]

<!-- image -->

```
% O60831 (G83 PECK DRILLING CANNED CYCLE) ; (G54 X0 Y0 is at the top-left of part) ; (Z0 is on top of the part) ; (T1 is a 0.3125 in. stub drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y-2. (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G83 Z-0.720 Q0.175 R0.1 F15.(Begin G83) ; (Drill 1st hole at current X Y location) ; X2. Y-4. (2nd hole) ; X4. Y-4. (3rd hole) ; X4. Y-2. (4th hole) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.1.44 G84 Tapping Canned Cycle (Group 09)

* E - Chip-clean RPM (Spindle reverses to remove chips after each cycle)

F - Feedrate

* J - Retract Multiple (Example: J2 retracts twice as fast as the cutting speed, also refer to Setting 130)
* L - Number of holes if G91 (Incremental Mode) is used
* R - Position of the R plane (Position above the part)
* X - X-Axis location of hole
* Y - Y-Axis location of hole
- Z - Position of the Z Axis at the bottom of hole
* Q - Peck Depth (always incremental)
* S - Spindle speed
* indicates optional

You do not need to command a spindle start (M03 / M04) before G84. The canned cycle starts and stops the spindle as needed.

NOTE:

<!-- image -->

## F7.30: G84 Tapping Canned Cycle

<!-- image -->

```
% O60841 (G84 TAPPING CANNED CYCLE) ; (G54 X0 Y0 is at the top-left of part) ; (Z0 is on top of the part) ; (T1 is a 3/8-16 tap) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y-2. (Rapid to 1st position) ; G43 H01 Z0.1 (Activate tool offset 1) ;
```

```
M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G84 Z-0.600 R0.1 F56.25 S900 (Begin G84) ; (900 rpm divided by 16 tpi = 56.25 ipm) ; (Drill 1st hole at current X Y location) ; X2. Y-4. (2nd hole) ; X4. Y-4. (3rd hole) ; X4. Y-2. (4th hole) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Canned cycle off, rapid retract) ; (Coolant off) ; G53 G49 Z0 (Z home) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.1.45 G85 Bore In, Bore Out Canned Cycle (Group 09)

- F - Feedrate
* L - Number of holes if G91 (Incremental Mode) is used
* R - Position of the R plane (position above the part)
* X - X-Axis location of holes
* Y - Y-Axis location of holes
- Z - Position of the Z Axis at the bottom of hole
* indicates optional

## F7.31: G85 Boring Canned Cycle

<!-- image -->

## 7.1.46 G86 Bore and Stop Canned Cycle (Group 09)

- F - Feedrate
* L - Number of holes if G91 (Incremental Mode) is used
* R - Position of the R plane (position above the part)
* X - X-Axis location of hole
* Y - Y-Axis location of hole
- Z - Position of the Z Axis at the bottom of hole
* indicates optional

Unless  you  specify  otherwise,  this  canned  cycle  uses  the  most recently  commanded  spindle  direction  ( M03 , M04 ,  or M05 ).  If  the program did not specify a spindle direction before it commands this canned cycle, the default is M03 (clockwise). If you command M05 , the canned  cycle  will  run  as  a  'no-spin'  cycle.  This  lets  you  run applications with self-driven tools, but it can also cause a crash. Be sure  of  the  spindle  direction  command  when  you  use  this  canned cycle.

CAUTION:

<!-- image -->

This G code will stop the spindle once the tool reaches the bottom of the hole. The tool is retracted once the spindle has stopped.

## F7.32: G86 Bore and Stop Canned Cycles

<!-- image -->

## 7.1.47 G89 Bore In, Dwell, Bore Out Canned Cycle (Group 09)

- F - Feedrate
- L - Number of holes if G91 (Incremental Mode) is used
- P - The dwell time at the bottom of the hole
* R - Position of the R plane (position above the part)
- X - X-Axis location of holes
- Y - Y-Axis location of holes
- Z - Position of the Z Axis at the bottom of hole
* indicates optional

The P values are modal. This means if you are in the middle of a canned cycle and a G04 Pnn or an M97 Pnn is used the P value will be used for the dwell / subprogram as well as the canned cycle.

Unless  you  specify  otherwise,  this  canned  cycle  uses  the  most recently  commanded  spindle  direction  ( M03 , M04 ,  or M05 ).  If  the program did not specify a spindle direction before it commands this canned cycle, the default is M03 (clockwise). If you command M05 , the canned  cycle  will  run  as  a  'no-spin'  cycle.  This  lets  you  run applications with self-driven tools, but it can also cause a crash. Be sure  of  the  spindle  direction  command  when  you  use  this  canned cycle.

NOTE:

<!-- image -->

<!-- image -->

## CAUTION:

## F7.33: G89 Bore and Dwell and Canned Cycle

<!-- image -->

## 7.1.48 G90 Absolute / G91 Incremental Position Commands (Group 03)

These G codes  change the  way the axis  commands are interpreted. Axes  commands following a G90 will move the axes to the machine coordinate. Axes commands following a G91 will move the axis that distance from the current point. G91 is not compatible with G143 (5-Axis Tool Length Compensation).

The  Basic  Programming  section  of  this  manual,  beginning  on  page 205 ,  includes  a discussion of absolute versus incremental programming.

## 7.1.49 G92 Set Work Coordinate Systems Shift Value (Group 00)

This G-code does not move any of the axes; it only changes the values stored as user work offsets. G92 works differently depending on Setting 33, which selects a FANUC or HAAS coordinate system.

## FANUC or HAAS

If Setting 33 is set to FANUC or HAAS , a G92 command shifts all work coordinate systems ( G54 - G59 , G110 - G129 ) so that the commanded position becomes the current position in the active work system. G92 is non-modal.

A G92 command cancels any G52 in effect for the commanded axes. Example: G92 X1.4 cancels the G52 for the X-Axis. The other axes are not affected.

The G92 shift value is displayed at the bottom of the Work Offsets page and may be cleared there if necessary. It is also cleared automatically after power-up, and any time [ZERO RETURN] and [ALL] or [ZERO RETURN] and [SINGLE] are used.

## G92 Clear Shift Value From Within a Program

G92 shifts may be canceled by programming another G92 shift to change the current work offset back to the original value.

```
% O60921 (G92 SHIFT WORK OFFSETS) ; (G54 X0 Y0 Z0 is at the center of mill travel) ; G00 G90 G54 X0 Y0 (Rapid to G54 origin) ; G92 X2. Y2. (Shifts current G54) ; G00 G90 G54 X0 Y0 (Rapid to G54 origin) ; G92 X-2. Y-2. (Shifts current G54 back to original) ; G00 G90 G54 X0 Y0 (Rapid to G54 origin) ; M30 (End program) ; %
```

## 7.1.50 G93 Inverse Time Feed Mode (Group 05)

F - Feed Rate (strokes per minute)

This G code specifies that all F (feedrate) values are interpreted as strokes per minute. In other words the time (in seconds) to complete the programmed motion using G93 is, 60 (seconds) divided by the F value.

G93 is generally used in 4 and 5-axis work when the program is generated using a CAM system. G93 is a way of translating the linear (inches/min) feedrate into a value that takes rotary motion into account. When G93 is used, the F value will tell you how many times per minute the stroke (tool move) can be repeated.

When G93 is used, feedrate ( F ) is mandatory for all interpolated motion blocks. Therefore each non-rapid motion block must have its own feedrate ( F ) specification.

Pressing [RESET] will  set  the  machine  to G94 (Feed  per  Minute) mode. Settings 34 and 79 (4th &amp; 5th axis diameter) are not necessary when using G93 .

<!-- image -->

## 7.1.51 G94 Feed Per Minute Mode (Group 05)

This code deactivates G93 (Inverse Time Feed Mode) and returns the control to Feed Per Minute mode.

## 7.1.52 G95 Feed per Revolution (Group 05)

When G95 is active, a spindle revolution will result in a travel distance specified by the Feed value. If Setting 9 is set to INCH , then the feed value F will be taken as inches/rev (set to MM , then the feed will be taken as mm/rev). Feed Override and Spindle Override will affect the behavior of the machine while G95 is active. When a Spindle Override is selected, any change in the spindle speed will result in a corresponding change in feed in order to keep the chip load uniform. However, if a Feed Override is selected, then any change in the Feed Override will only affect the feed rate and not the spindle.

## 7.1.53 G98 Canned Cycle Initial Point Return (Group 10)

Using G98 , the Z-Axis returns to its initial starting point (the Z position in the block before the canned cycle) between each X/Y position. This lets you program up and around areas of the part, clamps, and fixtures.

F7.34: G98 Initial Point Return. After the second hole, the Z Axis returns to the starting position [G98] to move over the toe clamp to the next hole position.

<!-- image -->

```
% O69899 (G98/G99 INITIAL POINT & R PLANE RETURN) ; (G54 X0 Y0 is top right corner of part) ; (Z0 is on top of the part) ; (T1 is a drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G17 G40 G49 G54 (Safe startup) ; G00 G54 X1. Y-0.5 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z2. (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G81 G99 X1. Z-0.5 F10. R0.1 (Begin G81 using G99) ; G98 X2. (2nd hole and then clear clamp with G98) ; X4. (Drill 3rd hole) ; (BEGIN COMPLETION BLOCKS) ; G00 Z2. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ;
```

```
G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.1.54 G99 Canned Cycle R Plane Return (Group 10)

Using G99 , the Z-Axis will stay at the R plane between each X and/or Y location. When obstructions are not in the path of the tool G99 saves machining time.

F7.35: G99 R Plane Return. After the first hole, the Z Axis returns to the R plane position [G99] and moves to the second hole position. This is a safe move in this case because there are no obstacles.

<!-- image -->

```
% O69899 (G98/G99 INITIAL POINT & R PLANE RETURN) ; (G54 X0 Y0 is top right corner of part) ; (Z0 is on top of the part) ; (T1 is a drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G17 G40 G49 G54 (Safe startup) ; G00 G54 X1. Y-0.5 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z2. (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G81 G99 X1. Z-0.5 F10. R0.1 (Begin G81 using G99) ; G98 X2. (2nd hole and then clear clamp with G98) ;
```

```
X4. (Drill 3rd hole) ; (BEGIN COMPLETION BLOCKS) ; G00 Z2. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.1.55 G100 Disable / G101 Enable Mirror Image (Group 00)

```
* X - X-Axis command * Y - Y-Axis command * Z - Z-Axis command * A - A-Axis command * B - B-Axis command * C - C-Axis command
```

* indicates optional

Programmable mirror imaging is used to turn on or off any of the axes. When one is ON , axis motion may be mirrored (or reversed) around the work zero point. These G codes should be used in a command block without any other G codes. They do not cause any Axis motion. The bottom of the screen indicates when an axis is mirrored. Also see Settings 45, 46, 47, 48, 80, and 250 for mirror imaging.

The format for turning Mirror Image on and off is:

```
G101 X0. (turns on mirror imaging for the X-Axis) ; G100 X0. (turns off mirror imaging for the X-Axis) ;
```

## F7.36: X-Y Mirror Image

<!-- image -->

## 7.1.56 G103 Limit Block Look-Ahead (Group 00)

G103 specifies the maximum number of blocks the control looks ahead (Range 0-15), for example:

<!-- formula-not-decoded -->

During machine motions, the control prepares future blocks (lines of code) ahead of time. This is commonly called 'Block Look-ahead.' While the control executes the current block, it has already interpreted and prepared the next block for continuous motion.

A program command of G103  P0 ,  or  simply G103 ,  disables  block  limiting.  A  program command of G103 Pn limits look-ahead to n blocks.

G103 is useful for debugging macro programs. The control interprets Macro expressions during look-ahead time. If you insert a G103 P1 into the program, the control interprets macro expressions (1) block ahead of the currently executing block.

When a G103 P1 is called, it is best to add several empty lines after a block with G-code if a block using macros follows that G-code block, to ensure that the macro statement is only  evaluated  after  the  previous  G-code  block  is  processed.  This  keeps  macros  from unintentionally being reassigned values before the G-code blocks are done (see example below), and also helps ensure that the value of macros used during conditional statements are the intended values.

Example:

<!-- image -->

## NOTE:

```
#12012 = 1; G04 P1. ; #12012 = 0;
```

This  is  intended  to  turn  an  output  on,  wait  1  second,  and  then  turn  it  off.  However, lookahead  causes  the  output  to  turn  on  then  immediately  back  off  while  the  control processes the dwell. G103 P1 is used to limit lookahead to 1 block. To make this example work properly, modify it as follows:

```
G103 P1; ; #12012=1; G04 P1.; ; ; ; #12012=0;
```

G103 affects cutter compensation and High Speed Machining.

The P values are modal. This means if you are in the middle of a canned cycle and a G04 Pnn or an M97 Pnn is used the P value will be used for the dwell / subprogram as well as the canned cycle.

## 7.1.57 G107 Cylindrical Mapping (Group 00)

* X - X-Axis command
* Y - Y-Axis command
* Z - Z-Axis command
* A - A-Axis command
* B - B-Axis command
- C - C-Axis command
* Q - Diameter of the cylindrical surface
* R - Radius of the rotary axis
* indicates optional

This G code translates all programmed motion occurring in a specified linear axis into the equivalent motion along the surface of a cylinder (as attached to a rotary axis) as shown in the following figure. It is a Group 0 G code, but its default operation is subject to Setting 56 ( M30 Restores Default G). The G107 command is used to either activate or deactivate cylindrical mapping.

- Any linear-axis program can be cylindrically mapped to any rotary axis (one at a time).

- An existing linear-axis G-code program can be cylindrically mapped by inserting a G107 command at the beginning of the program.
- The  radius  (or  diameter)  of  the  cylindrical  surface  can  be  redefined,  allowing cylindrical mapping to occur along surfaces of different diameters without having to change the program.
- The radius (or diameter) of the cylindrical surface can either be synchronized with or be independent of the rotary axis diameter(s) specified in the Settings 34 and 79 .
- G107 can  also  be  used  to  set  the  default  diameter  of  a  cylindrical  surface, independently of any cylindrical mapping that may be in effect.

## 7.1.58 G110-G129 Coordinate System #7-26 (Group 12)

These  codes  select  one  of  the  additional  work  coordinate  systems.  All  subsequent references to axis positions will be interpreted in the new coordinate system. Operation of G110 to G129 is the same as G54 to G59 .

## 7.1.59 G136 Automatic Work Offset Center Measurement (Group 00)

This G-code is optional and requires a probe. Use it to set work offsets to the center of a work piece with a work probe.

- F - Feedrate
* I - Optional offset distance along X-Axis
* J - Optional offset distance along Y-Axis
* K - Optional offset distance along Z-Axis
* X - Optional X-Axis motion command
* Y - Optional Y-Axis motion command
* Z - Optional Z-Axis motion command
* indicates optional

Automatic Work Offset Center Measurement ( G136 ) is used to command a spindle probe to set work offsets. A G136 will feed the axes of the machine in an effort to probe the work piece with a spindle mounted probe. The axis (axes) will move until a signal (skip signal) from  the  probe  is  received  or  the  end  of  the  programmed  move  is  reached.  Tool compensation ( G41 , G42 , G43 , or G44 ) must not be active when this function is performed. The currently active work coordinate system is set for each axis programmed. Use a G31 cycle with an M75 to set the first point. A G136 will set the work coordinates to a point at the center of a line between the probed point and the point set with an M75 . This allows the center of the part to be found using two separate probed points.

If an I , J , or K is specified, the appropriate axis work offset is shifted by the amount in the I , J , or K command. This allows the work offset to be shifted away from the measured center of the two probed points.

## Notes:

This code is non-modal and only applies to the block of code in which G136 is specified.

The points probed are offset by the values in Settings 59 through 62. See the Settings section of this manual for more information.

Do not use Cutter Compensation ( G41 , G42 ) with a G136 .

Do not use tool length Compensation ( G43 , G44 ) with G136

To avoid damaging the probe, use a feed rate below F100 . (inch) or F2500 . (metric).

Turn on the spindle probe before using G136 .

If your mill has the standard Renishaw probing system, use the following commands to turn on the spindle probe:

```
M59 P3 ;
```

Use the following commands to turn off the spindle probe:

M69 P3 ;

Also see M75 , M78 , and M79 .

Also see G31 .

This sample program measures the center of a part in the Y Axis and records the measured value to the G58 Y Axis work offset. To use this program, the G58 work offset location must be set at or close to the center of the part to be measured.

```
% O61361 (G136 AUTO WORK OFFSET - CENTER OF PART) ; (G58 X0 Y0 is at the center of part) ; (Z0 is on top of the part) ; (T1 is a spindle probe) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00  G58 X0. Y1. (Rapid to 1st position) ; (BEGIN PROBING BLOCKS) ; M59 P3 (Spindle probe on) ; Z-10. (Rapid spindle down to position) ; G91 G01 Z-1. F20. (Incremental feed by Z-1.) ; G31 Y-1. F10. M75 (Measure & record Y reference) ; G01 Y0.25 F20. (Feed away from surface) ; G00 Z2. (Rapid retract) ;
```

```
Y-2. (Move to opposite side of part) ; G01 Z-2. F20. (Feed by Z-2.) ; G136 Y1. F10. ; (Measure and record center in the Y axis) ; G01 Y-0.25 (Feed away from surface) ; G00 Z1. (Rapid retract) ; M69 P3 (Spindle probe off) ; (BEGIN COMPLETION BLOCKS) ; G00 G90 G53 Z0. (Rapid retract to Z home) ; M30 (End program) ; %
```

## 7.1.60 G141 3D+ Cutter Compensation (Group 07)

- X - X-Axis command
- Y - Y-Axis command
- Z - Z-Axis command
* A - A-Axis command (optional)
* B - B-Axis command (optional)
* D - Cutter Size Selection (modal)
- I - X-Axis cutter compensation direction from program path
- J - Y-Axis cutter compensation direction from program path
- K - Z-Axis cutter compensation direction from program path
- F - Feedrate
* indicates optional

This feature performs three-dimensional cutter compensation.

The form is:

```
G141 Xnnn Ynnn Znnn Innn Jnnn Knnn Fnnn Dnnn
```

## Subsequent lines can be:

```
G01 Xnnn Ynnn Znnn Innn Jnnn Knnn Fnnn ; Or G00 Xnnn Ynnn Znnn Innn Jnnn Knnn ;
```

Some CAM systems are able to output the X , Y , and Z with values for I , J , K . The I , J , and K values tell the control the direction in which to apply the compensation at the machine. Similar to other uses of I , J , and K , these are incremental distances from the X , Y , and Z point called.

The I , J , and K specify the normal direction, relative to the center of the tool, to the contact point of the tool in the CAM system. The I , J , and K vectors are required by the control to be able to shift the toolpath in the correct direction. The value of the compensation can be in a positive or negative direction.

The offset amount entered in radius or diameter (Setting 40) for the tool will compensate the path by this amount, even if the tool motions are 2 or 3 axes. Only G00 and G01 can use G141 . A Dnn will have to be programmed; the D-code selects which tool wear diameter offset to use. A feedrate must be programmed on each line if in G93 Inverse Time Feed mode.

With a unit vector, the length of the vector line must always equal 1. In the same way that a unit circle in mathematics is a circle with a radius of 1, a unit vector is a line that indicates a direction with a length of 1. Remember, the vector line does not tell the control how far to move the tool when a wear value is entered, just the direction in which to go.

Only the endpoint of the commanded block is compensated in the direction of I , J , and K . For this reason, this compensation is recommended only for surface toolpaths having a tight  tolerance  (small  motion  between  blocks  of  code). G141 compensation  does  not prohibit  the  toolpath  from  crossing  over  itself  when  excessive  cutter  compensation  is entered. The tool will be offset, in the direction of the vector line, by the combined values of the tool offset geometry plus the tool offset wear. If compensation values are in diameter mode (Setting 40), the move will be half the amount entered in these fields.

For best results, program from the tool center using a ball nose endmill.

```
% O61411 (G141 3D CUTTER COMPENSATION) ; (G54 X0 Y0 is at the bottom-left) ; (Z0 is on top of the part) ; (T1 is a ball nose endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 Z0 A0 B0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G141 D01 X0. Y0. Z0. ; (Rapid to position with 3D+ cutter comp) ; G01 G93 X.01 Y.01 Z.01 I.1 J.2 K.9747 F300. ; (Inverse time feed on, 1st linear motion) ;
```

```
N1 X.02 Y.03 Z.04 I.15 J.25 K.9566 F300. (2nd motion) ; X.02 Y.055 Z.064 I.2 J.3 K.9327 F300. (3rd motion) ; X2.345 Y.1234 Z-1.234 I.25 J.35 K.9028 F200. ; (Last motion) ; (BEGIN COMPLETION BLOCKS) ; G94 F50. (Inverse time feed off) ; G00 G90 G40 Z0.1 M09 (Cutter comp off) ; (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

In the above example, we can see where the I , J ,  and K were derived by plugging the points into the following formula:

AB = [(x 2 -x 1 ) 2  + (y 2 -y 1 ) 2  + (z 2 -z 1 ) 2 ], a 3D version of the distance formula. Looking at line N1 , we use 0.15 for x 2 , 0.25 for y 2 , and 0.9566 for Z 2 . Because I , J , and K are incremental, we will use 0 for x 1 , y 1 , and z 1 .

- F7.37: Unit Vector Example: The commanded line endpoint [1] is compensated in the direction of the vector line [2](I,J,K), by the amount of the Tool Offset Wear.

0

<!-- image -->

```
% AB=[(.15) 2  + (.25) 2  + (.9566) 2 ] AB=[.0225 + .0625 + .9150] AB=1 %
```

## A simplified example is listed below:

```
% O61412 (G141 SIMPLE 3D CUTTER COMPENSATION) ; (G54 X0 Y0 is at the bottom-left) ; (Z0 is on top of the part) ; (T1 is a ball nose endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G141 D01 X0. Y0. Z0. ; (Rapid to position with 3D+ cutter compensation) ; N1 G01 G93 X5. Y0. I0. J-1. K0. F300. ; (Inverse time feed on & linear motion) ; (BEGIN COMPLETION BLOCKS) ; G94 F50. (Inverse time feed off) ; G00 G90 G40 Z0.1 M09 (Cutter compensation off) ; (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

In this case, the wear value (DIA) for T01 is set to -.02. Line N1 moves the tool from ( X0. , Y0. , Z0. ) to ( X5. , Y0., Z0. ). The J value tells the control to compensate the endpoint of the programmed line only in the Y Axis.

Line N1 could have been written using only the J-1 . (not using I0 . or K0 .), but a Y value must be entered if a compensation is to be made in this axis ( J value used).

## 7.1.61 G143 5-Axis Tool Length Compensation + (Group 08)

(This G-code is optional; it only applies to machines on which all rotary motion is movement of the cutting tool, such as VR-series mills)

This G code allows the user to correct for variations in the length of cutting tools without the need for a CAD/CAM processor. An H code is required to select the tool length from the existing  length  compensation  tables.  A G49 or H00 command  will  cancel  5-axis compensation. For G143 to work correctly there must be two rotary axes, A and B. G90 , absolute positioning mode must be active ( G91 cannot be used). Work position 0,0 for the A and B axes must be so the tool is parallel with Z-Axis motion.

The intention behind G143 is to compensate for the difference in tool length between the originally posted tool and a substitute tool. Using G143 allows the program to run without having to repost a new tool length.

G143 tool length compensation works only with rapid ( G00 ) and linear feed ( G01 ) motions; no other feed functions ( G02 or G03 ) or canned cycles (drilling, tapping, etc.) can be used. For a positive tool length, the Z-Axis would move upward (in the + direction). If one of X, Y or Z is not programmed, there will be no motion of that axis, even if the motion of A or B produces a new tool length vector. Thus a typical program would use all 5 axes on one block of data. G143 may effect commanded motion of all axes in order to compensate for the A and B axes.

Inverse feed mode ( G93 ) is recommended, when using G143 .

```
% O61431 (G143 5-AXIS TOOL LENGTH) ; (G54 X0 Y0 is at the top-right) ; (Z0 is on top of the part) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y0 Z0 A0 B0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G143 H01 X0. Y0. Z0. A-20. B-20. ; (Rapid to position w/ 5 Axis tool length comp) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 G93 X.01 Y.01 Z.01 A-19.9 B-19.9 F300. ; (Inverse time feed on , 1st linear motion) ; X0.02 Y0.03 Z0.04 A-19.7 B-19.7 F300. ( 2nd motion) ; X0.02 Y0.055 Z0.064 A-19.5 B-19.6 F300. (3rd motion) ; X2.345 Y.1234 Z-1.234 A-4.127 B-12.32 F200. ; (Last motion) ; (BEGIN COMPLETION BLOCKS) ; G94 F50. (Inverse time feed off) ; G00 G90 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Tool length comp off) ; (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.1.62 G150 General Purpose Pocket Milling (Group 00)

- D - Tool radius/diameter offset selection
- F - Feedrate
- I - X-Axis cut increment (positive value)
- J - Y-Axis cut increment (positive value)
- K - Finishing pass amount (positive value)
- P - Subprogram number that defines pocket geometry
- Q - Incremental Z-Axis cut depth per pass (positive value)
* R - Position of the rapid R-plane location
* S - Spindle speed
- X - X start position
- Y - Y start position
- Z - Final depth of pocket
* indicates optional

The G150 starts by positioning the cutter to a start point inside the pocket, followed by the outline,  and  completes  with  a  finish  cut.  The  end  mill  will  plunge  in  the  Z-Axis.  A subprogram P### is called, which defines the pocket geometry of a closed area using G01 , G02 , and G03 motions in the X and Y axes on the pocket. The G150 command will search for an internal subprogram with a N-number specified by the P-code. If that is not found the control will search for an external subprogram. If neither are found, alarm 314 Subprogram Not In Memory will be generated.

When defining the G150 pocket geometry in the subprogram, do not move back to the starting hole after the pocket shape is closed.

The pocket geometry subprogram cannot use macro variables.

An I or J value  defines the roughing pass amount the cutter moves over for each cut increment. If I is used, the pocket is roughed out from a series of increment cuts in the X-Axis. If J is used, the increment cuts are in the Y-Axis.

The K command defines a finish pass amount on the pocket. If a K value is specified, a finish pass is performed by K amount, around the inside of pocket geometry for the last pass and is done at the final Z depth. There is no finishing pass command for the Z depth.

The R value needs to be specified, even if it is zero ( R0 ),  or  the last R value that was specified will be used.

<!-- image -->

<!-- image -->

Multiple passes in the pocket area are done, starting from the R plane, with each Q (Z-Axis depth) pass to the final depth. The G150 command will first make a pass around pocket geometry, leaving stock with K , then doing passes of I or J roughing out inside of pocket after feeding down by the value in Q until the Z depth is reached.

The Q command must be in the G150 line, even if only one pass to the Z depth is desired.

The Q command starts from the R plane.

Notes: The subprogram ( P ) must not consist of more than 40 pocket geometry moves.

It may be necessary to drill a starting point, for the G150 cutter, to the final depth (Z). Then position the end mill to the start location in the XY axes within the pocket for the G150 command.

## F7.38: G150 General Pocket Milling: [1] Start Point, [Z] Final depth.

<!-- image -->

```
% O61501 (G150 GENERAL POCKET MILLING) ; (G54 X0 Y0 is at the bottom-left) ; (Z0 is on top of the part) ; (T1 is a .5" endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X3.25 Y4.5 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z1.0 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G150 X3.25 Y4.5 Z-1.5 G41 J0.35 K.01 Q0.25 R.1 P61502 D01 F15. ; (Pocket mill sequence, call pocket subprogram) ; (Cutter comp on) ; (0.01' finish pass K on sides) ; G40 X3.25 Y4.5 (Cutter comp off) ;
```

```
(BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; % % O61502 (G150 GENERAL POCKET MILL SUBPROGRAM) ; (Subprogram for pocket in O61501) ; (Must have a feedrate in G150) ; G01 Y7. (First linear move onto pocket geometry) ; X1.5 (Linear move) ; G03 Y5.25 R0.875 (CCW arc) ; G01 Y2.25 (Linear move) ; G03 Y0.5 R0.875 (CCW arc) ; G01 X5. (Linear move) ; G03 Y2.25 R0.875 (CCW arc) ; G01 Y5.25 (Linear move) ; G03 Y7. R0.875 (CCW arc) ; G01 X3.25 (Close pocket geometry) ; M99 (Exit to Main Program) ; %
```

## Square Pocket

## F7.39: G150 General Purpose Pocket Milling: 0.500 diameter endmill.

<!-- image -->

5.0 x 5.0 x 0.500 DP. Square Pocket

## Main Program

%

```
O61503 (G150 SQUARE POCKET MILLING) ; (G54 X0 Y0 is at the center of the part) ; (Z0 is on top of the part) ; (T1 is a .5" endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X0 Y1.5 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z1.0 (Activate tool offset 1) ; M08(Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z0.1 F10. (Feed right above the surface) ; G150 P61504 Z-0.5 Q0.25 R0.01 J0.3 K0.01 G41 D01 F10. ; (Pocket Mill sequence, call pocket subprogram) ; (Cutter comp on) ; (0.01' finish pass K on sides) ; G40 G01 X0. Y1.5 (Cutter comp off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract,Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## Subprogram

```
% O61505 (G150 INCREMENTAL SQUARE POCKET MILLING SUBPROGRAM) ; (Subprogram for pocket in O61503) ; (Must have a feedrate in G150) ; G91 G01 Y0.5 (Linear move to position 1) ; X-2.5 (Linear move to position 2) ; Y-5. (Linear move to position 3) ; X5. (Linear move to position 4) ; Y5. (Linear move to position 5) ; X-2.5 (Linear move to position 6, Close Pocket Loop) ; G90 (Turn off incremental mode, Turn on absolute) ; M99 (Exit to Main Program) ; %
```

Absolute  and  Incremental  examples  of  a  subprogram  called  up  by  the P#### command in the G150 line:

## Absolute Subprogram

```
% O61504 (G150 ABSOLUTE SQUARE POCKET MILLING SUBPROGRAM) ; (Subprogram for pocket in O61503) ; (Must have a feedrate in G150) ; G90 G01 Y2.5 (Linear move to position 1) ; X-2.5 (Linear move to position 2) ; Y-2.5 (Linear move to position 3) ; X2.5 (Linear move to position 4) ; Y2.5 (Linear move to position 5) ; X0. (Linear move to position 6, Close Pocket Loop) ; M99 (Exit to Main Program) ; %
```

## Incremental Subprogram

```
% O61505 (G150 INCREMENTAL SQUARE POCKET MILLING SUBPROGRAM) ; (Subprogram for pocket in O61503) ; (Must have a feedrate in G150) ; G91 G01 Y0.5 (Linear move to position 1) ; X-2.5 (Linear move to position 2) ; Y-5. (Linear move to position 3) ; X5. (Linear move to position 4) ; Y5. (Linear move to position 5) ; X-2.5 (Linear move to position 6, Close Pocket Loop) ; G90 (Turn off incremental mode, Turn on absolute) ; M99 (Exit to Main Program) ; %
```

## Square Island

## F7.40: G150 Pocket Milling Square Island: 0.500 diameter endmill.

<!-- image -->

## 5.0 x 5.0 x 0.500 DP. Square Pocket with Square Island

## Main Program

```
% O61506 (G150 SQUARE ISLAND POCKET MILLING) ; (G54 X0 Y0 is at the bottom-left) ; (Z0 is on top of the part) ; (T1 is a .5" endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y2. (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z1.0(Activate tool offset 1) ; M08(Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z0.01 F30. (Feed right above the surface) ; G150 P61507 X2. Y2. Z-0.5 Q0.5 R0.01 I0.3 K0.01 G41 D01 F10. ; (Pocket mill sequence, call pocket subprogram) ; (Cutter comp off) ; (0.01' finish pass K on sides) ; G40 G01 X2.Y2. (Cutter comp off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## Subprogram

```
% O61507 (G150 SQUARE ISLAND POCKET MILLING SUBPROGRAM) ; (Subprogram for pocket in O61503) ; (Must have a feedrate in G150) ; G01 Y1. (Linear move to position 1) ; X6. (Linear move to position 2) ; Y6. (Linear move to position 3) ; X1. (Linear move to position 4) ; Y3.2 (Linear move to position 5) ; X2.75 (Linear move to position 6) ; Y4.25 (Linear move to position 7) ; X4.25 (Linear move to position 8) ; Y2.75 (Linear move to position 9) ; X2.75 (Linear move to position 10) ; Y3.8 (Linear move to position 11) ; X1. (Linear move to position 12) ; Y1. (Linear move to position 13) ; X2. (Linear move to position 14, Close Pocket Loop) ; M99 (Exit to Main Program) ; %
```

## Round Island

## F7.41: G150 Pocket Milling Round Island: 0.500 diameter endmill.

5.0 x 5.0 x 0.500 DP. Square Pocket with Round Island

<!-- image -->

## Main Program

```
% O61508 (G150 SQ POCKET W/ ROUND ISLAND MILLING) ; (G54 X0 Y0 is at the bottom-left) ; (Z0 is on top of the part) ; (T1 is a .5" endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y2. (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z1.0 M08 (Activate tool offset 1) ; (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z0.01 F30. (Feed right above the surface) ; (Pocket mill sequence, call pocket subprogram) ; (Cutter comp on) ; (0.01' finish pass K on sides) ; G40 G01 X2.Y2. (Cutter comp off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ;
```

```
G150 P61509 X2. Y2. Z-0.5 Q0.5 R0.01 J0.3 K0.01 G41 D01 F10. ; %
```

## Subprogram

```
% O61509 (G150 SQ POCKET W/ ROUND ISLAND MILLING SUBPROGRAM) ; (Subprogram for pocket in O61503) ; (Must have a feedrate in G150) ; G01 Y1. (Linear move to position 1) ; X6. (Linear move to position 2) ; Y6. (Linear move to position 3) ; X1. (Linear move to position 4) ; Y3.5 (Linear move to position 5) ; X2.5 (Linear move to position 6) ; G02 I1. (CW circle along X axis at position 7) ; G02 X3.5 Y4.5 R1. (CW arc to position 8) ; G01 Y6. (Linear move to position 9) ; X1. (Linear move to position 10) ; Y1. (Linear move to position 11) ; X2. (Linear move to position 12, Close Pocket Loop) ; M99 (Exit to Main Program) ;
```

%

## 7.1.63 G154 Select Work Coordinates P1-P99 (Group 12)

This feature provides 99 additional work offsets. G154 with a P value from 1 to 99 activates additional work offsets.  For  example G154  P10 selects  work offset 10  from the  list  of additional work offsets.

<!-- image -->

NOTE:

<!-- image -->

NOTE:

G110 to G129 refer to the same work offsets as G154 P1 through P20 ; they can be selected by using either method.

When a G154 work offset is active, the heading in the upper right work offset will show the G154 P value.

The P values are modal. This means if you are in the middle of a canned cycle and a G04 Pnn or an M97 Pnn is used the P value will be used for the dwell / subprogram as well as the canned cycle.

G154 work offsets format

```
#14001-#14006 G154 P1 (also #7001-#7006 and G110) #14021-#14026 G154 P2 (also #7021-#7026 and G111) #14041-#14046 G154 P3 (also #7041-#7046 and G112) #14061-#14066 G154 P4 (also #7061-#7066 and G113) #14081-#14086 G154 P5 (also #7081-#7086 and G114) #14101-#14106 G154 P6 (also #7101-#7106 and G115) #14121-#14126 G154 P7 (also #7121-#7126 and G116) #14141-#14146 G154 P8 (also #7141-#7146 and G117) #14161-#14166 G154 P9 (also #7161-#7166 and G118) #14181-#14186 G154 P10 (also #7181-#7186 and G119) #14201-#14206 G154 P11 (also #7201-#7206 and G120) #14221-#14226 G154 P12 (also #7221-#7226 and G121) #14241-#14246 G154 P13 (also #7241-#7246 and G122) #14261-#14266 G154 P14 (also #7261-#7266 and G123)
```

```
#14281-#14286 G154 P15 (also #7281-#7286 and G124) #14301-#14306 G154 P16 (also #7301-#7306 and G125) #14321-#14326 G154 P17 (also #7321-#7326 and G126) #14341-#14346 G154 P18 (also #7341-#7346 and G127) #14361-#14366 G154 P19 (also #7361-#7366 and G128) #14381-#14386 G154 P20 (also #7381-#7386 and G129) #14401-#14406 G154 P21 #14421-#14426 G154 P22 #14441-#14446 G154 P23 #14461-#14466 G154 P24 #14481-#14486 G154 P25 #14501-#14506 G154 P26 #14521-#14526 G154 P27 #14541-#14546 G154 P28 #14561-#14566 G154 P29 #14581-#14586 G154 P30 #14781-#14786 G154 P40 #14981-#14986 G154 P50 #15181-#15186 G154 P60 #15381-#15386 G154 P70 #15581-#15586 G154 P80 #15781-#15786 G154 P90 #15881-#15886 G154 P95 #15901-#15906 G154 P96 #15921-#15926 G154 P97 #15941-#15946 G154 P98 #15961-#15966 G154 P99
```

## 7.1.64 G156 Broaching Canned Cycle (Group 09)

- Z - Z-axis absolute location total pecking depth.
* X - X-axis absolute location of furthest slice cycle.
* Y - Y-axis absolute location of furthest slice cycle.
* I - size of increment between slice cycles.
* K - Z-axis size of increment between pecks in a cycle.
* F - Feed rate per minute.
* C - C-axis position.
* D - Tool clearance when returning to starting plane.

*indicates optional

The machine must have software version 100.20.000.1000 or higher to use this G-code.

NOTE:

<!-- image -->

F7.42: G156 Broaching Canned Cycle: [S] Start position, [I] Slices, [K] Pecks.

<!-- image -->

Broaching operations canned cycle can be done on Inner and outer grooves in different position using the G156 code with an optional address codes which define the tool Pecks and the cut paths.

F7.43: Broaching operations canned cycle can be done using a single tool path (with adjustable programmable Pecks) when using a special broaching shape tool.

<!-- image -->

Spindle orient command M19 P / R code which used to position the spindle before broaching must be used first before executing G156 broaching canned cycle.

M19 , P , or R should not be on the same line as G156 . M19 , P , or R value should not be negative. See

M19

for more information.

<!-- image -->

NOTE:

When  moving  the  program  and  broach  tool  from  one  machine  to another, the R value in the M19 (spindle orientation) line may change.

When K is added to a G156 block, then pecking will be performed at each interval specified by K .

The D code  can  be  used  for  grooving  and  turning  to  provide  material  clearance  when returning to starting plane S .

The D code command is used to provide a tool clearance shift, in the X-axis before returning in the Z-axis to the "C" clearance point.

When an X ,  or Y code is added to a G156 block  and  the  current  (i.e.  actual) X ,  Y-axis machine position not at the position defined by G156 X or Y , then a minimum of two pecking canned cycles will occur, one at the current (actual) location of the machine X Y-axis, and another one at the X Y location set by G156.

<!-- image -->

<!-- image -->

## NOTE:

<!-- image -->

NOTE:

The I code is the incremental distance (slices cycle) between the start position S toward the target X / Y Axes positions (i.e. the thickness of each slice).

Adding  an I will  performs  multiple,  evenly  spaced,  slice  cycles  between  the  starting position S and X / Y target position.

When the distance between S and target X / Y is  not  evenly divisible by I ,  then  the  last interval is less than I .

The tool clearance shift direction (i.e. shift in + X or - X, ZX plane,) will be depend on the sign of the D value (Positive/Negative).

When the D has a positive value, the tool moves in the positive direction of the X-axis.

When the D has a negative value, the tool moves further in the negative direction of the X-axis.

When D has a zero value or it not specified with the G156 lathe broaching canned cycle, then there shall be no tool clearance shift in the X-axis before returning in the Z-axis to the "C" clearance point.I.e. the tool returning in the Z axis to the "C" clearance point will use the same peck path in the opposite direction.

An alarm will be generated if any spindle commanded to turn (other than spindle orient/ c axis position) within broaching canned cycle, or the broaching canned cycle is starting the Pecks cycle and the spindle is still turning.

Cxx (position the C axis) could be use before or on the same line of G156 broaching canned cycle.

The broaching canned cycle is a modal, and should be repeated on each line within the canned cycle uses any broaching address code. Refer to example below:

## T7.2: Mill Broaching: Example 1

| G-Code                                                                                                                                     | Program Sequence                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| % G156 X-10. Y-5.0 Z-12.0 I0.5 K0.5 F10.; X-5. Y-2.0 Z-10.0 I2.0 K2.0; I1.0 K1.0; C90.; C45.0 X-5. Y-3.0 Z-10.0 I2.0 K2.0; M19; G00 G80; % | • Mill Broaching Operations Canned Cycle Start. • Perform another broach with new XYZIK address codes values. • Perform another broach with new IK address codes values. • Perform another broach at new angle using the last specified address codes. • Rotate to new angle then broach using the new address codes values. • Orient the spindle. • End of Canned Cycle. |

## 7.1.65 G167 - Modify Setting (Group 00)

- P - This code specifies the setting number.
- Q - specifies the setting value. This can be a decimal numeric value or an enumerated representation for unit-less settings.
- K - the number after the K code specifies a guard code for permanent changes.

This  G-code  allows  the  user  permanently  make  changes  to  settings  during  program execution.

The control will generate an Alarm when:

- the P or Q code is missing.
- the P code is not a valid setting number.
- the Q code is not a valid for the setting number.

## Examples of G167:

## Example #1

```
G167 P250 Q1 K10755;
```

Turns on setting 250 Mirror Image C Axis.

## Example #2

<!-- image -->

NOTE:

G167 P84 Q3 K10755;

Sets setting 84 Tool Overload Action to Autofeed.

## Example #3

G167 P142 Q1.25 K10755;

Sets setting 142 Offset Chng Tolerance to 1.25.

## 7.1.66 G174 CCW / G184 CW Non-Vertical Rigid Tap (Group 00)

- F - Feedrate
- X - X position at bottom of hole
- Y - Y position at bottom of hole
- Z - Z position at bottom of hole
* S - Spindle Speed
* indicates optional

A  specific X , Y , Z , A , B position  must  be  programmed  before  the  canned  cycle  is commanded. This position is used as the Start position.

This G code is used to perform rigid tapping for non-vertical holes. It may be used with a right-angle head to perform rigid tapping in the X or Y Axis on a three-axis mill, or to perform rigid tapping along an arbitrary angle with a five-axis mill. The ratio between the feedrate and spindle speed must be precisely the thread pitch being cut.

It  is  not  necessary  to  start  the  spindle  before  this  canned  cycle;  the  control  does  this automatically.

## 7.1.67 G187 Accuracy Control (Group 00)

G187 is  an accuracy command that can set and control both the smoothness and max corner rounding value when cutting a part. The format for using G187 is G187 Pn Ennnn .

- P - Controls the smoothness level, P1 (rough), P2 (medium), or P3 (finish). Temporarily overrides Setting 191.
- E - Sets the max corner rounding value. Temporarily overrides Setting 85.

Setting 191 sets the default smoothness to the user specified ROUGH , MEDIUM , or FINISH when G187 is not active. The Medium setting is the factory default setting.

Changing Setting 85 to a low value may make the machine operate as if it is in exact stop mode.

<!-- image -->

Changing setting 191 to FINISH will take longer to machine a part. Use this setting only when needed for the best finish.

G187 Pm Ennnn sets both the smoothness and max corner rounding value. G187 Pm sets the smoothness but leaves max corner rounding value at its current value. G187 Ennnn sets the max corner rounding but leaves smoothness at its current value. G187 by itself cancels the E value and sets smoothness to the default smoothness specified by Setting 191. G187 will be canceled whenever [RESET] is pressed, M30 or M02 is executed, the end of program is reached, or [EMERGENCY STOP] is pressed.

## 7.1.68 G234 Tool Center Point Control (TCPC) (Group 08)

G234 Tool Center Point Control (TCPC) lets a machine correctly run a contouring 4- or 5-axis program when the workpiece is not located in the exact location specified by the CAM-generated program. This eliminates the need to repost a program from the CAM system when the programmed and the actual workpiece locations are different.

<!-- image -->

<!-- image -->

If you intend to use G268 or G269 with G234 then G268 must be called first or Alarm 2062 TCPC OR DWO INCOMPATIBLE CODE will be generated.

## VR/GM-2-5AX - G234 - Tool Center Point Control (TCPC)

G234 Tool Center Point Control (TCPC) is a software feature in the Haas CNC control that allows a machine to correctly run a contouring 4- or 5-axis program when the workpiece is not located in the exact location specified by a CAM-generated program.

This eliminates the need to repost a program from the CAM system when the programmed and the actual  workpiece  locations  are  different.  The  Haas  CNC  control  combines  the known centers of rotation for the rotary axes (MRZP) and the location of the workpiece (e.g., active work offset G54 ) into a coordinate system.

TCPC makes sure that this coordinate system remains fixed relative to the table; when the rotary axes rotate, the linear coordinate system rotates with them. Like any other work setup, the workpiece must have a work offset applied to it. This tells the Haas CNC control where the workpiece is located on the machine table.

TCPC is activated with G234 . G234 cancels the previous H-code. An H-code must therefore be placed on the same block as G234 . G234 is canceled by G49 , G42 , and G44 .

The rotary axes must be at 0 before commanding G234 .

<!-- image -->

NOTE:

<!-- image -->

NOTE:

TCPC G-code is programmed from the tool tip. The control knows the centers of rotation for the rotary axes (MRZP), the location of the workpiece (active work offset), and the tool length offset. The control uses this data to calculate the position of tool tip relative to the active work offset and maintains a static tool tip position through rotary feed moves.

Tool tip position is not maintained during rapid rotary moves. Do not program rapid moves while TCPC is active.

The diagram below illustrates TCPC positioning.

TCPC Program Example

<!-- image -->

When starting TCPC it is safest to establish a new XYZ using a rapid move. The example below has a rapid G00 XYZ move after the G234 H code.

```
% O00003 (TCPC SAMPLE); G20; G00 G17 G40 G80 G90 G94 G98; G53 Z0.; T1 M06; G00 G90 G54 B0. C0. (POSITION ROTARY AXES); G00 G90 X-0.9762 Y1.9704 S10000 M03 (POSITION LINEAR AXES); G234 H01(TCPC ON WITH LENGTH OFFSET 1); G00 X-0.9762 Y1.9704; G00 Z1.0; G01 X-0.5688 Y1.1481 Z0.2391 B43.421 C115.162 F40.;
```

<!-- image -->

NOTE:

```
X-0.4386 Y0.8854 Z-0.033 B43.421 C116.576; X-0.3085 Y0.6227 Z-0.3051 B45.421 C116.654; X-0.307 Y0.6189 Z-0.3009 B46.784 C116.382; X-0.3055 Y0.6152 Z-0.2966 B46.43 C116.411; X-0.304 Y0.6114 Z-0.2924 B46.076 C116.44; X-0.6202 Y0.5827 Z-0.5321 B63.846 C136.786; X-0.6194 Y0.5798 Z-0.5271 B63.504 C136.891; X-0.8807 Y0.8245 Z-0.3486; X-1.1421 Y1.0691 Z-0.1701; X-1.9601 Y1.8348 Z0.3884G49 (TCPC OFF); G00 G53 Z0.; G53 B0. C0.; G53 Y0.; M30; %
```

## UMC - G234 - Tool Center Point Control (TCPC) (Group 08)

G234 Tool Center Point Control (TCPC) is a software feature in the Haas CNC control that allows a machine to correctly run a contouring 4- or 5-axis program when the workpiece is not located in the exact location specified by a CAM-generated program. This eliminates the need to repost a program from the CAM system when the programmed and the actual workpiece locations are different.

The Haas CNC control combines the known centers of rotation for the rotary table (MRZP) and the location of the workpiece (e.g., active work offset G54) into a coordinate system. TCPC makes sure that this coordinate system remains fixed relative to the table; when the rotary axes rotate, the linear coordinate system rotates with them. Like any other work setup, the workpiece must have a work offset applied to it. This tells the Haas CNC control where the workpiece is located on the machine table.

The conceptual example and illustrations in this section represent a line segment from a full 4- or 5-axis program.

For clarity, the illustrations in this section do not depict workholding. Also,  as conceptual, representative drawings, they are not to scale and may not depict the exact axis motion described in the text.

The straight line edge highlighted in Figure F7.45 is defined by point (X0, Y0, Z0) and point (X0, Y-1., Z0). Movement along the Y Axis is all that is required for the machine to create this edge. The location of the workpiece is defined by work offset G54.

## F7.45: Location of Workpiece Defined by G54

<!-- image -->

In Figure F7.46 , the B and C Axes have been rotated 15 degrees each. To create the same edge, the machine needs to make an interpolated move with the X, Y, and Z Axes. Without TCPC, you would need to repost the CAM program for the machine to correctly create this edge.

## F7.46: G234 (TCPC) Off and the B and C Axes Rotated

<!-- image -->

TCPC is invoked in Figure F7.47 . The Haas CNC control knows the centers of rotation for the rotary table (MRZP), and the location of the workpiece (active work offset G54). This data  is  used  to  produce  the  desired  machine  motion  from  the  original  CAM-generated program. The machine follows an interpolated X-Y-Z path to create this edge, even though the program simply commands a single-axis move along the Y Axis.

## F7.47: G234 (TCPC) On and the B and C Axes Rotated

<!-- image -->

## G234 Programmer's Notes

These key presses and program codes cancel G234:

- [ EMERGENCY STOP]
- [ RESET]
- [ HANDLE JOG]
- [ LIST PROGRAM]
- M02 - Program End
- M30 - Program End and Reset
- G43 - Tool Length Compensation +
- G44 - Tool Length Compensation -
- G49 - G43 / G44 / G143 Cancel

These codes will NOT cancel G234:

- M00 - Program Stop
- M01 - Optional Stop

These key presses and program codes impact G234:

- G234 invokes TCPC and cancels G43.
- When using tool length compensation, either G43 or G234 must be active. G43 and G234 cannot be active at the same time.
- G234 cancels the previous H-code. An H-code must therefore be placed on the same block as G234.
- G234 cannot be used at the same time as G254 (DWO).

These codes ignore 234:

- G28 - Return to Machine Zero Through Optional Reference Point

- G29 - Move to Location Thru G29 Reference Point
- G53 - Non-Modal Machine Coordinate Selection
- M06 - Tool Change

Invoking G234 (TCPC) rotates the work envelope. If the position is close to the travel limits, the rotation can put the current work position outside of travel limits and cause an over travel alarm. To solve this, command the machine to the center of the work offset (or near the center of the table on a UMC), and then invoke G234 (TCPC).

G234 (TCPC) is intended for simultaneous 4- and 5-axis contouring programs. An active work offset (G54, G55, etc.) is required to use G234.

## 7.1.69 G253 Orient Spindle Normal To Feature Coordinate System (Group 00)

G253 is a 5 axis G-Code used to orient the spindle normal the feature coordinate system. This code can only be used while G268 is active.

```
% O00005 (G268 WITH G81 DRILL CANNED CYCLE)(COMMAND ANGLE WITH IJK BEFORE MOVING TO OFFSET); T1 M06 (TOOL CHANGE); G54 G00 G40 G80 G17 G90 (GENERAL SAFE STARTUP LINE); X0 Y0 S1500 M03 (INITIAL XYZ LOCATION); G43 Z06. H01 (ENACT TOOL LENGTH COMP.); G268 X2. Y2. Z0 I0 J30. K45. Q123 (SET TILTED PLANE); G253 (MOVE SPINDLE PERPENDICULAR TO TILTED PLANE); G00 X0 Y0 Z.5 (MOVE TO START LOCATION); G81 G98 R0.1 Z-1. F75.; G80; G269 (CANCEL TILTED PLANE); G00 G53 Z0 M05; G53 B0 C0; G53 X0 Y0; M30; %
```

## 7.1.70 G254 Dynamic Work Offset (DWO) (Group 23)

G254 Dynamic Work Offset (DWO) is similar to TCPC, except that it is designed for use with 3+1 or 3+2 positioning, not for simultaneous 4- or 5-axis machining. If the program does not use the B and C Axes, there is no need to use DWO.

UMC - G254 - Dynamic Work Offset (DWO) (Group 23)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## NOTE:

G254 Dynamic Work Offset (DWO) is similar to TCPC, except that it is designed for use with 3+1 or 3+2 positioning, not for simultaneous 4- or 5-axis machining. If the program does not make use of the tilt and rotary Axes, there is no need to use DWO.

The B-Axis value of the work offset you use with G254 MUST be zero.

With DWO, you no longer need to set the workpiece in the exact position as programmed in the CAM system. DWO applies the appropriate offsets to account for the differences between  the  programmed  workpiece  location  and  the  actual  workpiece  location.  This eliminates the need to repost a program from the CAM system when the programmed and actual workpiece locations are different.

The control knows the centers of rotation for the rotary table (MRZP) and the location of the workpiece (active work offset). This data is used to produce the desired machine motion from the original CAM-generated program. Therefore, it is recommended that G254 be invoked after the desired work offset is commanded, and after any rotational command to position the 4th and 5th axes.

After G254 is  invoked, you must  specify an X, Y, and Z Axis  position  before a cutting command, even if it recalls the current position. The program should specify the X- and Y Axis position in one block and the Z Axis in a separate block.

Before  rotary  motion,  use  a  G53  Non-Modal  Machine  Coordinate motion command to safely retract  the  tool  from  the  workpiece  and allow clearance for the rotary motion. After the rotary motion finishes, specify an X-, Y-, and Z-Axis position before a cutting command, even if it recalls the current position. The program should specify the X- and Y-Axis  position  in  one  block  and  the  Z-Axis  position  in  a  separate block.

Be  sure  to  cancel  G254  with  G255  when  your  program  does simultaneous 4- or 5-axis machining.

For clarity, the illustrations in this section do not depict workholding.

The block in the figure below was programmed in the CAM system with the top center hole located at the center of the pallet and defined as X0, Y0, Z0.

## F7.48: Original Programmed Position

<!-- image -->

In the figure below, the actual workpiece is not located in this programmed position. The center of the workpiece is actually located at X3, Y-2, Z0, and is defined as G54.

## F7.49: Center at G54, DWO Off

<!-- image -->

DWO is invoked in the figure below. The control knows the centers of rotation for the rotary table (MRZP), and the location of the workpiece (active work offset G54). The control uses this data to apply the appropriate offset adjustments to make sure that the proper toolpath is applied to the workpiece, as intended by the CAM-generated program. This eliminates the need to repost a program from the CAM system when the programmed and actual workpiece locations are different.

## F7.50: Center with DWO On

<!-- image -->

## G254 Program Example

```
% O00004 (DWO SAMPLE) ; G20 ; G00 G17 G40 G80 G90 G94 G98 ; G53 Z0. ; T1 M06 ; G00 G90 G54 X0. Y0. B0. C0. (G54 is the active work offset for) ; (the actual workpiece location) ; S1000 M03 ; G43 H01 Z1. (Start position 1.0 above face of part Z0.) ; G01 Z-1.0 F20. (Feed into part 1.0) ; G00 G53 Z0. (Retract Z with G53) ; B90. C0. (ROTARY POSITIONING) ; G254 (INVOKE DWO) ; X1. Y0. (X and Y position command) ; Z2. (Start position 1.0 above face of part Z1.0) ; G01 Z0. F20. (Feed into part 1.0 ) ; G00 G53 Z0. (Retract Z with G53) ; B90. C-90. (ROTARY POSITIONING) ; X1. Y0. (X and Y position command) ; Z2. (Start position 1.0 above face of part Z1.0) ; G01 Z0. F20. (Feed into part 1.0 ) ; G255 (CANCEL DWO) ; B0. C0. ; M30 ; %
```

## G254 Programmer's Notes

These key presses and program codes will cancel G254:

- [ EMERGENCY STOP]
- [ RESET]
- [ HANDLE JOG]
- [ LIST PROGRAM]
- G255 - Cancel DWO
- M02 - Program End
- M30 - Program End and Reset

These codes will NOT cancel G254:

- M00 - Program Stop
- M01 - Optional Stop

Some codes ignore G254 . These codes will not apply rotational deltas:

- *G28 - Return to Machine Zero Through Optional Reference Point
- *G29 - Move to Location Through G29 Reference Point
- G53 - Non-Modal Machine Coordinate Selection
- M06 - Tool Change

*It is strongly recommended that you not use G28 or G29 while G254 is active, nor when the B and C Axes are not at zero.

1. G254 (DWO) is intended for 3+1 and 3+2 machining, where the B and C Axes are used to position only.
2. An active work offset ( G54 , G55 , etc.) must be applied before G254 is commanded.
3. All rotary motion must be complete before G254 is commanded.
4. After G254 is invoked, you must specify an X-, Y-, and Z-Axis position prior to any cutting command, even if it recalls the current position. It is recommended to specify the X and Y Axes in one block, and the Z Axis in a separate block.
5. Cancel G254 with G255 immediately after use and before ANY rotary motion.
6. Cancel G254 with G255 any time simultaneous 4- or 5-axis machining is performed.
7. Cancel G254 with G255 and retract the cutting tool to a safe location before the workpiece is repositioned.

## 7.1.71 G255 Cancel Dynamic Work Offset (DWO) (Group 23)

G255 cancels G254 Dynamic Work Offset (DWO).

## 7.1.72 G266 Visible Axes Linear Rapid %Motion (Group 00)

- E - Rapid rate.
- P - Axis parameter number. Example P1 = X, P2 = Y, P3 = Z.
- I - Machine coordinate position command.

The below example commands the X-axis to move to X-1. at 10% rapid rate.

```
% G266 E10. P1 I-1. (RAPID AXIS #1, X, AT 10%, TO MACHINE POSITION -1.0) %
```

## 7.1.73 G268 / G269 Feature Coordinate System (Group 14)

- X - Feature coordinate system origin X coordinate in the WCS.
- Y - Feature coordinate system origin Y coordinate in the WCS.
- Z - Feature coordinate system origin Z coordinate in the WCS.
* I - Rotation of feature coordinate system about working coordinate system X axis.
* J - Rotation of feature coordinate system about working coordinate system Y axis.
* K - Rotation of feature coordinate system about working coordinate system Z axis.
* Q - Qnnn is used to define the order in which the I,J,K rotations will be applied. The default value used if Q is omitted, Q123 rotates about X, then Y, then Z. Q321 rotates about Z, then Y, then X.
* indicates optional

If you intend to use G268 or G269 with G234 then G268 must be called first or Alarm 2062 TCPC OR DWO INCOMPATIBLE CODE will be generated.

<!-- image -->

NOTE:

## F7.51: G268 Feature Coordinate System

<!-- image -->

G268 is a 5 axis G-Code used to define a tilted feature coordinate system relative to the working coordinate system. Canned cycles and G-codes work normally within the feature coordinate  system.  Before  activating G268 , G43 Tool  Length  Compensation,  must  be activated. However, the transformation from the working coordinate system to the feature coordinate system is performed independently from the tool length offset. Calling G268 only establishes  the  feature  coordinate  system.  It  does  not  cause  motion  in  any  axis.  After calling G268 the current position of the spindle must be recalled. G269 is used to cancel G268 and revert back the WCS.

There  are  two  ways  to  define  a  feature  coordinate  system  using G268 .  The  first  is  to command the B and C axis to the desired angle and specify only the feature coordinate system origin using G268 . The feature coordinate system plane will be the plane normal to the spindle axis at the moment G268 is called.

```
% O00001 (G268 WITH G81 DRILL CANNED CYCLE)(ANGLE FROM SPINDLE POSITION); T1 M06 (TOOL CHANGE); G54 G00 G40 G80 G17 G90 (GENERAL SAFE STARTUP LINE); X0 Y0 S1500 M03 (INITIAL XYZ LOCATION);
```

```
G00 B30. C45. (SET SPINDLE ANGLE); G43 Z6. H01 (ENACT TOOL LENGTH COMP.); G268 X2. Y2. Z0 (SET TILTED PLANE); G00 X0 Y0 Z.5 (RECALL POSITION); G81 G98 R0.1 Z-1. F75.; G80; G269 (CANCEL TILTED PLANE); G00 G53 Z0 M05; G53 B0 C0; G53 X0 Y0; M30; %
```

The second way to define a feature coordinate system using G268 is to use the optional I, J, K, and Q address codes to specify rotation angles relative to the WCS and rotation order. By using this method, a feature coordinate system that is not normal to the spindle axis may be defined.

```
% O00002 (G268 WITH G81 DRILL CANNED CYCLE)(COMMAND ANGLE WITH IJK & Q); T1 M06 (TOOL CHANGE); G54 G00 G40 G80 G17 G90 (GENERAL SAFE STARTUP LINE); X0 Y0 S1500 M03 (INITIAL XYZ LOCATION); G00 B30. C45. (SET SPINDLE ANGLE); G43 Z06. H01 (ENACT TOOL LENGTH COMP.); G268 X2. Y2. Z0 I0 J30. K45. Q123 (SET TILTED PLANE); G00 X0 Y0 Z.5(RECALL POSITION); G81 G98 R0.1 Z-1. F75.; G80; G269 (CANCEL TILTED PLANE); G00 G53 Z0 M05; G53 B0 C0; G53 X0 Y0; M30; %
```

## 7.1.74 G281 Enable / G280 Disable Safe Run (Group 00)

G281 and G280 allow safe run to be turned off and on with G codes. G281 turns safe run on and G280 turns safe run off.

## 7.2 About G-codes

G-codes tell the machine tool what type of action to do, such as:

- Rapid moves

<!-- image -->

NOTE:

<!-- image -->

NOTE:

- Move in a straight line or arc
- Set tool information
- Use letter addressing
- Define axis and beginning and ending positions
- Pre-set  series  of  moves  that  bore  a  hole,  cut  a  specific  dimension,  or  a  contour (canned cycles)

G-code commands are either modal or non-modal. A modal G-code stays in effect until the end  of  the  program  or  until  you  command  another  G-code  from  the  same  group.  A non-modal G-code affects only the line it is in; it does not affect the next program line. Group 00 codes are non-modal; the other groups are modal.

For a description of  basic programming,  refer  to the  basic  programming  section of  the Programming chapter, starting on page 201 .

The Visual Programming System (VPS) is an optional programming mode that  lets  you  program  part  features  without  manually  writing G-code.

A program block can contain more than one G-code, but you cannot put two G-codes from the same group in the same program block.

## 7.3 Canned Cycles

Canned cycles are G-codes that do repetitive operations such as drilling, tapping,  and boring. You define a canned cycle with alphabetic address codes. While the canned cycle is active, the machine does the defined operation every time you command a new position, unless you specify not to.

## 7.4 Using Canned Cycles

You can program canned cycle X and Y positions in either absolute ( G90 ) or incremental ( G91 ).

## Example:

```
% G81 G99 Z-0.5 R0.1 F6.5 (This drills one hole); (at the present location) ; G91 X-0.5625 L9 (This drills 9 more holes 0.5625); (equally spaced in the X-negative direction) ; %
```

<!-- image -->

NOTE:

There  are  (3)  possible  ways  for  a  canned  cycle  to  behave  in  the  block  in  which  you command it:

- If you command an X/Y position in the same block as the canned cycle G-code, the canned cycle executes. If Setting 28 is OFF , the canned cycle executes in the same block only if you command an X/Y position in that block.
- If Setting 28 is ON , and you command a canned cycle G-code with or without an X/Y position in the same block, the canned cycle executes in that block-either at the position where you commanded the canned cycle, or at the new X/Y position.
- If  you  include  a  loop  count  of  zero  ( L0 )  in  the  same  block  as  the  canned  cycle G-code, the canned cycle does not execute in that block. The canned cycle does not execute regardless of Setting 28 and whether or not the block also contains an X/Y position.

Unless otherwise noted, the program examples given here assume that Setting 28 is ON .

When a canned cycle is active, it repeats at every new X/Y position in the program. In the example above, with each incremental move of -0.5625 in the X axis, the canned cycle ( G81 ) drills a 0.5" deep hole. The L address code in the incremental position command ( G91 ) repeats this operation (9) times.

Canned cycles operate differently depending on whether incremental ( G91 )  or  absolute ( G90 ) positioning is active. Incremental motion in a canned cycle is often useful, because it lets you use a loop ( L ) count to repeat the operation with an incremental X or Y move between cycles.

## Example:

```
% X1.25 Y-0.75 (center location of bolt hole pattern) ; G81 G99 Z-0.5 R0.1 F6.5 L0; (L0 on the G81 line will not drill a hole) ; G70 I0.75 J10. L6 (6-hole bolt hole circle) ; %
```

The R plane value and the Z depth value are important canned cycle address codes. If you specify these addresses in a block with XY commands, the control does the XY move, and it does all of the subsequent canned cycles with the new R or Z value.

The X and Y positioning in a canned cycle is done with rapid moves.

<!-- image -->

NOTE:

<!-- image -->

G98 and G99 change the way the canned cycles operate. When G98 is active, the Z-Axis will return to the initial start plane at the completion of each hole in the canned cycle. This allows for positioning up and around areas of the part and/or clamps and fixtures.

When G99 is active, the Z-Axis returns to the R (rapid) plane after each hole in the canned cycle for clearance to the next XY location. Changes to the G98 / G99 selection can also be made after the canned cycle is commanded, which will affect all later canned cycles.

A P address is an optional command for some canned cycles. This is a programmed pause at the bottom of the hole to help break chips, provide a smoother finish, and relieve any tool pressure to hold closer tolerance.

A P address  used  for  one  canned  cycle  is  used  in  others  unless canceled ( G00 , G01 , G80 or the [RESET] button).

You must define an S (spindle  speed) command in or before the canned cycle G-code block.

Tapping in a canned cycle needs a feed rate calculated. The feed formula is:

Spindle speed divided by threads per inch of the tap = feedrate in inches per minute

The metric version of the feed formula is:

```
RPM times metric pitch = feedrate in mm per minute
```

Canned cycles also benefit from the use of Setting 57. If this setting is ON , the machine stops after the X/Y rapids before it moves the Z Axis. This is useful to avoid nicking the part when the tool exits the hole, especially if the R plane is close to the part surface.

The Z, R, and F addresses are required data for all canned cycles.

## 7.5 Canceling a Canned Cycle

G80 cancels all canned cycles. G00 or G01 code also cancel a canned cycle. A canned cycle stays active until G80 , G00 , or G01 cancels it.

## 7.6 Looping Canned Cycles

This is an example of a program that uses an incrementally looped drilling canned cycle.

<!-- image -->

NOTE:

The sequence of drilling used here is designed to save time and to follow the shortest path from hole to hole.

F7.52: G81 Drilling Canned Cycle: [R] R Plane, [Z] Z Plane, [1] Rapid, [2] Feed.

X

<!-- image -->

X

```
% O60810 (Drilling grid plate 3x3 holes) ; (G54 X0 Y0 is at the top-left of part) ; (Z0 is at the top of the part) ; (T1 is a drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X1.0 Y-1.0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Activate tool offset 1) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G81 Z-1.5 F15. R.1 (Begin G81 & drill 1st hole) ; G91 X1.0 L2 (Drill 1st row of holes) ; G90 Y-2.0 (1st hole of 2nd row) ; G91 X-1.0 L2 (2nd row of holes) ; G90 Y-3.0 (1st hole of 3rd row) ;
```

X

X

```
G91 X1.0 L2 (3rd row of holes) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 7.7 X/Y Plane Obstacle Avoidance in a Canned Cycle

If you put an L0 on a canned cycle line, you can make an X, Y move without the Z-Axis canned operation. This is a good way to avoid obstacles in the X/Y plane.

Consider a 6" square aluminum block, with a 1" by 1" deep flange on each side. The print calls for two holes centered on each side of the flange. You use a G81 canned cycle to make the holes. If you simply command the hole positions in the drill canned cycle, the control takes the shortest path to the next hole position, which puts the tool through the corner of the workpiece. To prevent this, command a position past the corner, so the move to the next hole position does not go through the corner. The drill canned cycle is active, but you do not want a drill cycle at that position, so use L0 in this block.

F7.53: Canned Cycle Obstacle Avoidance. The program drills holes [1] and [2], then moves to X5.5. Because of the L0 address in this block, there is no drill cycle in this position. Line [A] shows the path that the canned cycle would follow without the obstacle avoidance line. The next move is in the Y Axis only to the position of the third hole, where the machine does another drill cycle.

<!-- image -->

```
(BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X2. Y-0.5(Rapid to first position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 M08 (Activate tool offset 1) ; (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G81 Z-2. R-0.9 F15. (Begin G81 & Drill 1st hole) ; X4. (Drill 2nd hole) ; X5.5 L0 (Corner avoidance) ; Y-2. (3rd hole) ; Y-4. (4th hole) ; Y-5.5 L0 (Corner avoidance) ; X4. (5th hole) ; X2. (6th hole) ; X0.5 L0 (Corner avoidance) ; Y-4. (7th hole) ; Y-2. (8th hole) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```