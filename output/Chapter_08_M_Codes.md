## Chapter 8: M-codes

## 8.1 List of M-codes

This  chapter  gives  detailed  descriptions  of  the  M-codes  that  you  use  to  program  your machine.

<!-- image -->

## CAUTION:

<!-- image -->

NOTE:

The sample programs in this manual have been tested for accuracy, but they are for illustrative purposes only. The programs do not define tools, offsets, or materials. They do not describe workholding or other fixturing. If you choose to run a sample program on your machine, do so in Graphics mode. Always follow safe machining practices when you run an unfamiliar program.

The sample programs in this manual represent a very conservative programming style. The samples are intended to demonstrate safe and reliable programs, and they are not necessarily the fastest or most efficient  way  to  operate  a  machine.  The  sample  programs  use G-codes that you might choose not to use in more efficient programs.

M-codes are miscellaneous machine commands that do not command axis motion. The format for an M-code is the letter M followed by two to three digits; for example M03 .

Only one M-code is allowed per line of code. All M-codes take effect at the end of the block.

| Setting   | Description           |   Page |
|-----------|-----------------------|--------|
| M00       | Stop Program          |    436 |
| M01       | Optional Program Stop |    436 |
| M02       | Program End           |    436 |
| M03       | Spindle Commands      |    436 |
| M04       | Spindle Commands      |    436 |
| M05       | Spindle Commands      |    436 |

| Setting   | Description                                                        |   Page |
|-----------|--------------------------------------------------------------------|--------|
| M06       | Tool Change                                                        |    437 |
| M07       | Shower Coolant On                                                  |    438 |
| M08 / M09 | Coolant On / Off                                                   |    438 |
| M10 / M11 | Engage / Release 4th Axis Brake                                    |    439 |
| M12 / M13 | Engage / Release 5th Axis Brake                                    |    439 |
| M16       | Tool Change                                                        |    439 |
| M19       | Orient Spindle                                                     |    439 |
| M21-M25   | Optional User M Function with M-Fin                                |    440 |
| M29       | Set Output Relay with M-Fin                                        |    442 |
| M30       | Program End and Reset                                              |    442 |
| M31       | Chip Conveyor Forward                                              |    442 |
| M33       | Chip Conveyor Stop                                                 |    442 |
| M34       | Coolant Increment                                                  |    442 |
| M35       | Coolant Decrement                                                  |    442 |
| M36       | Pallet Part Ready                                                  |    443 |
| M39       | Rotate Tool Turret                                                 |    444 |
| M41 / M42 | Low / High Gear Override                                           |    444 |
| M46       | Qn Pmm Jump to Line                                                |    444 |
| M48       | Validate That The Current Program is Appropriate for Loaded Pallet |    444 |
| M50       | Pallet Change Sequence                                             |    445 |
| M51-M55   | Set Optional User M-codes                                          |    445 |
| M59       | Set Output Relay                                                   |    445 |
| M61-M65   | Clear Optional User M-codes                                        |    446 |

| Setting     | Description                                      | Page    |
|-------------|--------------------------------------------------|---------|
| M69         | Clear Output Relay                               | 446     |
| M70/M71     | Workholding Clamp / Unclamp                      | 447     |
| M73 / M74   | Tool Air Blast (TAB) On / Off                    | 447     |
| M75         | Set G35 or G136 Reference Point                  | 448     |
| M78         | Alarm if Skip Signal Found                       | 448     |
| M79         | Alarm if Skip Signal Not Found                   | 448     |
| M80 / M81   | Auto Door Open / Close                           | 448     |
| M82         | Tool Unclamp                                     | 448     |
| M83 / M84   | Auto Air Gun On / Off                            | 449     |
| M86         | Tool Clamp                                       | 449     |
| M88 / M89   | Through-Spindle Coolant On / Off                 | 449     |
| M90 / M91   | Fixture Clamp Input On / Off                     | 450     |
| M95         | Sleep Mode                                       | 450     |
| M96         | Jump If No Input                                 | 450     |
| M97         | Local Sub-Program Call                           | 452     |
| M98         | Sub-Program Call                                 | 452     |
| M99         | Sub-Program Return or Loop                       | 453     |
| M104 / M105 | Probe Arm Extend/ Retract Interactive User Input | 454 454 |
| M109        |                                                  | 457     |
| M116 / M117 | Vise Air Chips Blast ON/OFF                      |         |
| M130 / M131 | Display Media / Cancel Display Media             | 457     |
| M138 / M139 | Spindle Speed Variation On/Off                   | 458     |
| M158 / M159 | Mist Condenser On/Off                            | 459     |

| Setting     | Description                       |   Page |
|-------------|-----------------------------------|--------|
| M160        | Cancel Active PulseJet            |    459 |
| M161 Pnn    | PulseJet Continuous Mode          |    460 |
| M162 Pnn    | PulseJet Single Event Mode        |    460 |
| M163 Pnn    | PulseJet Modal Mode               |    460 |
| M180 / M181 | Automatic Window Open/Close       |    461 |
| M183/M184   | Auto Air Hole Blast On/OFF        |    461 |
| M199        | Pallet / Part Load or Program End |    462 |
| M300        | M300 - APL/Robot Custom Sequence  |    462 |

## 8.1.1 M00 Stop Program

