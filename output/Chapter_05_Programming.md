## Chapter 5: Programming

## 5.1 Create / Select Programs for Editing

You  use  the  Device  Manager  ( [LIST  PROGRAM] )  to  create  and  select  programs  for editing.  Refer  to  page 113 to  create  a  new  program.  Refer  to  page 115 to  choose  an existing program to edit.

## 5.2 Program Edit Modes

The Haas control has (2) program edit modes: The program editor or manual data input (MDI). You use the program editor to make changes to numbered programs stored in an attached memory device (machine memory, USB, or net share). You use MDI mode to command the machine without a formal program.

The Haas control screen has (2) program edit panes: The Active Program / MDI pane, and the Program Generation pane. The Active Program / MDI pane is on the left side of the screen in all display modes. The Program Generation pane appears only in EDIT mode.

## F5.1: Example Edit Panes. [1] Active Program / MDI Pane, [2] Program Edit Pane, [3] Clipboard Pane

<!-- image -->

## 5.3 Basic Program Editing

This section describes the basic program editing functions. These functions are available when you edit a program.

1. To write a program, or make changes to a program:
- a. To edit a program in MDI, press [MDI] . This is EDIT:MDI mode. The program is displayed on the Active pane.
- b. To edit a numbered program, select it in the Device Manager ( [LIST PROGRAM] ), then press [EDIT] . This is EDIT:EDIT mode. The program is displayed in the Program Generation pane.
2. To highlight code:
- a. Use the cursor arrow keys or the jog handle to move the highlight cursor through the program.
- b. You can interact with single pieces of code or text (cursor highlighting), blocks of code, or multiple blocks of code (block selection). Refer to the Block Selection section for more information.
3. To add code to the program:
- a. Highlight the code block you want the new code to follow.
- b. Type the new code.
- c. Press [INSERT] . Your new code appears after the block you highlighted.
4. To replace code:
- a. Highlight the code you want to replace.
- b. Type the code you want to replace the highlighted code with.
- c. Press [ALTER] . Your new code takes the place of the code you highlighted.
5. To remove characters or commands:
- a. Highlight the text you want to delete.
- b. Press [DELETE] . The text that you highlighted is removed from the program.
6. Press [UNDO] to reverse up to the last (40) changes.

<!-- image -->

## NOTE:

<!-- image -->

## NOTE:

You cannot use [UNDO] to reverse changes that you made if you exit EDIT:EDIT mode.

In EDIT:EDIT mode, the control does not save the program as you edit. Press [MEMORY] to save the program and load it into the Active Program pane.

## 5.4 Block Selection

When you edit a program, you can select single or multiple blocks of code. You can then copy and paste, delete, or move those blocks in one step.

## To select a block:

1. Use the cursor arrow keys to move the highlight cursor to the first or last block in your selection.

You can start a selection at the top block or the bottom block, and then move up or down as appropriate to complete your selection.

You cannot include the program name block in your selection. The control gives the message GUARDED CODE .

2. Press [F2] to start your selection.
3. Use the cursor arrow keys or the jog handle to expand the selection.
4. Press [F2] to complete the selection.

## 5.5 Actions with a Block Selection

After you make a text selection, you can copy and paste it, move it, or delete it.

<!-- image -->

## NOTE:

These instructions assume you have already made a block selection as described in the Block Selection section.

<!-- image -->

## NOTE:

<!-- image -->

## NOTE:

<!-- image -->

<!-- image -->

These  are  actions  available  in  MDI  and  the  Program  Editor.  You cannot use [UNDO] to reverse these actions.

1. To copy and paste the selection:
- a. Move the cursor to the location where you want to put a copy of the text.
- b. Press [ENTER] .

The control puts a copy of the selection on the next line after the cursor location.

The control does not copy the text to the clipboard when you use this function.

2. To move the selection:
- a. Move the cursor to the location where you want to move the text.
- b. Press [ALTER] .

The control removes the text from its current location and puts it in the line after the current line.

3. Press [DELETE] to delete the selection.

## 5.6 Manual Data Input (MDI)

Manual  Data  Input  (MDI)  lets  you  command  automatic  CNC  moves  without  a  formal program. Your input stays on the MDI input page until you delete it.

## F5.2: MDI Input Page Example

<!-- image -->

1. Press [MDI] to enter MDI mode.
2. Type your program commands in the window. Press [CYCLE START] to execute the commands.

3. If you want to save the program you created in MDI as a numbered program:
- a. Press [HOME] to put the cursor at the beginning of the program.
- b. Type a new program number. Program numbers must follow the standard program number format ( Onnnnn ).
- c. Press [ALTER] .
- d. In the RENAME pop-up window, you can type a filename and file title for the program. Only the O number is required.
- e. Press [ENTER] to save the program to memory.
4. Press [ERASE PROGRAM] to delete everything from the MDI input page.

## 5.7 Program Editor

The Program Editor is a full-featured editing environment with access to powerful functions in an easy-to-use pull-down menu. You use the Program Editor for normal editing.

Press [EDIT] to enter edit mode and use the Program Editor.

## F5.3: Example Program Editor Screen. [1] Main Program Display, [2] Menu Bar, [3] Clipboard

<!-- image -->

## 5.8 Program Editor Pull-Down Menu

The Program Editor uses a pull-down menu to give you easy access to editor functions in (5) categories: File , Edit , Search , and Modify . This section describes the categories and the choices you can make when you select them.

To use the pull-down menu:

1. Press [EDIT] to start the Program Editor.
2. Press [F1] to access the pull-down menu.

The menu opens for the last category you used. If you have not yet used the pull-down menu, the File menu opens by default.

3. Use the [LEFT] and [RIGHT] cursor arrow keys to highlight a category. When you highlight a category, the menu appears below the category name.
4. Use the [UP] and [DOWN] cursor arrow keys to select an option inside of the current category.
5. Press [ENTER] to execute the command.

Some menu commands require further  input  or  confirmation.  In  these  cases,  an  input window or confirmation pop-up appears on the screen. Type your input in the field(s) where applicable, and then press [ENTER] to confirm the action or [UNDO] to close the popup and cancel the action.

## 5.9 File Menu

The File menu has these options:

- New :  Creates  a  new  program.  In  the  pop-up  menu  fields,  type  an  O  number (required), a filename (optional), and a file title (optional). For more information about this menu, refer to 'Create a New Program' in the Operation section of this manual.
- Set  To  Run :  Saves the program and puts it in the active program pane on the left-hand side of the screen. You can also press [MEMORY] to use this function.
- Save :  Saves the program. The program's filename and path change from red to black to show that the changes are saved.
- Save As : You can save the file under any filename. The program's new filename and path will change from red to black to show that the changes are saved.
- Discard  Changes :  Reverts  any  changes  you've  made  since  the  file  was  last saved.

## 5.10 Edit Menu

The Edit menu has these options:

- Undo : Reverses the last edit operation, up to the last (40) edit operations. You can also press [UNDO] to use this function.

- Redo : Reverses the last undo operation, up to the last (40) undo operations.
- Cut Selection To Clipboard : Removes the selected lines of code from the program and puts them in the clipboard. Refer to 'Block Selection' to learn how to make a selection.
- Copy Selection To Clipboard : Puts the selected lines of code in the clipboard. This operation does not remove the original selection from the program.
- Paste From Clipboard : Puts a copy of the clipboard contents below the current line. This does not remove the clipboard contents.
- Insert File Path (M98) : Lets you select a file from a directory and creates the path with the M98.
- Insert Media File (M130) : Lets you select a media file from a directory and creates the path with the M130.
- Insert Media File ($FILE) : Lets you select a media file from a directory and creates the path with the $FILE tag.
- Special Symbols : Inserts a special symbol.

