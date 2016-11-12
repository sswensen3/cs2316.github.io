---
layout: homework
title: Homework 7
---

# Homework 7

## Introduction

In this homework you will practice writing GUI applications.

## Problem Description

You will be coding a Connect 4 game! For reference on how a Connect 4 game looks and operates, visit https://www.mathsisfun.com/games/connect4.html.

This assignment must be completely implemented with Object Oriented Programming and must use the Tkinter GUI module! Assignments that do not compile will get minimal to 0 points.

In addition, you must implement error checking for invalid input when applicable.

## Helpful Resources
Most of the relevant Tkinter GUI widgets have been discussed in lecture slides (available on the course website) and lecture code (posted on T-Square). However, the following websites are useful to learn more about Tkinter:
- [Tkinter documentation](https://docs.python.org/3/library/tk.html) (official Python documentation)
- [effbot.org](http://effbot.org/tkinterbook/) (some code here may be out of date, but has some good examples and descriptions of widgets)

## Solution Description
You must define a class called GUI and the `__init__` method must open a Home Screen GUI. Your code should have a main method that instantiates a GUI object and runs mainloop. How you choose to implement this is up to you and you must write a brief README file to explain what you did. If you use any images, the image files must be submitted with the assignment so the TAs can grade your homework.
Your Connect 4 game should have the following properties:

### Home Screen GUI:
1. Must have at least one Radiobutton to choose the game to play. The user will choose a game and the game grid will reflect their choice. If you implement the extra credit games, add them as options (i.e., Radiobuttons), but even if you implement only Connect 4 you need to have at least one Radiobutton. 
2. Must have an Entry input for each player's name. (If left blank, the game will continue with a generic player name such as "Player 1" or "P1").
3. Must have a start Button that will close the Home Screen GUI window and open the Game Board GUI window. (Note: Start button must be deactivated until the user has selected a game to play.)
4. The user should be able to easily identify the functionality of each of the widgets.

### Game Board Screen:
1. Must display each player's name and score at the top. The score is the number of games the player has won.
2. Must indicate which player's turn it is
3. Must display a bordered grid of 6x6 squares (Hint: use Labels) for Connect 4
4. Each player's game piece must be a different color (you can make these either text or symbols)
5. Must allow the current player to select a column in which to play a game piece (selection can be determined by a Combobox, simple clicking, Buttons, etc. Make sure to explain in your README.)
6. Game pieces must not overlap and must be inserted directly above other game pieces in the same column (Game pieces must not "float" in the middle of the game board)
7. Must display an error messagebox if a column is full of game pieces or if no column is selected. This does not end the player's turn.
8. Must have a "Quit" Button that first opens a messagebox to ask the user if they are sure they want to quit (hint: messagebox.askyesno). If a user chooses to quit, the Game Board Screen must close and the Home Screen must open. If the user does not choose to quit, the game should resume where it left off.

### Winner Checking:
9. The winner must be identified as soon as they win and a messagebox must pop up to ask if the players would like to play again (hint: messagebox.askyesno).
10. If the user chooses to play again, the game board should be cleared and the players’ scores should be updated to reflect the results of the previous game(s). If the user does not choose to play again, the Game Board Screen must close and the Home Screen should open. 
11. Each direction should be checked to determine if the current player has just won (i.e., down, left, right, diagonal down and left, diagonal down and right)
12. If no player has won and the Game Board fills up with pieces, a messagebox should pop up to inform the user that the game was a draw and ask if they would like to play again (see #9). Neither player should earn a winning point in this case.

### Extra Credit (Up to the Discretion of Grading TA):
- (+20 points) Tic Tac Toe
	* for reference: https://www.exploratorium.edu/brain_explorer/tictactoe.html 
- (+10 points) if images are used as game pieces in Connect 4 or Tic Tac Toe
	* for reference: http://effbot.org/tkinterbook/photoimage.htm 
- (+10 points) Creativity (formatting, colors, extra functionality, etc.)## 
- (+20 points) Connect 5 level (8x8 grid, 2 players, and wins determined by 5 in a row)
- (+20 points) Connect 4 with 3 players
- (+20 points) Scoreboard :The ScoreBoard should be a GUI window that records all of the scores from the winning players in ALL games and displays them from highest score to lowest score.

Explain all Extra Credit in your README!

### What is expected:
1. You must implement Connect 4 CORRECTLY to get 100/100
2. Connect 5, Connect 4 with 3 players, and Tic Tac Toe are all EXTRA CREDIT

## Suggested Solution Outline
The following is a suggested outline of a solution for this assignment. These methods are provided to you as a starting point. You are encouraged to write additional methods and/or substitute different methods for those seen below.

```Python
class GUI:
    def __init__(self, rootwin):
        """Create the Home Screen GUI. The Home Screen must have at least one 
        radio button to choose a game to play (even if you only implement
        Connect 4!) The GUI must have at least two entry boxes so players
        can input their names and there should be labels next to the entries
        to let the user know what they are for. If a user leaves an entry blank,
        the player should have a default name like "Player 1" or "P1" and NOT
        an empty string. The Home Screen GUI must also have a "Start"
        button that should be deactivated until the user chooses a game from
        the radio buttons. The Start button must hide the Home Screen
        and open the Game Board Screen (i.e., command=game_board).

        Parameters:
        rootwin: Tk window passed in as the root window
        """
```
```Python
    def game_board(self):
        """Create the Game Board Screen GUI using a TopLevel of the root Home
        Screen GUI. The GUI must display each player's name and score at the top.
        The score is the number of games the player has won. There should also be
        a label that indicates whose turn it is. For Connect 4, the Game Board must
        be a 6x6 grid of bordered labels. (You may want to save these labels in a nested 
        list so you can update them when players play. You may also want to save which 
        player played a game piece in that location.) The current player must be able 
        to select a column to play a "game piece". (This can be achieved by using 
        OptionMenu, simple clicking, buttons, etc. and should be explained in your README.) 
        Each player's game piece must be a different color and they can be labels with 
        symbols, text, or even images (if you use images correctly, you will get extra 
        credit). Game pieces must not overlap and must be inserted directly above other 
        game pieces in the same column (i.e., pieces must not "float" in the middle of 
        the Game Board). If a column is full or if no column is selected then an error 
        messagebox must tell the user to choose an appropriate column. (This should not 
        end the current player's turn!) The GUI must have a "Quit" button that first opens
        a messagebox to ask the user if they are sure they want to quit (using
        messagebox.askyesno). If a user chooses to quit, close the Game Board Screen
        and open the Home Screen. If the user does not choose to quit, the game should
        resume where it left off.
        """

    def play(self):
        """When a user selects a column in the Game Board Screen, play() should be called.
        This function should change the label corresponding to the appropriate location
        of the game piece that was played. It should also check if a player has won. The
        winner should be identified in a messagebox as soon as they win and the user must
        be asked if the players would like to play again using a messagebox.askyesno. If
        the user chooses to play again, the Game Board Screen should be reset and the
        players' scores must reflect the results of the previous game(s). If the user
        chooses not to play again, the Game Board Screen must close and the Home Screen
        should open. If the Game Board fills up with pieces and no player has won, a
        messagebox should pop up to inform the user and askl if they would like to play
        again. Neither player should earn a point in this case. NOTE: See checkwin() 
        for one possible way of checking if a player has won. You can call it in play().
        """

    def check_win(self, cur_row, cur_col):
        """Checks each direction to determine if the current player has just won. The
        directions to check are down, left, right, diagonal left and down, and diagonal
        right and down.

        Parameters:
        cur_row: integer representing the row of the game piece that was just played
        cur_col: integer representing the column of the game piece that was just played

        Return:
        won: bool -- True if the currentPlayer has won, False otherwise
        """
```
```Python
def main(args):
    """Must create a Tk window to pass into an instance of the GUI class and run
    the mainloop() on it."""
```

## Example GUI Layouts
Below are sample layouts for the Home Screen and Game Board Screen GUIs. Your GUIs do not need to look exactly like these, feel free to customize your GUI layouts as long as they are organized.

![Home Screen](http://cs2316.gatech.edu/fall2016/hw7/start_screen.png "Start Screen")

![Game Board](http://cs2316.gatech.edu/fall2016/hw7/game_board.png "Game Board")
![Game Board](http://cs2316.gatech.edu/fall2016/hw7/game_board2.png "Game Board")


## Grading Rubric
**Home Screen GUI [15]**
- Radio Button (5)
	* (2) radio button present 
	* (3) radio button is linked to a variable that identifies the game to play (3)
- Entries (5)
	* (1) labels indicate what players should type in where
	* (1) entries present
	* (2) text from entries correspond to names of players in the game
	* (1) player's name defaults to generic player title if entry left blank
- Start Button (5)
	* (2) deactivated until game is selected
	* (3) hides the Home Screen and displays the GameBoard Screen when clicked
	
**(-5) if GUI has all elements but in a confusing or disorganized layout**



**Connect 4 GUI [85]**
- GUI elements (15)
	* Initial Labels (5)
		- (3) players names and scores are displayed
		- (2) current player's turn is indicated
	* Grid (5)
		- (3) labels gridded correctly
		- (1) labels have borders
		- (1) grid is 6x6
	* Quit Button (5)
		- (1) Button present
		- (2) When clicked, button asks user if they would like to quit with messagebox
		- (2) Quits if user clicks Yes, continues the game otherwise
- Game Play (70)
	* Column Selection (15)
		- (5) follows README description
		- (10) column selection works
	* Player's turn label is updated to reflect current player's turn (5)
	* Game pieces are distinguishable (2)
	* Pieces are played in the correct location (10)
		- (3) column is correct
		- (7) row is correct
	* Winner Checking (30)
		- each direction is checked correctly
			* (5) down 
			* (5) left
			* (5) right
			* (5) diagonal down and left
			* (5) diagonal down and right
		- (3) Winner is determined as soon as they win
		- (2) Messagebox tells user when someone wins
	* Game Board After Win (5)
		- (2) Game Board reset after winner determined and user chooses to play again
		- (3) Game Board reflects players scores after winner is determined
	* Error Checking (8)
		- (3) Error messagebox works if column is full or if no column is selected
		- (5) Full game board handled correctly (messagebox pops up and asks if user would like to play again and neither player gets point)
	* Game successfully closes and returns to Home Screen when user chooses not to play again (5)
	* main() correctly instantiates object of the GUI class using a Tk() window (5)

**(-5) if GUI has all elements but in a confusing or disorganized manner**

**NOTE: TAs can take off points for errors not listed above (e.g., miscellaneous syntax errors, runtime errors)**



**Extra Credit [100]:**
- Tic Tac Toe (+20)
	* (+10) Playing functionality works according to the rules of Tic Tac Toe (i.e., 3x3 grid, players take turns choosing a grid location to play, each player's game piece is a different symbol/image) and implementation is explained in README
	* (+5) Winning Functionality (handles a win or tie)
	* (+5) Keeps track of scores and turns in the same way Connect 4 does
- Connect 5* (+20)
	* must have same functionality as Connect 4, but grid must be 8x8 and the winner is determined after 5 pieces from the same player are played in a row
- Connect 4 with 3 Players* (+20)
	* must have same functionality as Connect 4, but must include a third player with a distinguishable game piece
- Use of Images as Game Pieces (+10)
- Creativity including extra formatting, functionality, colors, etc. (up to discretion of grading TA) (+10)
- Scoreboard (+20)
	* (+5) GUI looks like a scoreboard (see example image of a game scoreboard)
		- ![Game Board](http://cs2316.gatech.edu/fall2016/hw7/scoreboard.gif "Scoreboard")
	* (+10) winning players and number of wins (i.e., score) recorded
	* (+5) players in order of highest score to lowest score

**Only attempt Connect 5 and Connect 4 with 3 players if you have successfully completed Connect 4.**


## Submission Instructions
Turn in the following files:

1. hw7.py
2. README.txt
3. any images you used


## Verify Your T-Square Submission!

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

- After uploading the files to T-Square you should receive an email from T-Square listing the names of the files that were uploaded and received. If you do not get the confirmation email almost immediately, something is wrong with your HW submission and/or your email. Even receiving the email does not guarantee that you turned in exactly what you intended.
- After submitting the files to T-Square, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the T-Square Assignment page placing them in a new folder.
- Re-run and test the files you downloaded from T-Square to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps insure that you turn in the correct files.
    - It helps you realize if you omit a file or files. Missing files will not be given any credit, and non-compiling homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute! (If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