The M00 code  stops  a  program.  It  stops  the  axes,  spindle,  and  turns  off  the  coolant (including optional Through Spindle Coolant, Through Tool Air Blast, and Auto Air Gun / Minimum Quantity Lubrication). The next block after the M00 is highlighted when viewed in the  program  editor.  Press [CYCLE  START] to  continue  program  operation  from  the highlighted block.

## 8.1.2 M01 Optional Program Stop

M01 works the same as M00 , except the optional stop feature must be on. Press [OPTION STOP] to toggle the feature on and off.

## 8.1.3 M02 Program End

M02 ends a program.

NOTE:

The most common way of ending a program is with an M30 .

<!-- image -->

## 8.1.4 M03 Spindle Fwd / M04 Spindle Rev / M05 Spindle Stop

M03 turns the spindle on in the forward direction.

M04 turns the spindle on in the reverse direction.

M05 stops the spindle, and waits for it to stop.

<!-- image -->

## NOTE:

<!-- image -->

## NOTE:

## 8.1.5 M06 Tool Change

## T - Tool number

The M06 code is used to change tools. For example, M06 T12 puts tool 12 into the spindle. If the spindle is running, the spindle and coolant (including TSC) is stopped by the M06 command.

The  M06  command automatically  stops the  spindle,  stops  coolant, moves the Z Axis to the tool change position, and orients the spindle for the tool change. You do not need to include these commands for a tool change in your program.

M00 , M01 ,  any  work  offset  G-code  ( G54 ,  etc.),  and  block  delete slashes before a tool change stop look-ahead, and the control does not pre-call the next tool to the change position (for a side-mount tool changer only). This can cause significant delays to program execution, because  the  control  must  wait  for  the  tool  to  arrive  at  the  change position before it can execute the tool change. You can command the carousel  to  the  tool  position  with  a  T  code  after  a  tool  change;  for example:

```
M06 T1 (FIRST TOOL CHANGE) ; T2 (PRE-CALL THE NEXT TOOL) ;
```

Refer to page 169 for more information on side-mount tool changer programming.

<!-- image -->

## NOTE:

<!-- image -->

## NOTE:

Spindle speed is controlled with an S address code; for example, S5000 commands a spindle speed of 5000 RPM.

If your machine has a gearbox, the spindle speed you program determines the gear that the machine uses, unless you use M41 or M42 to override gear selection. Refer to page 444 for more information on the gear select override M-codes.

## 8.1.6 M07 Shower Coolant On

M07 starts the optional shower coolant. M09 stops the shower coolant and also stops the standard coolant. The optional shower coolant stops automatically before a tool change or a pallet change. It automatically starts again after a tool change if it was ON before a tool change command.

<!-- image -->

NOTE:

Some  machines  use  optional relays and optional  M-codes  to command shower coolant, such as M51 on and M61 off. Check your machine configuration for the correct M-code programming.

## 8.1.7 M08 Coolant On / M09 Coolant Off

P - M08 Pn

M08 starts the optional coolant supply and M09 stops it.

The control checks the coolant level only at the start of a program, so a low coolant condition will not stop a running program.

Do not use straight or 'neat' mineral cutting oils. They cause damage to rubber components in the machine.

The following applies to machines equipped with the Variable Flow Coolant option.

The variable flow coolant option allows the user to operate the coolant pump at different speeds to increase or decrease the flow of coolant.

An optional P-Code can be specified along with an M08 to change the speed of the coolant pump.

- M08 P0 = Low Pressure - The pump will operate at 50HZ speed.
- M08 P1 = Normal Pressure - The pump will operate at 60HZ speed.
- M08 P2 = High Pressure - The pump will operate at 80HZ speed.

If no P-Code is specified, or the specified P-Code is out of range, then normal pressure will be used.

<!-- image -->

NOTE:

<!-- image -->

CAUTION:

<!-- image -->

NOTE:

<!-- image -->

NOTE:

If the machine is not equipped with a Variable Frequency Drive for the coolant pump, then the P-Code will have no effect.

## 8.1.8 M10 Engage 4th Axis Brake / M11 Release 4th Axis Brake

M10 applies the brake to the optional 4th axis and M11 releases the brake. The optional 4th axis brake is normally engaged, so the M10 command is only required when an M11 has released the brake.

## 8.1.9 M12 Engage 5th Axis Brake / M13 Release 5th Axis Brake

M12 applies the brake to the optional 5th axis and M13 releases the brake. The optional 5th axis brake is normally engaged, so the M12 command is only required when an M13 has released the brake.

## 8.1.10 M16 Tool Change

T - Tool number

This M16 behaves the same as M06 . However M06 is the preferred method for commanding tool changes.

## 8.1.11 M19 Orient Spindle (Optional P and R Values)

P - Number of degrees (0 - 360) R - Number of degrees with two decimal places (0.00 - 360.00).

M19 adjusts the spindle to a fixed position. The spindle only orients to the zero position without the optional M19 orient spindle feature. The orient spindle function allows P and R address codes. For example:

```
M19 P270. (orients the spindle to 270 degrees) ;
```

The R -value allows the programmer to specify up to two decimal places; for example:

```
M19 R123.45 (orients the spindle to 123.45 degrees) ;
```

<!-- image -->

## NOTE:

The range for M19 is 0 to 360 degrees. If a negative value if given, it will be ignored and spindle will orient to 0 degrees.

## 8.1.12 M21-M25 Optional User M Function with M-Fin

M21 through M25 are for user-defined relays. Each M-code closes one of the optional relays and  waits  for  an  external  M-Fin  signal. [RESET] stops  any  operation  waiting  for  a relay-activated accessory to finish. Also, refer to M51 - M55 and M61 - M65 .