## 5.11 Search Menu

The Search menu gives you access to the Find And Replace Text function. This function lets you quickly find code in the program and optionally replace it. To use it:

<!-- image -->

NOTE:

This function searches for program code, not text. You cannot use this function to find text strings (like comments).

F5.4: Find and Replace Menu Example: [1] Text to Find, [2] Replacement Text, [3] Search Direction, [4] Find Option, [5] Replace Option, [6] Find and Replace Option, [7] Replace all Option

<!-- image -->

<!-- image -->

## Specify Your Find / Replace Code

1. Press [ENTER] in the editor pull-down menu to open the Find And Replace Text menu. Use the cursor arrow keys to move between the fields in the menu.
2. In the Find field, Type the code you want to search for.
3. If you want to replace some or all of the found code, type the replacement code in the Replace field.
4. Use the [LEFT] and [RIGHT] cursor arrow keys to choose the search direction. Forward searches the program below the cursor position, Backward searches the program above the cursor position.

After you specify at least the code that you want to search for and the direction you want to search, press the function key for the search mode that you want to use:

## Find Code ( [F1] )

Press [F1] to find the search term.

The  control  searches  the  program  in  the  specified  direction  and  highlights  the  first occurrence of the search term. Each time you press [F1] , the control searches for the next occurrence of the search term, in the search direction that you specified, until it reaches the end of the program.

## Replace Code ( [F2] )

After the search function finds an occurrence of your search term, you can press [F2] to replace that code with the contents of the Replace field.

If you press [F2] with no text in the Replace field, the control deletes that occurrence of your search term.

## Find and Replace ( [F3] )

Press [F3] instead of [F1] to start the find and replace operation. For each occurrence of your search term, press [F3] if you want to replace it with the text in the Replace field.

## Replace All ( [F4] )

Press [F4] to replace all of the search term occurrences in (1) step. You cannot undo this.

## 5.12 MODIFY Menu

The Modify menu has commands that let you make quick changes to an entire program, or to selected lines within a program.

<!-- image -->

You cannot use [UNDO] to reverse Modify operations. The operations also automatically save the program. If you are not sure you want to keep the changes that you make, be sure to save a copy of the original program.

- Remove All Line Numbers : Automatically removes all N-code line numbers from the program or the selected program blocks.
- Renumber All Lines : Automatically adds N-code line numbers to the program or the selected program blocks. Enter the line number you want to start with and the increment to use between line numbers, then press [ENTER] to continue or press [UNDO] to cancel and to return to the editor.
- Reverse + And - Signs : Changes positive values for selected address codes to negative, or negative values to positive. Press the letter key for the address codes that you want to reverse to toggle selections in the pop-up menu. Press [ENTER] to execute the command or [CANCEL] to return to the editor.

## F5.5: Reverse Plus and Minus Signs Menu

<!-- image -->

- Reverse X And Y : Changes the X address codes in the program to Y address codes, and changes Y address codes to X address codes.

## 5.13 Editor View Settings

With in the editor menu there are three groups of view settings: text color, clipboard, and magnify &amp; highlight.

These options can be accessed by pressing [F1] and then navigating to the View menu.

## F5.6: Example Editor View Settings

<!-- image -->

Text Color: This setting has two states: Haas Colors and Black and White. Black and White will have black text on a white background. While Haas Colors will make specific parts of text colored differently.

1. G and M codes: Blue. G codes are dark blue while M codes are light blue
2. Comments: Gray and italicized.
3. Operators: Green. (If, While, SIN, etc.)
4. All other text: Black

## F5.7: Editor page

<!-- image -->

With magnify off the text will not change when the line is selected [1]. With magnify on the text of the line that is selected will be bigger [2]. With Magnify &amp; Highlight on the text of the line that is selected will be bigger and the full line will be highlighted [3].

## F5.8: Magnify &amp; Highligh screen

```
1 2 3 N10; (FACE TOP .005 DEEP) ; T1 M06 G00G90 G54 X2. Y1.5 S [10000*#102 JM03 G43H01 Z0.1 M08 G01 Z-0.015 F[200.*#102]; X-8. : N10; (FACE TOP .005 DEEP) ; T1 M06 G00G90 G54 X2. Y1.5S[10000*#102]M03 ; G43 H01 Z0.1 M08 ; G01 Z-0.015 F [200.*#102]; X-8. ; N10; (FACE TOP .005 DEEP) ; T1 M06 G00 G90 G54 X2. Y1.5 S [ 10000 * #102 ] M03 ; G43 H01 Z0.1 M08 G01 Z-0.015 F [200.*#102]; X-8. ;
```

The hide clipboard view setting allows the clipboard box at the bottom of the editor to be hidden.

## F5.9: Hide Clipboard screen

<!-- image -->

## 5.14 G Code and M Code Quick Create

The Quick Create feature allows the user to quickly insert G or M codes into a program they are  editing.  While  using the  touch  screen  they  can  press [QUICK CREATE] [1]  in  the bottom right or press [F1] [2], select Edit [3], and Quick Create [4] if the user does not want to use the touch screen.

## F5.10: Example Quick create

<!-- image -->

## F5.11: Select G or M codes [1].

<!-- image -->

## F5.12: Use the arrow keys or the touch screen to select the desired G or M code [1].

<!-- image -->

## F5.13: Use the arrow keys or the touch screen to select the desired G or M code [1].

<!-- image -->

F5.14: Fill out any address codes that are either optional or required [1] and press [ENTER]

<!-- image -->

## F5.15: The code will then be inserted into the program.

<!-- image -->

## 5.15 G and M Code Balloon Help

If a G or M code is highlighted a balloon will pop up with a part of the help text for that code. This feature can be enabled or disabled by going to MDI -&gt; View -&gt; G/M code Help. There are three modes this feature can be in Disabled, 3 seconds, or 5 seconds. Disabled turns this feature off so no balloon will show up. 3 seconds will mean the G or M code will need to be highlighted for 3 seconds before the balloon pops up and 5 seconds extends the delay to 5 seconds.

## 5.16 Basic Programming

A typical CNC program has (3) parts:

1. Preparation: This portion of the program selects the work and tool offsets, selects the cutting tool, turns on the coolant, sets spindle speed, and selects absolute or incremental positioning for axis motion.
2. Cutting: This portion of the program defines the tool path and feed rate for the cutting operation.
3. Completion: This portion of the program moves the spindle out of the way, turns off the spindle, turns off the coolant, and moves the table to a position from where the part can be unloaded and inspected.

This is a basic program that makes a 0.100" (2.54 mm) deep cut with Tool 1 in a piece of material along a straight line path from X = 0.0, Y = 0.0 to X = - 4.0, Y = - 4.0.

<!-- image -->

## NOTE:

A program block can contain more than one G-code, as long as those G-codes are from different  groups.  You  cannot  place  two  G-codes from  the  same  group  in  a  program  block.  Also  note  that  only  one M-code per block is allowed.