Only one relay is switched at a time. A typical operation is to command a rotary product. The sequence is:

1. Run the machining portion of a CNC part program.
2. Stop CNC motion and command a relay.
3. Wait for a finish (M-Fin) signal from the equipment.
4. Continue the CNC part program.

The M-Fin connector is at P8 on the I/O PCB. Refer to the description below for a diagram and pinouts.

## M-code Relays

The M-code relays are in the lower-left corner of the I/O PCB.

These M-Code relays are sold separately (P/N 93-2889)

These relays can activate probes, auxiliary pumps, clamping devices, etc. Connect these auxiliary devices to the terminal strip for the individual relay. The terminal strip has positions for, Normally Open (NO), Normally Closed (NC), and Common (COM).

<!-- image -->

## F8.1: Main I/O PCB M-code Relays.

<!-- image -->

F8.2: M-Fin Circuit at P8 on the Main I/O PCB. Pin 3 is the M-Fin input and interacts with input number 18 in the control. Pin 1 is the M-Fin output and interacts with output number 4 on the control.

<!-- image -->

## Optional 8M-code Relays

You can purchase additional M-code relays in banks of 8.

Only the outputs on the I/O PCB are addressable with M21 - M25 , M51 - M55 , and M61 - M65 . If you use an 8M relay bank, you must use M29 , M59 , and M69 with P codes to activate the relays on the bank. The P codes for the first 8M bank are P90 - P97 .

## 8.1.13 M29 Set Output Relay with M-Fin

P - Discrete output relay from 0 to 255.

M29 turns on a relay, pauses the program, and waits for an external M-Fin signal. When the control receives the M-Fin signal, the relay turns off and the program continues. [RESET] stops any operation waiting for a relay-activated accessory to finish.

## 8.1.14 M30 Program End and Reset

M30 stops a program. It also stops the spindle, turns off the coolant (including TSC), and returns the program cursor to the start of the program.

<!-- image -->

NOTE:

As of software version 100.16.000.1041, M30 no longer cancels tool length offsets.

## 8.1.15 M31 Chip Conveyor Forward / M33 Chip Conveyor Stop

M31 starts the optional chip removal system (auger, multi-auger, or belt-style conveyor) in the forward direction; the direction that moves the chips out of the machine. You should run the chip conveyor intermittently, as this allows piles of larger chips to collect smaller chips and carry them out of the machine. You can set the chip conveyor duty cycle and run time with Settings 114 and 115.

The optional conveyor coolant washdown runs while the chip conveyor is on.

M33 stops conveyor motion.

## 8.1.16 M34 Coolant Increment / M35 Coolant Decrement

- P - M34 Pnn moves the P-Cool spigot to specific position away from home. M35 Pnn moves the P-Cool spigot to specific position towards home.

Example: The P-Cool spigot is at position P5 and you need to go to P10, you can use:

M34 P10

M35 P10

NOTE:

The P address value shall be keyed in without a decimal point.

<!-- image -->

or

## F8.3: P-Cool Spigot

<!-- image -->

CAUTION:

<!-- image -->

M34 moves the optional P-Cool spigot one position away from the current position (farther from home).

M35 moves the coolant spigot one position towards the home position.

Do not rotate the coolant spigot by hand. Serious motor damage will occur.

## 8.1.17 M36 Pallet Part Ready

Used on machines with pallet changers. M36 delays the pallet change until [PART READY] is  pushed.  A  pallet  change  occurs  after [PART READY] is  pushed  and  the  doors  are closed. For example:

```
% Onnnnn (program number) ; M36 (Flash 'Part Ready' light, wait until the button is pressed) ; M01 ; M50 (Perform pallet change after [PART READY] is pushed) ; (Part Program) ; M30 ; %
```

## 8.1.18 M39 Rotate Tool Turret

M39 is used to rotate the umbrella tool changer without a tool change. Program the tool pocket number ( Tn ) before M39 .

M06 is the command to change tools. M39 is normally useful for diagnostic purposes, or to recover from a tool changer crash.

<!-- image -->

## WARNING:

Either  original  pocket  should  be  restored  after  this  movement  or another empty pocket should be aligned with a tool change location. Otherwise, this will lead to a crash if the machine attempts to do a tool change with a filled pocket.

## 8.1.19 M41 Low Gear Override / M42 High Gear Override

On machines with a transmission, M41 holds the machine in low gear and M42 holds the machine in high gear. Normally, the spindle speed ( Snnnn )  determines which gear the transmission should be in.

Command M41 or M42 with the spindle speed before the spindle start command, M03 . For example:

```
% S1200 M41 ; M03 ; %
```

The gear state reverts to default at the next spindle speed ( Snnnn ) command. The spindle does not have to stop.

## 8.1.20 M46 Qn Pmm Jump to Line

Jump to line mm in the current program if pallet n is loaded, otherwise go to the next block.

## 8.1.21 M48 Validate That The Current Program is Appropriate for Loaded Pallet

Checks in the Pallet Schedule Table that the current program is assigned to the loaded pallet. If the current program is not in the list or the loaded pallet is incorrect for the program, an alarm is generated. M48 can be in a program listed in the PST, but never in a subroutine of the PST program. An alarm will occur if M48 is incorrectly nested.

## 8.1.22 M50 Pallet Change Sequence

* P - Pallet number

*indicates optional

This M-code is used to call a pallet change sequence. An M50 with a P command will call a specific pallet. M50 P3 will change to pallet 3, commonly used with Pallet Pool machines.

M50P0 is a special code used to extract a pallet without loading the next one. Use this code when you want to run a wash-down program or a spindle fan to clean the receiver before loading the next pallet while the machine is in pallet mode ( M199 ).

M96 Jump  If  No  Input  can  be  used  in  conjunction  with M50P0 to  skip  the  wash-down program if your are not in pallet mode. Refer to the M96 help text for more information on how to program a wash-down cycle to clean the receiver.

## 8.1.23 M51-M56 Turn On Built-In M-code Relay

The M51 through M56 codes are built-in M-Code relays. They activate one of the relays and leave it active. Use M61 - M66 to turn these off. [RESET] turns off all of these relays.

Refer to M21 through M26 on page 440 for details on the M-code relays with M-Fin.

## 8.1.24 M59 Turn On Output Relay

P - Discrete output relay number.

M59 turns on a discrete output relay. An example of its usage is M59 Pnnn , where nnn is the relay number being turned on.

When using Macros, M59 P90 does the same thing as using the optional macro command #12090=1 , except that it is processed at the end of the line of code.

| Built-In M-Code Relays   | 8M PCB Relay Bank 1 (JP1)   | 8M PCB Relay Bank 2 (JP2)   | 8M PCB Relay Bank 3 (JP3)   |
|--------------------------|-----------------------------|-----------------------------|-----------------------------|
| P114 (M21)               | P90                         | P103                        | P79                         |
| P115 (M22)               | P91                         | P104                        | P80                         |
| P116 (M23)               | P92                         | P105                        | P81                         |
| P113 (M24)               | P93                         | P106                        | P82                         |
| P112 (M25)               | P94                         | P107                        | P83                         |

| Built-In M-Code Relays   | 8M PCB Relay Bank 1 (JP1)   | 8M PCB Relay Bank 2 (JP2)   | 8M PCB Relay Bank 3 (JP3)   |
|--------------------------|-----------------------------|-----------------------------|-----------------------------|
| P4 (M26)                 | P95                         | P108                        | P84                         |
| -                        | P96                         | P109                        | P85                         |
| -                        | P97                         | P110                        | P86                         |

## 8.1.25 M61-M66 Turn Off Built-In M-code Relay

M61 through M65 are optional and turn off one of the relays. The M number corresponds to M51 through M55 that turned on the relay. [RESET] turns off all of these relays. Refer to M21 - M25 on page 440 for details on the M-code relays.

## 8.1.26 M69 Turn Off Output Relay

P - Discrete output relay number from 0 to 255.

M69 turns off a relay. An example of its usage is M69 P12nnn , where nnn is the number of the relay being turned off.

When using  Macros, M69  P12003 does  the  same  thing  as  using  the  optional  macro command #12003=0 , except that it is processed in the same order as axis motion.

| Built-In M-Code Relays   | 8M PCB Relay Bank 1 (JP1)   | 8M PCB Relay Bank 2 (JP2)   | 8M PCB Relay Bank 3 (JP3)   |
|--------------------------|-----------------------------|-----------------------------|-----------------------------|
| P114 (M21)               | P90                         | P103                        | P79                         |
| P115 (M22)               | P91                         | P104                        | P80                         |
| P116 (M23)               | P92                         | P105                        | P81                         |
| P113 (M24)               | P93                         | P106                        | P82                         |
| P112 (M25)               | P94                         | P107                        | P83                         |
| P4 (M26)                 | P95                         | P108                        | P84                         |
| -                        | P96                         | P109                        | P85                         |
| -                        | P97                         | P110                        | P86                         |

## 8.1.27 M70 Workholding Clamp / M71 Workholding Unclamp

Use M70 / M71 to clamp or unclamp the vises setup on the workholding page.

P - The P code defines the vise number. The range is P1 - 8.

- Q - The Q code enables or disables the vise unclamp check when commanding the spindle.

Q = 0 or not specified: Enable Unclamp Check. Q = 1: Disable Unclamp Check.

Example:

Example:

M70 P1 clamps Vise 1 and M71 P1 unclamps it.

M71 P1 Q1 disables the unclamp check for Vise 1.

The Vise Safety Check will be restored after Power Cycle, Program End(M02,M30),  End  of  Program,  Alarms,  Reset  is  pressed,  or workholding commands.

The system will default to Vise 1, if no P-Code is specified with M70 or M71 .

## NOTE:

<!-- image -->

<!-- image -->

NOTE:

<!-- image -->

NOTE:

This M code is not affected by the status of setting 389. See table below for more details.

| Setting 389   | M71 Q-Code   | Message on Cycle start   | Alarm 9938.001 when is commanded Spindle   |
|---------------|--------------|--------------------------|--------------------------------------------|
| Off           | Q0           | No                       | Yes                                        |
| Off           | Q1           | No                       | No                                         |
| On            | Q0           | Yes                      | Yes                                        |
| On            | Q1           | Yes                      | No                                         |

## 8.1.28 M73 Tool Air Blast (TAB) On / M74 Tool Air Blast Off

These M-codes control the Tool Air Blast (TAB) option. M73 turns on TAB, and M74 turns it off.

## 8.1.29 M75 Set G35 or G136 Reference Point

This code is used to set the reference point for G35 and G136 commands. It must be used after a probing function.

## 8.1.30 M78 Alarm if Skip Signal Found