```
% O40001 (Basic program) ; (G54 X0 Y0 is top right corner of part) ; (Z0 is on top of the part) ; (T1 is a 1/2" end mill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G17 G40 G49 G54 (Safe startup) ; X0 Y0 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 F20. Z-0.1 (Feed to cutting depth) ; X-4. Y-4. (linear motion) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 5.17 Preparation

These are the preparation code blocks in the sample program O40001:

| Preparation Code Block   | Description                                                                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| %                        | Denotes the beginning of a program written in a text editor.                                                                                    |
| O40001 (Basic program) ; | O40001 is the name of the program. Program naming convention follows the Onnnnn format: The letter 'O', or 'o' is followed by a 5-digit number. |

| Preparation Code Block                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (G54 X0 Y0 is top right corner of part) ; | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| (Z0 is on top of the part) ;              | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| (T1 is a 1/2" end mill) ;                 | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| (BEGIN PREPARATION BLOCKS) ;              | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| T1 M06 (Select tool 1) ;                  | Selects tool T1 to be used. M06 commands the tool changer to load Tool 1 ( T1 ) into the spindle.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| G00 G90 G17 G40 G49 G54 (Safe startup) ;  | This is referred to as a safe startup line. It is good machining practice to place this block of code after every tool change. G00 defines axis movement following it to be completed in Rapid Motion mode. G90 defines axis movements following it to be completed in absolute mode (refer to page 205 for more information). G17 defines the cutting plane as the XY plane. G40 cancels Cutter Compensation. G49 cancels tool length compensation. G54 defines the coordinate system to be centered on the Work Offset stored in G54 on the Offset display. |
| X0 Y0 (Rapid to 1st position) ;           | X0 Y0 commands the table to move to the position X = 0.0 and Y = 0.0 in the G54 coordinate system.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| S1000 M03 (Spindle on CW) ;               | M03 turns the spindle on in a clockwise direction. It takes the address code Snnnn , where nnnn is the desired spindle RPM. On machines with a gearbox, the control automatically selects high gear or low gear, based on the commanded spindle speed. You can use an M41 or M42 to override this. Refer to page 444 for more information on these M-codes.                                                                                                                                                                                                   |
| G43 H01 Z0.1 (Tool offset 1 on) ;         | G43 H01 turns on Tool Length Compensation +. The H01 specifies to use the length stored for Tool 1 in the Tool Offset display. Z0.1 commands the Z Axis to Z=0.1.                                                                                                                                                                                                                                                                                                                                                                                             |
| M08 (Coolant on) ;                        | M08 commands the coolant to turn on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## 5.18 Cutting

These are the cutting code blocks in the sample program O40001:

| Cutting Code Block                       | Description                                                                                                                                                                                                                                             |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G01 F20. Z-0.1 (Feed to cutting depth) ; | G01 F20. defines axis movements after it to be completed in a straight line. G01 requires the address code Fnnn.nnnn . The address code F20. specifies that the feed rate for the motion is 20" (508 mm) / min. Z-0.1 commands the Z Axis to Z = - 0.1. |
| X-4. Y-4. (linear motion) ;              | X-4. Y-4. commands the X Axis to move to X = - 4.0 and commands the Y Axis to move to Y = - 4.0.                                                                                                                                                        |

## 5.19 Completion

These are the completion code blocks in the sample program O40001:

| Completion Code Block                       | Description                                                                                                                                                                                   |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G00 Z0.1 M09 (Rapid retract, Coolant off) ; | G00 commands the axis motion to be completed in rapid motion mode. Z0.1 Commands the Z Axis to Z = 0.1. M09 commands the coolant to turn off.                                                 |
| G53 G49 Z0 M05 (Z home, Spindle off) ;      | G53 defines axis movements after it to be with respect to the machine coordinate system. G49 cancels tool length compensation. Z0 is a command to move to Z = 0.0. M05 turns the spindle off. |
| G53 Y0 (Y home) ;                           | G53 defines axis movements after it to be with respect to the machine coordinate system. Y0 is a command to move to Y = 0.0.                                                                  |
| M30 (End program) ;                         | M30 ends the program and moves the cursor on the control to the top of the program.                                                                                                           |
| %                                           | Denotes the end of a program written in a text editor.                                                                                                                                        |

## 5.20 Absolute vs. Incremental Positioning (G90, G91)

Absolute ( G90 )  and incremental positioning ( G91 )  define  how the control interprets axis motion commands.

When you command axis motion after a G90 code, the axes move to that position relative to the origin of the coordinate system currently in use.

When you command axis motion after a G91 , the axes move to that position relative to the current position.

Absolute  programming  is  useful  in  most  situations.  Incremental  programming  is  more efficient for repetitive, equally spaced cuts.

Figure F5.16 shows a part with 5 equally spaced Ø0.25" (13 mm) diameter holes. The hole depth is 1.00" (25.4 mm) and the spacing is 1.250" (31.75 mm) apart.

F5.16: Absolute / Incremental Sample Program. G54 X0. Y0. for Incremental [1], G54 for Absolute [2]

<!-- image -->

Below are  two  example  programs  that  drill  the  holes  as  shown  in  the  drawing,  with  a comparison between absolute and incremental positioning. We start the holes with a center drill, and finish drilling the holes with a 0.250" (6.35 mm) drill bit. We use a 0.200" (5.08 mm) depth of cut for the center drill and 1.00" (25.4 mm) depth of cut for the 0.250" drill. G81 , Drill Canned Cycle, is used to drill the holes.

## F5.17: Mill Incremental Positioning Example.

<!-- image -->

```
% O40002 (Incremental ex-prog) ; N1 (G54 X0 Y0 is center left of part) ; N2 (Z0 is on top of the part) ; N3 (T1 is a center drill) ; N4 (T2 is a drill) ; N5 (T1 PREPARATION BLOCKS) ; N6 T1 M06 (Select tool 1) ; N7 G00 G90 G40 G49 G54 (Safe startup) ; N8 X0 Y0 (Rapid to 1st position) ; N9 S1000 M03 (Spindle on CW) ; N10 G43 H01 Z0.1(Tool offset 1 on) ; N11 M08(Coolant on) ; N12 (T1 CUTTING BLOCKS) ; N13 G99 G91 G81 F8.15 X1.25 Z-0.3 L5 ; N14 (Begin G81, 5 times) ; N15 G80 (Cancel G81) ; N16 (T1 COMPLETION BLOCKS) ; N17 G00 G90 G53 Z0. M09 (rapid retract, clnt off); N18 M01 (Optional stop) ; N19 (T2 PREPARATION BLOCKS) ; N20 T2 M06 (Select tool 2) ; N21 G00 G90 G40 G49 (Safe startup) ; N22 G54 X0 Y0 (Rapid to 1st position) ;
```

```
N23 S1000 M03 (Spindle on CW) ; N24 G43 H02 Z0.1(Tool offset 2 on) ; N25 M08(Coolant on) ; N26 (T2 CUTTING BLOCKS) ; N27 G99 G91 G81 F21.4 X1.25 Z-1.1 L5 ; N28 G80 (Cancel G81) ; N29 (T2 COMPLETION BLOCKS) ; N30 G00 Z0.1 M09 (Rapid retract, clnt off) ; N31 G53 G90 G49 Z0 M05 (Z home, spindle off) ; N32 G53 Y0 (Y home) ; N33 M30 (End program) ; %
```

## F5.18: Mill Absolute Positioning Example

<!-- image -->

```
% O40003 (Absolute ex-prog) ; N1 (G54 X0 Y0 is center left of part) ; N2 (Z0 is on top of the part) ; N3 (T1 is a center drill) ; N4 (T2 is a drill) ; N5 (T1 PREPARATION BLOCKS) ; N6 T1 M06 (Select tool 1) ; N7 G00 G90 G40 G49 G54 (Safe startup) ; N8 X1.25 Y0 (Rapid to 1st position) ; N9 S1000 M03 (Spindle on CW) ;
```

```
N10 G43 H01 Z0.1 (Tool offset 1 on) ; N11 M08 (Coolant on) ; N12 (T1 CUTTING BLOCKS) ; N13 G99 G81 F8.15 X1.25 Z-0.2 ; N14 (Begin G81, 1st hole) ; N15 X2.5 (2nd hole) ; N16 X3.75 (3rd hole) ; N17 X5. (4th hole) ; N18 X6.25 (5th hole) ; N19 G80 (Cancel G81) ; N20 (T1 COMPLETION BLOCK) ; N21 G00 G90 G53 Z0. M09 (Rapid retract, clnt off); N22 M01 (Optional Stop) ; N23 (T2 PREPARATION BLOCKS) ; N24 T2 M06 (Select tool 2) ; N25 G00 G90 G40 G49 (Safe startup) ; N26 G54 X1.25 Y0 (Rapid to 1st position) ; N27 S1000 M03 (Spindle on CW) ; N28 G43 H02 Z0.1 (Tool offset 2 on) ; N29 M08 (Coolant on) ; N30 (T2 CUTTING BLOCKS) ; N31 G99 G81 F21.4 X1.25 Z-1. (1st hole) ; N32 X2.5 (2nd hole) ; N33 X3.75 (3rd hole) ; N34 X5. (4th hole) ; N35 X6.25 (5th hole) ; N36 G80 (Cancel G81) ; N37 (T2 COMPLETION BLOCKS) ; N38 G00 Z0.1 M09 (Rapid retract, Clnt off) ; N39 G53 G49 Z0 M05 (Z home, Spindle off) ; N40 G53 Y0 (Y home) ; N41 M30 (End program) ; %
```

The absolute program method needs more lines of code than the incremental program. The programs have similar preparation and completion sections.

Look at line N13 in the incremental programming example, where the center drill operation begins. G81 uses the loop address code, Lnn , to specify the number of times to repeat the cycle. The address code L5 repeats this process (5) times. Each time the canned cycle repeats, it moves the distance that the optional X and Y values specify. In this program, the incremental program moves 1.25" in X from the current position with each loop, and then does the drill cycle.

For each drill operation, the program specifies a drill depth 0.1" deeper than the actual depth, because motion starts from 0.1" above the part.

In absolute positioning, G81 specifies the drill depth, but it does not use the loop address code. Instead, the program gives the position of each hole on a separate line. Until G80 cancels the canned cycle, the control does the drill cycle at each position.

The absolute positioning program specifies the exact hole depth, because the depth starts at the part surface (Z=0).

## 5.21 G43 Tool Offset

The G43  Hnn Tool  Length  Compensation  command  should  be  used  after  every  tool change.  It  adjusts  the  Z-Axis  position  to  account  for  the  length  of  the  tool.  The Hnn argument specifies which tool length to use. For more information see Setting Tool Offsets on page 137 in the Operation section.

<!-- image -->

## CAUTION:

The tool length nn value should match the nn value from the M06 Tnn tool change command to avoid a possible collision.

Setting 15 - H &amp; T Code Agreement controls whether the nn value needs to match in the Tnn and Hnn arguments. If Setting 15 is ON and the Tnn and Hnn do not match, Alarm 332 - H and T Not Matched is generated.

## 5.22 G54 Work Offsets

Work Offsets define where a work piece is located on the table.

Work Offsets available are G54 - G59 , G110 - G129 ,  and G154  P1-P99 . G110 - G129 and G154 P1-P20 refer to the same Work Offsets.

A useful feature is to set up multiple work pieces on the table and machining multiple parts in one machine cycle. This is accomplished by assigning each work piece to a different Work Offset.

For more information, reference the G-code section of this manual. Below is an example of machining multiple parts in one cycle. The program uses M97 Local Sub-Program Call in the cutting operation.

```
% O40005 (Work offsets ex-prog) ; (G54 X0 Y0 is center left of part) ; (Z0 is on top of the part) ; (T1 is a drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54(Safe startup) ; X0 Y0 ;
```

<!-- image -->

NOTE:

```
(Move to first work coordinate position-G54) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1 (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; M97 P1000 (Call local Subprogram) ; G00 Z3. (Rapid retract) ; G90 G110 G17 G40 G80 X0. Y0. ; (Move to second work coordinate position-G110) ; M97 P1000 (Call local Subprogram) ; G00 Z3. (Rapid Retract) ; G90 G154 P22 G17 G40 G80 X0. Y0. ; (Move to third work coordinate position-G154 P22) ; M97 P1000 (Call local Subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; N1000 (Local subprogram) ; G81 F41.6 X1. Y2. Z-1.25 R0.1 (Begin G81) ; (1st hole) ; X2. Y2. (2nd hole) ; G80 (Cancel G81) ; M99 ; %
```

## 5.23 Miscellaneous Codes

This section lists frequently used M-codes. Most programs have at least one M-code from each of the following families.

Refer to the M-code section of this manual, starting on page 433 , for a list of all M-codes with descriptions.

You can use only one M-code on each line of the program.

## 5.24 Tool Functions (Tnn)

The Tnn code selects the next tool to be placed in the spindle from the tool changer. The T address does not start the tool change operation; it only selects which tool will be used next. M06 starts a tool change operation; for example, T1M06 puts tool 1 in the spindle.

<!-- image -->

## CAUTION:

There is no X or Y motion required before a tool change; however, if the work piece or fixture is large, position X or Y before a tool change to prevent a crash between the tools and the part or fixture.

You can command a tool change with the X, Y, and Z Axes in any position. The control will bring the Z Axis up to the machine zero position. The control moves the Z Axis to a position above machine zero during a tool change, but it never moves below machine zero. At the end of a tool change, the Z Axis is at machine zero.

## 5.25 Spindle Commands

There are (3) primary spindle M-code commands:

- M03 Snnnn commands the spindle to turn clockwise.
- M04 Snnnn commands the spindle to turn counter-clockwise.

The Snnnn address commands the spindle to turn at nnnn RPM, up to the maximum spindle speed.

- M05 commands the spindle to stop.

When you command an M05 , the control waits for the spindle to stop before the program continues.

NOTE:

<!-- image -->

<!-- image -->

NOTE:

## 5.26 Program Stop Commands

There are (2) main M-codes and (1) subprogram M-code to denote the end of a program or subprogram:

- M30 - Program End and Rewind ends the program and resets to the beginning of the program. This is the most common way to end a program.
- M02 - Program End ends the program and remains at the location of the M02 block of code in the program.

<!-- image -->

NOTE:

- M99 - Subprogram Return or Loop exits the subprogram and resumes the program that called it.

If your subprogram does not end with M99 , the control gives Alarm 312 - Program End .

## 5.27 Coolant Commands

Use M08 to  command standard coolant on. Use M09 to  command standard coolant off. Refer to page 438 for more information on these M-codes.

If your machine has Through-Spindle Coolant (TSC), use M88 to command it on, and M89 to command it off.

## 5.28 Cutting G-codes

The main cutting G-codes are categorized into interpolation motion and canned cycles. Interpolation motion cutting codes are broken down into:

- G01 - Linear Interpolation Motion
- G02 - Clockwise Circular Interpolation Motion
- G03 - Counter-Clockwise Circular Interpolation Motion
- G12 - Clockwise Circular Pocket Milling
- G13 - Counter-Clockwise Circular Pocket Milling

## 5.29 Linear Interpolation Motion

G01 Linear Interpolation Motion is used to cut straight lines. It requires a feedrate, specified with the Fnnn.nnnn address code. Xnn.nnnn , Ynn.nnnn , Znn.nnnn , and Annn.nnn are optional address codes to specify cut. Subsequent axis motion commands will use the feed  rate  specified  by G01 until  another  axis  motion, G00 , G02 , G03 , G12 ,  or G13 is commanded.

Corners can be chamfered using the optional argument Cnn.nnnn to define the chamfer. Corners can be rounded using the optional address code Rnn.nnnn to define the radius of the arc. Refer to page 323 for more information on G01 .

## 5.30 Circular Interpolation Motion

G02 and G03 are the G-codes for circular cutting motions. Circular Interpolation Motion has several optional address codes to define the arc or circle. The arc or circle begins cutting from the current cutter position [1] to the geometry specified within the G02 / G03 command.

Arcs can be defined using two different methods. The preferred method is to define the center of the arc or circle with I, J and/or K and to define the end point [3] of the arc with an X, Y and/or Z. The I J K values define the relative X Y Z distances from the starting point [2] to the center of the circle. The X Y Z values define the absolute X Y Z distances from the starting point to the end point of the arc within the current coordinate system. This is also the only method to cut a circle. Defining only the I J K values and not defining the end point X Y Z values will cut a circle.

The other method to cut an arc is to define the X Y Z values for the end point and to define the radius of the circle with an R value.

Below are examples of using the two different methods to cut a 2" (or 2 mm) radius, 180 degree, counter-clockwise arc. The tool starts at X0 Y0 [1], moves to the starting point of the arc [2], and cuts the arc to the end point [3]:

## F5.19: Arc Cutting Example

<!-- image -->

## Method 1:

```
% T01 M06 ; ... G00 X4. Y2. ; G01 F20.0 Z-0.1 ;
```

```
G03 F20.0 I-2.0 J0. X0. Y2. ; ... M30 ; %
```

## Method 2:

```
% T01 M06 ; ... G00 X4. Y2. ; G01 F20.0 Z-0.1 ; G03 F20.0 X0. Y2. R2. ; ...M30 ; %
```

Below is an example of how to cut a 2" (or 2 mm) radius circle:

```
% T01 M06 ; ... G00 X4. Y2. ; G01 F20.0 Z-0.1 ; G02 F20.0 I2.0 J0. ; ... M30 ; %
```

## 5.31 Cutter Compensation

Cutter compensation is a method of shifting the tool path so that the actual centerline of the tool moves to either the left or right of the programmed path. Normally, cutter compensation is programmed to shift the tool in order to control feature size. The offset display is used to enter the amount that the tool is to be shifted. The offset can be entered as either a diameter or  radius  value,  depending  on  Setting  40,  for  both  the  geometry  and  wear  values.  If diameter is specified, the shift amount is half of the value entered. The effective offset values are the sum of the geometry and wear values. Cutter compensation is only available in  the  X  Axis  and  the  Y  Axis  for  2D  machining  ( G17 ).  For  3D  machining,  cutter compensation is available in the X Axis, Y Axis, and Z Axis ( G141 ).

## 5.32 General Description of Cutter Compensation

G41 selects cutter compensation left. This means that the control moves the tool to the left of the programmed path (with respect to the direction of travel) to compensate for the tool radius or diameter defined in the tool offsets table (Refer to Setting 40). G42 selects cutter compensation right, which moves the tool to the right of the programmed path, with respect to the direction of travel.

A G41 or G42 command must have a Dnnn value to select the correct offset number from the radius / diameter offset column. The number to use with D is in the far-left column of the tool  offsets  table.The  value  that  the  control  uses  for  cutter  compensation  is  in  the GEOMETRY column under D (if Setting 40 is DIAMETER ) or R (if Setting 40 is RADIUS ).

If  the  offset  value  is  negative,  cutter  compensation  operates  as  though  the  program specifies the opposite G code. For example, a negative value entered for a G41 will behave as if a positive value was entered for G42 . Also, when cutter compensation is active ( G41 or G42 ), you may use only the X-Y plane ( G17 ) for circular motions. Cutter compensation is limited to compensation in only the X-Y plane.

G40 cancels cutter compensation and is the default condition when you power on your machine. When cutter compensation is not active, the programmed path is the same as the center of the cutter path. You may not end a program ( M30 , M00 , M01 , or M02 ) with cutter compensation active.

The control operates on one motion block at a time. However, it will look ahead at the next (2) blocks that have X or Y motions. The control checks these (3) blocks of information for interference.  Setting  58 controls  how  this  part  of  cutter  compensation  works. Available Setting 58 values are Fanuc or Yasnac.

If Setting 58 is set to Yasnac, the control must be able to position the side of the tool along all of the edges of the programmed contour without overcutting the next two motions. A circular motion joins all of the outside angles.

If Setting 58 is set to Fanuc, the control does not require that the tool cutting edge be placed along all edges of the programmed contour, preventing overcutting. However the control will generate an alarm if the cutter's path is programmed so that it will overcut. The control joins outside angles less than or equal to 270 degrees with a sharp corner. It joins outside angles of more than 270 degrees with an extra linear motion.

These diagrams show how cutter compensation works for the possible values of Setting 58. Note that a small cut of less than the tool radius and at a right angle to the previous motion will work only with the Fanuc setting.

- F5.20: Cutter Compensation, YASNAC Style,G41 with a Positive Tool Diameter or G42 with a Negative Tool Diameter: [1] Tool Path Actual Center, [2] Programmed Tool Path, [3] Start Point, [4] Cutter Compensation. G41 / G42 and G40 are commanded at the start and end of the tool path.
- F5.21: Cutter Compensation, YASNAC Style, G42 with a Positive Tool Diameter or G41 with a Negative Tool Diameter: [1] Tool Path Actual Center, [2] Programmed Tool Path, [3] Start Point, [4] Cutter Compensation. G41 / G42 and G40 are commanded at the start and end of the tool path.

<!-- image -->

<!-- image -->

F5.22: Cutter Compensation, FANUC Style, G41 with a Positive Tool Diameter or G42 with a Negative Tool Diameter: [1] Tool Path Actual Center, [2] Programmed Tool Path, [3] Start Point, [4] Cutter Compensation. G41 / G42 and G40 are commanded at the start and end of the tool path.

<!-- image -->

F5.23: Cutter Compensation, FANUC Style, G42 with a Positive Tool Diameter or G41 with a Negative Tool Diameter: [1] Tool Path Actual Center, [2] Programmed Tool Path, [3] Start Point, [4] Cutter Compensation. G41 / G42 and G40 are commanded at the start and end of the tool path.

<!-- image -->

## 5.33 Entry and Exit from Cutter Compensation

When entering and exiting cutter compensation, or when changing from left side to right side compensation, there are special considerations to be aware of. Cutting should not be performed during any of these moves. To activate cutter compensation, a nonzero D code must be specified with either G41 or G42 and G40 must be specified in the line that cancels cutter compensation. In the block that turns on cutter compensation, the starting position of the move is the same as the programmed position, but the ending position will be offset, to either  the  left  or  right  of  the  programmed  path,  by  the  amount  entered  in  the, radius/diameter, offset column.

In the block that turns off cutter compensation, the starting point is offset and the ending point  is  not  offset.  Similarly,  when  changing  from  left  to  right  or  right  to  left  side compensation,  the  starting  point  of  the  move  needed  to  change  cutter  compensation direction will be offset to one side of the programmed path and end at a point that is offset to the opposite side of the programmed path. The result of all this is that the tool moves through a path that may not be the same as the intended path or direction.

If  cutter compensation is turned on or off in a block without any X-Y move, there is no change made to cutter compensation until the next X or Y move is encountered. To exit from cutter compensation, you must specify G40 .

You should always turn off cutter compensation in a move that clears the tool away from the part being cut. If a program is terminated with cutter compensation still active, an alarm is generated. In addition, you cannot turn cutter compensation on or off during a circular move ( G02 or G03 ); otherwise an alarm will be generated.

An offset selection of D0 will  use zero as  the  offset value and have the same effect as turning off cutter compensation. If a new D value is selected while cutter compensation is already active, the new value will take effect at the end of the proceeding move. You cannot change the D value or change sides during a circular motion block.

When turning on cutter compensation in a move that is followed by a second move at an angle of less than 90 degrees, there are two ways of computing the first motion: cutter compensation type A and type B (Setting 43). Type A is the default in Setting 43 and is what is normally needed; the tool moves directly to the offset start point for the second cut. Type B is used when clearance around a fixture of clamp is needed, or in rare cases when part geometry demands it. The diagrams in this section illustrate the differences between type A and type B for both Fanuc and Yasnac settings (Setting 58 ).

## 5.34 Improper Cutter Compensation Application

F5.24: Improper Cutter Compensation: [1] Move is less than cutting comp radius, [2] Workpiece, [3] Tool.

<!-- image -->

A small cut of less than tool radius and at a right angle to the previous motion will only work with the Fanuc setting. A cutter compensation alarm will be generated if the machine is set to the Yasnac setting.

<!-- image -->

## 5.35 Feed Adjustments in Cutter Compensation

When  using  cutter  compensation  in  circular  moves,  there  is  the  possibility  of  speed adjustments to what has been programmed. If the intended finish cut is on the inside of a circular motion, the tool should be slowed down to ensure that the surface feed does not exceed what was intended by the programmer. There are problems, however, when the speed is slowed by too much. For this reason, Setting 44 is used to limit the amount by which the feed is adjusted in this case. It can be set between 1% and 100%. If set to 100%, there  will  be  no  speed  changes.  If  set  to  1%,  the  speed  can  be  slowed  to  1%  of  the programmed feed.

When the cut is on the outside of a circular motion, there is no speed-up adjustment made to the feed rate.

## 5.36 Cutter Compensation Entry (Yasnac)

- F5.25: Cutter Compensation Entry (Yasnac) Type A and B: [1] Programmed Path, [2] Tool Center Path, [r] Tool Radius

<!-- image -->

## 5.37 Cutter Compensation Entry (Fanuc style)

F5.26: Cutter Compensation Entry (Fanuc style) Type A and B: [1] Programmed Path, [2] Tool Center Path, [r] Tool Radius

<!-- image -->

## 5.38 Circular Interpolation and Cutter Compensation

In  this  section,  the  usage  of G02 (Circular  Interpolation  Clockwise), G03 (Circular Interpolation  Counterclockwise)  and  Cutter  Compensation  ( G41 :  Cutter  Compensation Left, G42 : Cutter Compensation Right) is described.

Using G02 and G03 ,  we  can  program  the  machine  to  cut  circular  moves  and  radii. Generally, when programming a profile or a contour, the easiest way to describe a radius between two points is with an R and a value. For complete circular moves (360 degrees), an I or a J with a value must be specified. The circle section illustration will describe the different sections of a circle.

By using cutter compensation in this section, the programmer will be able to shift the cutter by  an  exact  amount  and  be  able  to  machine  a  profile  or  a  contour  to  the  exact  print dimensions.  By  using  cutter  compensation,  programming  time  and  the  likelihood  of  a programming  calculation  error  is  reduced  due  to  the  fact  that  real  dimensions  can  be programmed, and part size and geometry can be easily controlled.

Here are a few rules about cutter compensation that you must follow closely for successful machining operations. Always refer to these rules when you write your programs.

1. Cutter compensation must be turned ON during a G01 X,Y move that is equal to or greater than the cutter radius, or the amount being compensated.
2. When an operation using cutter compensation is done, the cutter compensation will need to be turned OFF, using the same rules as the turn ON process, i.e., what is put in must be taken out.
3. In most machines, during cutter compensation, a linear X,Y move that is smaller than the cutter radius may not work. (Setting 58 - set to Fanuc - for positive results.)
4. Cutter compensation cannot be turned ON or OFF in a G02 or G03 arc movement.
5. With cutter compensation active, machining an inside arc with a radius less than what is defined by the active D value causes the machine to alarm. Can not have too big of a tool diameter if the radius of arc is too small.

## F5.27: Circle Sections

<!-- image -->

This illustration  shows how the tool path is calculated for the cutter compensation. The detail section shows the tool in the starting position and then in the offset position as the cutter reaches the workpiece.

F5.28: Circular Interpolation G02 and G03 : [1] 0.250" diameter endmill, [2] Programmed path, [3] Center of Tool, [4] Start Position, [5] Offset Tool Path.

<!-- image -->

## Programming exercise showing tool path.

This program uses cutter compensation. The toolpath is programmed to the centerline of the cutter. This is also the way the control calculates for cutter compensation.

```
% O40006 (Cutter comp ex-prog) ; (G54 X0 Y0 is at the lower left of part corner) ; (Z0 is on top of the part) ; (T1 is a .250 dia endmill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; X-1. Y-1. (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z0.1(Tool offset 1 on) ; M08(Coolant on) ; (BEGIN CUTTING BLOCKS) ; G01 Z-1. F50. (Feed to cutting depth) ; G41 G01 X0 Y0 D01 F50. (2D Cutter Comp left on) ; Y4.125 (Linear motion) ; G02 X0.25 Y4.375 R0.375 (Corner rounding) ; G01 X1.6562 (Linear motion) ; G02 X2. Y4.0313 R0.3437 (Corner rounding) ; G01 Y3.125 (Linear motion) ;
```

```
G03 X2.375 Y2.75 R0.375 (Corner rounding) ; G01 X3.5 (Linear motion) ; G02 X4. Y2.25 R0.5 (Corner rounding) ; G01 Y0.4375 (Linear motion) ; G02 X3.4375 Y-0.125 R0.5625 (Corner rounding) ; G01 X-0.125 (Linear motion) ; G40 X-1. Y-1. (Last position, cutter comp off) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## 5.39 Canned Cycles

Canned cycles are G-codes that do repetitive operations such as drilling,  tapping, and boring. You define a canned cycle with alphabetic address codes. While the canned cycle is active, the machine does the defined operation every time you command a new position, unless you specify not to.

## 5.40 Drilling Canned Cycles

All four drill canned cycles can be looped in G91 , Incremental Programming mode.

- The G81 Drill Canned Cycle is the basic drilling cycle. It is used for drilling shallow holes or for drilling with Through Spindle Coolant (TSC).
- The G82 Spot Drill Canned Cycle is the same as the G81 Drill Canned Cycle except that it can dwell at the bottom of the hole. The optional argument Pn.nnn specifies the duration of the dwell.
- The G83 Normal Peck Drilling Canned Cycle is typically used for drilling deep holes. Peck depth can be variable or constant and always incremental. Qnn.nnn. Do not use a Q value when programming with I, J, and K.
- The G73 High-Speed Peck Drilling Canned Cycle is the same as the G83 Normal Peck Drilling Canned Cycle except that tool peck retraction is specified with Setting 22 - Can Cycle Delta Z. Peck drilling cycles are advised for hole depths greater than 3  times  the  diameter  of  the  drill  bit.  The  initial  peck  depth,  defined  by I ,  should generally be a depth of 1 tool diameter.

## 5.41 Tapping Canned Cycles

There are two tapping canned cycles. All tapping canned cycles can be looped in G91 , Incremental Programming mode.

- The G84 Tapping Canned Cycle is the normal tapping cycle. It is used for tapping right-hand threads.

- G74 Reverse Tap Canned Cycle is the reverse thread tapping cycle. It is used for tapping left-hand threads.

## 5.42 Boring and Reaming Cycles

There  are  (5)  boring  canned  cycles.  All  boring  canned  cycles  can  be  looped  in G91 , Incremental Programming mode.

- The G85 Boring Canned Cycle is the basic boring cycle. It will  bore down to  the desired height and return to the specified height.
- The G86 Bore and Stop Canned Cycle is the same as the G85 Boring Canned Cycle except that the spindle will stop at the bottom of the hole before returning to the specified height.
- The G89 Bore In, Dwell, Bore Out Canned Cycle is the same as G85 except that there is a dwell at the bottom of the hole, and the hole continues to be bored at the specified feed rate as the tool returns to the specified position. This differs from other boring canned cycles where the tool either moves in Rapid Motion or hand jog to return to the return position.
- The G76 Fine Boring Canned Cycle bores the hole to the specified depth and after boring the hole, moves to clear the tool from hole before retracting.
- The G77 Back Bore Canned Cycle works similar to G76 except that before beginning to bore the hole, it moves the tool to clear the hole, moves down into the hole, and bores to the specified depth.

## 5.43 R Planes

R Planes, or return planes, are G-code commands that specify the Z-Axis return height during canned cycles. The R Plane G-codes remain active for the duration of the canned cycle it is used with. G98 Canned Cycle Initial Point Return moves the Z axis to the height of the Z axis prior to the canned cycle. G99 Canned Cycle R Plane Return moves the Z axis to the height specified by the Rnn.nnnn argument specified with the canned cycle. For additional information, refer to the G and M-code section.

## 5.44 Special G-codes

Special G-codes are used for complex milling. These include:

- Engraving ( G47 )
- Pocket Milling ( G12 , G13 , and G150 )
- Rotation and Scaling ( G68 , G69 , G50 , G51 )
- Mirror Image ( G101 and G100 )

## 5.45 Engraving

The G47 Text Engraving G-code lets you engrave text (including some ASCII characters) or sequential serial numbers with a single block of code.

Refer to page 347 for more information on engraving.

## 5.46 Pocket Milling

There are two types of pocket milling G-codes on the Haas control:

- Circular Pocket Milling is performed with the G12 Clockwise Circular Pocket Milling Command  and  the G13 Counter-Clockwise  Circular  Pocket  Milling  Command G-codes.
- The G150 General  Purpose  Pocket  Milling  uses  a  subprogram  to  machine user-defined pocket geometries.

Make sure that the subprogram geometry is a fully closed shape. Make sure that the X-Y starting point in the G150 command is within the boundary of the fully closed shape. Failure to do so may cause Alarm 370 - Pocket Definition Error.

Refer to page 334 for more information on the pocket milling G-codes.

## 5.47 Rotation and Scaling

<!-- image -->

You  must  purchase  the  rotation  and  scaling  option  to  use  these features. A 200-hour option tryout is also available.

G68 Rotation is used to rotate the coordinate system in the desired plane. You can use this feature  together  with G91 Incremental  Programming  mode  to  machine  symmetrical patterns. G69 cancels rotation.

G51 applies a scaling factor to the positioning values in blocks after the G51 command. G50 cancels  scaling.  You  can  use  scaling  together  with  rotation,  but  be  sure  to  command scaling first.

Refer to page 363 for more information on the rotation and scaling G-codes.

## 5.48 Mirror Image

G101 Enable Mirror Image will mirror axis motion about the specified axis. Settings 45 - 48 , 80 and 250 enable mirror imaging about the X, Y, Z, A, B, and C axes. The mirror pivot point along an axis is defined by the Xnn.nn argument. This can be specified for a Y Axis that  is  enabled  on  the  machine  and  in  the  settings  by  using  the  axis  to  mirror  as  the argument. G100 cancels G101 .

Refer to page 389 for more information on the mirror image G-codes.

## 5.49 Subprograms

Subprograms:

- Are usually a series of commands that are repeated several times in a program.
- Are written in a separate program, instead of repeating the commands many times in the main program.
- Are called in the main program with an M97 or M98 and a P code.
- Can include an L for repeat count. The subprogram call repeats L times before the main program continues with the next block.

When you use M97 :

- The P code  ( nnnnn )  is  the  same  as  the  block  number  ( Nnnnnn )  of  the  local subprogram.
- The subprogram must be within the main program

When you use M98 :

- The P code  ( nnnnn )  is  the  same  as  the  program  number  ( Onnnnn )  of  the subprogram.
- If the subprogram is not in memory, the file name must be Onnnnn.nc . The file name must contain the O, leading zeros and .nc for the machine to find the subprogram.
- The subprogram must reside in the active directory,  or  in  a  location  specified  in Settings 251/252. Refer to page 497 for  more  information on subprogram search locations.

Canned Cycles are the most common use of subprograms. For example, you might put the X and Y locations of a series of holes in a separate program. Then you can call that program as a subprogram with a canned cycle. Instead of writing the locations once for each tool, you write the locations only once for any number of tools.

## 5.50 External Subprogram (M98)

An external subprogram is a separate program that the main program references. Use M98 to command (call) an external subprogram, with Pnnnnn to refer to the program number you want to call.

When your program calls an M98 subprogram, the control looks for the subprogram in the main program's directory. If the control cannot find the subprogram in the main program's directory, it then looks in the location specified in Setting 251. Refer to page 496 for more information. An alarm occurs if the control cannot find the subprogram.

In this example, the subprogram (program O40008) specifies (8) positions. It also includes a G98 command at the move between positions 4 and 5. This causes the Z Axis to return to the initial starting point instead of the R plane, so the tool passes over the workholding.

The main program (Program O40007) specifies (3) different canned cycles:

1. G81 Spot drill at each position
2. G83 Peck drill at each position
3. G84 Tap at each position

Each canned cycle calls the subprogram and does the operation at each position.

```
% O40007 (External subprogram ex-prog) ; (G54 X0 Y0 is center left of part) ; (Z0 is on top of the part) ; (T1 is a spot drill) ; (T2 is a drill) ; (T3 is a tap) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X1.5 Y-0.5 (Rapid to 1st position) ; S1000 M03 (Spindle on CW) ; G43 H01 Z1. (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G81 G99 Z-0.14 R0.1 F7. (Begin G81) ; M98 P40008 (Call external subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; M01 (Optional stop) ; (BEGIN PREPARATION BLOCKS) ; T2 M06 (Select tool 2) ; G00 G90 G40 G49 G54 (Safe startup) ;
```

```
G00 G54 X1.5 Y-0.5 (Rapid to 1st position) ; S2082 M03 (Spindle on CW) ; G43 H02 Z1. (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G83 G99 Z-0.75 Q0.2 R0.1 F12.5 (Begin G83) ; M98 P40008 (Call external subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; M01 (Optional stop) ; (BEGIN PREPARATION BLOCKS) ; T3 M06 (Select tool 3) ; G00 G90 G40 G49 G54 (Safe startup) ; G00 G54 X1.5 Y-0.5 (Rapid to 1st position) ; S750 M03 (Spindle on CW) ; G43 H03 Z1. (Tool offset 3 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G84 G99 Z-0.6 R0.1 F37.5 (Begin G84) ; M98 P40008 (Call external subprogram); (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## F5.29: Subprogram Pattern

<!-- image -->

## Subprogram

```
% O40008 (Subprogram) ; X0.5 Y-0.75 (2nd position) ; Y-2.25 (3rd position) ; G98 X1.5 Y-2.5 (4th position) ; (Initial point return) ; G99 X3.5 (5th position) ; (R plane return) ; X4.5 Y-2.25 (6th position); Y-0.75 (7th position) ; X3.5 Y-0.5 (8th position) ; M99 (sub program return or loop) ; %
```

## 5.51 Local Subprogram (M97)

A local subprogram is a block of code in the main program that is referenced several times by  the  main  program.  Local  subprograms  are  commanded  (called)  using  an M97 and Pnnnnn , which refers to the N line number of the local subprogram.

The local subprogram format is to end the main program with an M30 then enter the local subprograms after the M30 . Each subprogram must have an N line number at the start and a M99 at the end that will send the program back to the next line in the main program.

## 5.52 Local Subprogram Example

```
% O40009 (Local subprogram ex-prog) ; (G54 X0 Y0 is at the top left corner of part) ; (Z0 is on top of the part) ; (T1 is a spot drill) ; (T2 is a drill) ; (T3 is a tap) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54(Safe startup) ; X1.5 Y-0.5 (Rapid to 1st position) ; S1406 M03 (Spindle on CW) ; G43 H01 Z1.(Tool offset 1 on) ; M08(Coolant on) ; (BEGIN CUTTING BLOCKS) ; G81 G99 Z-0.26 R0.1 F7. (Begin G81) ; M97 P1000 (Call local subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; M01 (Optional stop) ; (BEGIN PREPARATION BLOCKS) ; T2 M06 (Select tool 2) ; G00 G90 G40 G49 (Safe startup) ; G54 X1.5 Y-0.5 (Rapid back to 1st position) ; S2082 M03 (Spindle on CW) ; G43 H02 Z1. (Tool offset 2 on) ; M08(Coolant on) ; (BEGIN CUTTING BLOCKS) ; G83 G99 Z-0.75 Q0.2 R0.1 F12.5 (Begin G83) ; M97 P1000 (Call local subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ;
```

```
M01 (Optional stop) ; (BEGIN PREPARATION BLOCKS) ; T3 M06 (Select tool 3) ; G00 G90 G40 G49 (Safe startup) ; G54 X1.5 Y-0.5 ; (Rapid back to 1st position) ; S750 M03 (Spindle on CW) ; G43 H03 Z1.(Tool offset 3 on) ; M08(Coolant on) ; (BEGIN CUTTING BLOCKS) ; G84 G99 Z-0.6 R0.1 F37.5 (Begin G84) ; M97 P1000 (Call local subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; (LOCAL subprogram) ; N1000 (Begin local subprogram) ; X0.5 Y-0.75 (2nd position) ; Y-2.25 (3rd position) ; G98 X1.5 Y-2.5 (4th position) ; (Initial point return) ; G99 X3.5 (5th position) ; (R-plane return) ; X4.5 Y-2.25 (6th position) ; Y-0.75 (7th position) ; X3.5 Y-0.5 (8th position) ; M99 ; %
```

## 5.53 External Subprogram Canned Cycle Example (M98)

```
% O40010 (M98_External sub canned cycle ex) ; (G54 X0 Y0 is at the top left of the part) ; (Z0 is on top of the part) ; (T1 is a spot drill) ; (T2 is a drill) ; (T3 is a tap) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54(Safe startup) ;
```

```
X0.565 Y-1.875 (Rapid to 1st position) ; S1275 M03 (Spindle on CW) ; G43 H01 Z0.1 (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G82 Z-0.175 P0.03 R0.1 F10. (Begin G82) ; M98 P40011 (Call external subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; M01 (optional stop) ; (BEGIN PREPARATION BLOCKS) ; T2 M06 (Select tool 2) ; G00 G90 G40 G49 (Safe startup) ; G54  X0.565 Y-1.875 ; (Rapid back to 1st position) ; S2500 M03 (Spindle on CW) ; G43 H02 Z0.1 (Tool offset 2 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G83 Z-0.72 Q0.175 R0.1 F15. (Begin G83) ; M98 P40011 (Call external subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; M01 (optional stop) ; (BEGIN PREPARATION BLOCKS) ; T3 M06 (Select tool 3) ; G00 G90 G40 G49 (Safe startup) ; G54  X0.565 Y-1.875 ; (Rapid back to 1st position) ; S900 M03 (Spindle on CW) ; G43 H03 Z0.1 (Tool offset 3 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; G84 Z-0.6 R0.2 F56.25 (Begin G84) ; M98 P40011 (Call external subprogram) ; G80 G00 Z1. M09 (Cancel canned cycle) ; (BEGIN COMPLETION BLOCKS) ; G00 Z1. M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

```
% O40011 (M98_Subprogram X,Y Locations) ; X1.115 Y-2.75 (2nd position) ; X3.365 Y-2.875 (3rd position) ; X4.188 Y-3.313 (4th position) ; X5. Y-4. (5th position) ; M99 ; %
```

## 5.54 External Subprograms With Multiple Fixtures (M98)

Subprograms can be useful when cutting the same part in different X and Y locations within the machine. For example, there are six vises mounted on the table. Each of these vises uses a new X, Y zero. They are referenced in the program using the G54 through G59 work offsets in absolute coordinates. Use an edge finder or an indicator to establish the zero point on each part. Use the part zero set key in the work offset page to record each X, Y location.  Once  the  X,  Y  zero  position  for  each  workpiece  is  in  the  offset  page,  the programming can begin.

The figure shows what this setup would look like on the machine table. For an example, each of these six parts will need to be drilled at the center, X and Y zero.

## Main Program

```
% O40012 (M98_External sub multi fixture); (G54-G59 X0 Y0 is center of each part) ; (G54-G59 Z0 is on top of the part) ; (T1 is a drill) ; (BEGIN PREPARATION BLOCKS) ; T1 M06 (Select tool 1) ; G00 G90 G40 G49 G54(Safe startup) ; X0 Y0 (Rapid to 1st position) ; S1500 M03 (Spindle on CW) ; G43 H01 Z0.1 (Tool offset 1 on) ; M08 (Coolant on) ; (BEGIN CUTTING BLOCKS) ; M98 P40013 (Call external subprogram) ; G55 (Change work offset) ; M98 P40013 (Call external subprogram) ; G56 (Change work offset) ; M98 P40013 (Call external subprogram) ; G57 (Change work offset) ;
```

```
M98 P40013 (Call external subprogram) ; G58 (Change work offset) ; M98 P40013 (Call external subprogram) ; G59 (Change work offset) ; M98 P40013 (Call external subprogram) ; (BEGIN COMPLETION BLOCKS) ; G00 Z0.1 M09 (Rapid retract, Coolant off) ; G53 G49 Z0 M05 (Z home, Spindle off) ; G53 Y0 (Y home) ; M30 (End program) ; %
```

## F5.30: Subprogram Multiple Fixture Drawing

<!-- image -->

## Subprogram

```
% O40013 (M98_Subprogram) ; X0 Y0 (Move to zero of work offset) ; G83 Z-1. Q0.2 R0.1 F15. (Begin G83) ; G00 G80 Z0.2 M09 (Cancel canned cycle) ; M99 ; %
```

## 5.55 More Information - Programming

For the most current Programming Chapter scan the code below with your mobile device:

F5.31:

Mill Interactive Operator's Manual - Programming Chapter

<!-- image -->