M78 is used with a probe. An M78 generates an alarm if a programmed skip function ( G31 , G36 or G37 )  receives  a  signal  from  the  probe.  This  is  used  when  a  skip  signal  is  not expected, and may indicate a probe crash. This code can be placed on the same line as the skip G-code or in any block after.

## 8.1.31 M79 Alarm if Skip Signal Not Found

M79 is used with a probe. An M79 generates an alarm if a programmed skip function ( G31 , G36 , or G37 ) did not receive a signal from the probe. This is used when the lack of the skip signal means a probe positioning error. This code can be placed on the same line as the skip G-code or in any block after.

## F8.4: Probe Positioning Error: [1] Signal Found. [2] Signal not Found.

<!-- image -->

## 8.1.32 M80 Auto Door Open / M81 Auto Door Close

M80 opens the Auto Door and M81 closes it. The control pendant beeps while the door is in motion.

<!-- image -->

NOTE:

The M-codes work only while the machine receives a cell-safe signal from a robot or if it has a light curtain installed. For more information refer to Robot Integration Aid - NGC reference document.

## 8.1.33 M82 Tool Unclamp

M82 is used to release the tool from the spindle. It is used as a maintenance/test function only. Tool changes should be done using an M06 .

## 8.1.34 M83 Auto Air Gun On / M84 Auto Air Gun Off

M83 turns the Auto Air Gun (AAG) option on, and M84 turns it off. M83 with a Pnnn argument (where nnn is in milliseconds) turns the AAG on for the specified time, then turns it off. You can also press [SHIFT] and then [COOLANT] to turn on the AAG manually.

## 8.1.35 M86 Tool Clamp

M86 clamps a tool into the spindle. It is used as a maintenance/test function only. Tool changes should be done using an M06 .

## 8.1.36 M88 Through-Spindle Coolant On / M89 Through-Spindle Coolant Off

M88 turns on through-spindle coolant (TSC), and M89 turns off TSC.

The control automatically stops the spindle before it executes M88 or M89 . The control does not automatically start the spindle again after M89 . If your program continues with the same tool  after  an M89 command, be sure  to  add  a  spindle  speed  command  before  further motion.

You must use proper tooling, with a through-hole, when you use the TSC system. Failure to use proper tooling can flood the spindle head with coolant and void the warranty.

## Sample Program

The M88 command should be before the spindle speed command. If you  command M88 after  the  spindle  speed  command,  the  spindle starts, then stops, turns on TSC, and then starts again.

```
% T1 M6 (TSC Coolant Through Drill) ; G90 G54 G00 X0 Y0 ; G43 H01 Z.5 ; M88 (Turn TSC on) ; S4400 M3 ; G81 Z-2.25 F44. R.1 ; M89 G80 (Turn TSC off) ; G91 G28 Z0 ; G90 ; M30 ;
```

<!-- image -->

CAUTION:

<!-- image -->

NOTE:

%

## 8.1.37 M90 Fixture Clamp Input ON / M91 Fixture Clamp Input OFF

The M90 M-code enables fixture clamp input monitoring when setting 276 has a valid input number greater than 0. If variable #709 = 1 and the spindle is commanded on, the machine will generate alarm: 973 Fixture Clamp Incomplete.

The M91 M-code disables the fixture clamp input monitoring.

## 8.1.38 M95 Sleep Mode

Sleep mode is a long dwell. The format of the M95 command is: M95 (hh:mm) .

The comment immediately following M95 must contain the duration, in hours and minutes, that you want the machine to sleep. For example, if the current time were 6 p.m. and you want the machine to sleep until 6:30 a.m. the next day, command M95  (12:30) .  The line(s) after M95 should be axis moves and spindle warm-up commands.

## 8.1.39 M96 Jump If No Input

- P - Program block to go to when conditional test is met
- Q - Discrete input variable to test (0 to 255)
- R - A certain mechanism mode. R1 is for PP mode and R2 is for APL mode.

M96 is used to test a discrete input for 0 (off) and certain mechanisms status. Using the M96 with  the Q code  is  useful  for  checking  the  status  of  automatic  work  holding  or  other accessories that generate a signal for the control. The Q value must be in the range 0 to 255, which corresponds to the inputs found on the diagnostic display I/O tab. When this program block is executed and the input signal specified by Q has a value of 0, the program block Pnnnn is performed (the Nnnnn that matches the Pnnnn line must be in the same program).

The M96 sample program uses input #18 M-FIN INPUT

## Example:

```
% O00096(SAMPLE PROGRAM FOR M96 JUMP IF NO INPUT) ; (IF M-FIN INPUT #18 IS EQUAL TO 1 THE PROGRAM WILL JUMP TO N100) ; (AFTER JUMPING TO N100 THE CONTROL ALARMS OUT WITH A MESSAGE) ; (M-FIN INPUT=1) ; (IF M-FIN INPUT #18 IS EQUAL TO 0 THE PROGRAM JUMPS TO N10) ; (AFTER JUMPING TO N10 THE CONTROL DWELLS FOR 1 SECOND THEN
```

```
JUMPS TO N5) ; (THE PROGRAM CONTINUES THIS LOOP UNTIL INPUT #18 IS EQUAL TO 1) ; G103 P1 ; ... ; ... ; N5 M96 P10 Q18(JUMP TO N10 IF M-FIN INPUT #18 = 0) ; ... ; M99 P100(JUMP TO N100) ; N10 ; G04 P1. (DWELL FOR 1 SECOND) ; M99 P5 (JUMP TO N5) ; ... ; N100 ; #3000= 10(M-FIN INPUT=1) ; M30 ; ... ; %
```

Using the M96 with the R code allows user to run a G/M-code program after M96 R1 which will check if the pallet mode is ON to perform a certain function for example a wash cycle program. This is useful on a pallet pool machine if you want to clean the receiver before loading the next pallet while the machine is in pallet mode.

The following program is an example on how to use the M96 with a R code to run a wash cycle if the machine is in pallet mode.

```
O00097(SAMPLE PROGRAM FOR M96 R1 JUMP IF PP MODE IS NOT ON); ; ; (MACHINE OPERATIONS); ; ; N5 M96 P100 R1 (CHECK PALLET SCHEDULE - JUMP TO N100 IF NOT IN PALLET MODE); ; M50P0 (UNLOAD PALLET FROM MACHINE); ; ; (G/M CODE BLOCKS FOR PALLET POOL WASH CYCLE - AS EXAMPLE); ; ; N100M199 (LOAD NEXT PALLET IF IN PALLET MODE, OTHERWISE M30); %
```

## 8.1.40 M97 Local Subprogram Call

- P - Program line number to go to when conditional test is met
- L - Repeats subprogram call (1-99) times.

M97 is used to call a subprogram referenced by a line number ( N ) within the same program. A code is required and must match a line number within the same program. This is useful for  simple  subprograms  within  a  program;  does  not  require  a  separate  program.  The subprogram must end with an M99 . Lnn code in the M97 block repeats the subprogram call nn times.

The subprogram is within the body of the main program, placed after the M30 .

## M97 Example:

```
% O00001 ; M97 P100 L4 (CALLS N100 SUBPROGRAM) ; M30 ; N100 (SUBPROGRAM) ; ; M00 ; M99 (RETURNS TO MAIN PROGRAM) ; %
```

## 8.1.41 M98 Subprogram Call

- P - The subprogram number to run
- L - Repeats the subprogram call (1-99) times.

(&lt;PATH&gt;) - The Subprogram's directory path

M98 calls a  subprogram in the format M98  Pnnnn ,  where Pnnnn is  the  number  of the program to call, or M98 (&lt;path&gt;/Onnnnn) , where &lt;path&gt; is the device path that leads to the subprogram.

NOTE:

The file path is case sensitive.

The subprogram must contain an M99 to return to the main program. You can add an Lnn count to the M98 block M98 to call the subprogram nn times before continuing to the next block.

<!-- image -->

NOTE:

<!-- image -->

When your program calls an M98 subprogram, the control looks for the subprogram in the main program's directory. If the control cannot find the subprogram, it then looks in the location specified in Setting 251. Refer to page 151 for more information. An alarm occurs if the control cannot find the subprogram.

## M98 Example:

The subprogram is a separate program ( O00100 ) from the main program ( O00002 ).

```
% O00002 (PROGRAM NUMBER CALL); M98 P100 L4 (CALLS O00100 SUB 4 TIMES) ; M30 ; % % O00100 (SUBPROGRAM); M00 ; M99 (RETURN TO MAIN PROGRAM) ; % % O00002 (PATH CALL); M98 (USB0/O00001.nc) L4 (CALLS O00100 SUB 4 TIMES) ; M30 ; % % O00100 (SUBPROGRAM); M00 ; M99 (RETURN TO MAIN PROGRAM) ; %
```

## 8.1.42 M99 Subprogram Return or Loop

- P - Program line number to go to when conditional test is met

M99 has three main uses:

- M99 is used at the end of a subprogram, local subprogram, or macro to return back to the main program.
- An M99 Pnn jumps the program to the corresponding Nnn in the program.
- An M99 in the main program causes the program to loop back to the beginning and execute until [RESET] is pressed.

|                  | Haas                   |
|------------------|------------------------|
| calling program: | O0001 ;                |
|                  | ...                    |
|                  | N50 M98 P2 ;           |
|                  | N51 M99 P100 ;         |
|                  | ...                    |
|                  | N100 (continue here) ; |
|                  | ...                    |
|                  | M30 ;                  |
| subprogram:      | O0002 ;                |
|                  | M99 ;                  |

M99 jumps to a specific block with or with out the macro option.

## 8.1.43 M104 / M105 Probe Arm Extend/Retract (Optional)

The optional tool setting probe arm is extended and retracted using these M-codes.

## 8.1.44 M109 Interactive User Input

- P - A number in the range (500-549 or 10500-10549) representing the macro variable of the same name to be used for storing the user input value. M109 can be used to introduce a user input prompt which will pause program and prompt the user for input.

<!-- image -->

NOTE:

You must use a P code to specify macro variable in the range 500-549 or 10500 through 10549.

The P code will be used to store the value provided by the user input into the corresponding macro number.The program can check for any character that can be entered from the keyboard by comparing with the decimal equivalent of the ASCII character (G47, Text Engraving, has a list of ASCII characters).Any comment on the same block as M109 will act  as  the  prompt  if  provided.The  comment  block  may  itself  contain  a  macro  number reference with #macro[wf] format where macro is the macro number representation and wf represents the whole and fractional parts precision respectively

M109 lets a G-code program place a short prompt (message) on the screen. You must use a P code to specify macro variable in the range 500-549 or 10500 through 10549. The program can check for any character that can be entered from the keyboard by comparing with the decimal equivalent of the ASCII character ( G47 , Text Engraving, has a list of ASCII characters).

Macro Variables 540-599 and 10549-10599 are reserved for the WIPS (probe)  option.  If  your  machine  is  equipped  with  WIPS  only  use P500-539 or P10500-10599.

The following sample program asks the user a Y es or N o question, then waits for either a Y or an N to be entered. All other characters are ignored.

```
% O61091 (M109 INTERACTIVE USER INPUT) ; (This program has no axis movement) ; N1 #10501= 0. (Clear the variable) ; N5 M109 P10501 (Sleep 1 min?) ; IF [ #10501 EQ 0. ] GOTO5 (Wait for a key) ; IF [ #10501 EQ 89. ] GOTO10 (Y) ; IF [ #10501 EQ 78. ] GOTO20 (N) ; GOTO1 (Keep checking) ; N10 (A Y was entered) ; M95 (00:01) ; GOTO30 ; N20 (An N was entered) ; G04 P1. (Do nothing for 1 second) ; N30 (Stop) ; M30 ; %
```

The following sample program asks the user to select a number, then wait for a 1 , 2 , 3 , 4 or a 5 to be entered; all other characters are ignored.

```
% O00065 (M109 INTERACTIVE USER INPUT 2) ; (This program has no axis movement) ; N1 #10501= 0 (Clear Variable #10501) ; (Variable #10501 will be checked) ; (Operator enters one of the following selections); N5 M109 P10501 (1,2,3,4,5) ; IF [ #10501 EQ 0 ] GOTO5 ; (Wait for keyboard entry loop until entry) ; (Decimal equivalent from 49-53 represent 1-5) ; IF [ #10501 EQ 49 ] GOTO10 (1 was entered go to N10) ; IF [ #10501 EQ 50 ] GOTO20 (2 was entered go to N20) ; IF [ #10501 EQ 51 ] GOTO30 (3 was entered go to N30) ; IF [ #10501 EQ 52 ] GOTO40 (4 was entered go to N40) ; IF [ #10501 EQ 53 ] GOTO50 (5 was entered go to N50) ; GOTO1 (Keep checking for user input loop until found) ; N10 ; (If 1 was entered run this sub-routine) ; (Go to sleep for 10 minutes) ; #3006= 25 (Cycle start sleeps for 10 minutes) ; M95 (00:10) ; GOTO100 ; N20 ; (If 2 was entered run this sub routine) ; (Programmed message) ; #3006= 25 (Programmed message cycle start) ; GOTO100 ; N30 ; (If 3 was entered run this sub routine) ; (Run sub program 20) ; #3006= 25 (Cycle start program 20 will run) ; G65 P20 (Call sub-program 20) ; GOTO100 ; N40 ; (If 4 was entered run this sub routine) ; (Run sub program 22) ; #3006= 25 (Cycle start program 22 will be run) ; M98 P22 (Call sub program 22) ; GOTO100 ; N50 ; (If 5 was entered run this sub-routine) ; (Programmed message) ; #3006= 25 (Reset or cycle start will turn power off) ; #12006= 1 ; N100 ; M30 (End Program);
```

<!-- image -->

NOTE:

%

## 8.1.45 M116 Vise Air Chips Blast On / M117 Vise Air Chips Blast Off

M116 turns the Vise Air Chips Blast option on, and M117 turns it off.

## 8.1.46 M130 Display Media / M131 Cancel Display Media

M130 Lets you display video and still images during program execution. Some examples of how you can use this feature are:

- Providing visual cues or work instructions during program operation
- Providing images to aid part inspection at certain points in a program
- Demonstrating procedures with video

The correct command format is M130(file.xxx) , where file.xxx is the name of the file, plus the path, if necessary.

The file path is case sensitive.

<!-- image -->

## NOTE:

<!-- image -->

NOTE:

You can also add a second comment in parentheses to appear as a comment at the top of the media window.

M130 uses the subprogram search settings, Settings 251 and 252 in the same way that M98 does. You can also use the Insert Media File command  in  the  editor  to  easily  insert  an M130 code  that includes the filepath. Refer to page 190 for more information.

Permitted file formats are MP4, MOV, PNG, and JPEG.

For the fastest loading times, use files with pixel dimensions divisible by 8 (most unedited digital images have these dimensions by default), and a maximum pixel size of 1920 x 1080.

Your media appears in the Media tab under Current Commands. The media displays until the next M130 displays a different file, or M131 clears the media tab contents.

## F8.5: Media Display Example - Work Instruction during a Program

<!-- image -->

## 8.1.47 M138 / M139 Spindle Speed Variation On/Off

Spindle Speed Variation (SSV) lets you specify a range within which the spindle speed continuously  varies.  This  is  helpful  in  suppressing  tool  chatter,  which  can  lead  to  an undesirable part finish and/or damage to the cutting tool. The control varies the spindle speed based on Settings 165 and 166. For example, to vary spindle speed +/- 100 RPM from its current commanded speed with a duty cycle of 1 seconds, set Setting 165 to 100 and Setting 166 to 1.

The variation  you  use  depends  on  the  material,  tooling,  and  the  characteristics  of  you application, but 100 RPM over 1 second is a good starting point.

You can override the values of settings 165 and 166 using P and E address codes when used with M138. Where P is SSV Variation (RPM) and E is the SSV Cycle (Sec). See example below:

M138 P500 E1.5 (Turn SSV On, vary the speed by 500 RPM, cycle every 1.5 seconds);

M138 P500(Turn SSV on, vary the speed by 500, cycle based on setting 166);

M138 E1.5 (Turn SSV on, vary the speed by setting 165, cycle every 1.5 seconds);

<!-- image -->

NOTE:

If you have an M138 Enn on one line and a G187 Enn on another line, the E codes would be unique to the line they are on. The Enn Code for the  G187  would  apply  to  G187 only  and  not  affect  the active  SSV behavior.

M138 is independent of spindle commands; once commanded, it is active even when the spindle is not turning. Also,  M138 remains active until canceled  with M139, or at M30, Reset, or Emergency Stop.

## 8.1.48 M140 MQL On Continuous Mode / M141 MQL On Single Squirt Mode / M142 Stop MQL

M140 turns the Minimum Quantity Lubrication (MQL) option on, and M142 turns it off. M141 turns on the MQL on for the specified time, then turns it off.

## 8.1.49 M158 Mist Condenser On / M159 Mist Condenser Off

M158 turns on the Mist Condenser, and M159 turns off the Mist Condenser.

<!-- image -->

NOTE:

<!-- image -->

NOTE:

<!-- image -->

NOTE:

The mist condenser will run continuously if a program is running with axis motion.

An M158 in MDI will activate the mist condenser for 10 seconds, after this  the  mist  condenser  will  turn  OFF.  If  continuous  operation  is required the program will require feed motion of at least one axis.

If you want the mist condenser to remain ON, then go to CURRENT COMMANDS&gt;DEVICES&gt;MECHANISMS&gt;MIST  CONDENSER  and press [F2] to turn it on

## 8.1.50 M160 Cancel Active PulseJet

Use M160 to cancel an active PulseJet M-code.

## 8.1.51 M161 Pulse Jet Continuous Mode

* P - Pnn is the interval at which oil pulses occur (Min = 1 / Max = 99 seconds). For example P3 means there will be a pulse every 3 seconds.

*indicates optional

M161 will turn PulseJet on whenever a feed move is active in a program.

Refer to setting '369 - PulseJet Injection Cycle Time' on page 518 to set the PulseJet oil flow duty cycle.

## 8.1.52 M162 PulseJet Single Event Mode

* P - Pnn is how many pulses (Min= 1 / Max= 99 squirts).

*indicates optional

M162 will turn on PulseJet for a defined number of pulses. Best used for drilling and tapping or to manually lubricate a tool.

M162 is a non-blocking code. Anything after the code will be executed immediately.

NOTE:

<!-- image -->

Refer to setting '370 - PulseJet Single Squirt Count' on page 518 to set the squirt count.

## 8.1.53 M163 PulseJet Modal Mode

* P - Pnn is how many pulses for each hole (Min= 1 / Max = 99).

*indicates optional

M163 activates PulseJet to turn on during any canned drill, tap or bore cycles.

When a canned cycle is canceled by a method such as a G80 or a Feed. It will also cancel the M163 modal command.

## M163 Program Example:

```
G90 G54 G00 G28; S100 M03; M163 P3; G81 F12. R-1. Z-2.; X-1.; X-2.; G80;
```

<!-- image -->

NOTE:

<!-- image -->

NOTE:

```
G00 X-3.; G84 F12. R-1. Z-2.; X-4.; G80; M30;
```

The PulseJet M163 P3 in this program is canceled by G80 and will only run the first cycle.

Refer to setting '370 - PulseJet Single Squirt Count' on page 518 to set the squirt count.

## 8.1.54 M180 / M181 Automatic Window Open / Close

M180 opens the Auto Window and M181 closes it.

The M-codes work only while the machine receives a cell-safe signal from a robot or if it has a light curtain installed. For more information refer to Robot Integration Aid - NGC reference document.

NOTE:

<!-- image -->

## 8.1.55 M183 Auto Air Hole Blast On / M184 Auto Air Hole Blast Off

M183 turns the Hole Blast option on, and M184 turns it off. M183 with a Pnnn argument (where nnn is in seconds) turns the Hole Blast on for the specified time, then turns it off.

```
M183 P2. ;
```

## NOTE:

This will turn the Hole Blaster on for 2 seconds.

The  Hole  Blast  can  also  be  turned  on/off  by  going  to  the  Mechanisms  tab.  Current Commands&gt; Devices&gt; Mechanisms.

<!-- image -->

## 8.1.56 M199 Pallet / Part Load or Program End

M199 takes the place of an M30 or M99 at the end of a program. When running in Memory or MDI mode, pressing Cycle Start to run the program, the M199 will behave the same as an M30 . It will stop and rewind the program back to the beginning. While running in Pallet Change mode, pressing INSERT while on the Pallet Schedule Table to run a program, the M199 behaves the same as an M50 + M99 . It will end the program, get the next scheduled pallet  and  associated  program,  then  continue  to  run  until  all  scheduled  pallets  are completed.

## 8.1.57 M300 - APL/Robot Custom Sequence

The M300 code is used to call APL or Robot Custom Sequence programs. To call a specific program use the P code followed by the alias code, found in the APL custom sequence tab.

M300 Pn Q0 Plays the sequence in the background to the program.

M300 Pn R0 Plays the Sequence in reverse.

M300  Pn  R0 ignores  all  non-robot  related  commands  when  the motion file is ran in reverse. Example of some commands ignored: Machine Dwells, Auto Door commands, Workholding commands, and Spindle Orients.

<!-- image -->

NOTE: