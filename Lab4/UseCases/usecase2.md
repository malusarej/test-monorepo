**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**:  Change Drawing Color

**Primary Actor**: User

**Goal in Context**: The primary actor, a User, wants to select a specific color for drawing in the mini-paint application.

**Preconditions**: (1) The mini-paint application is running and accessible. (2) The user interface with the available color options is displayed.

**Trigger**: The user presses one of the number keys (1 through 8) to select a color.
  
**Scenario 1**: The user launches the mini-paint application.

**Scenario 2**: The application displays a drawing canvas and a color palette with the following options:
                        1 = Black
                        2 = White
                        3 = Red
                        4 = Green
                        5 = Blue
                        6 = Yellow
                        7 = Magenta
                        8 = Cyan

**Scenario 3**: The user presses one of the number keys (1 through 8) corresponding to the desired color.

**Scenario 4**: The application recognizes the user's input and selects the chosen color for drawing.

**Scenario 5**: The selected color is visually indicated to the user, such as by highlighting the chosen color on the palette

**Scenario 6**: The user can now draw on the canvas using the selected color.
 
**Exceptions**: The user might press an invalid key or a key that does not correspond to a color (e.g., a key outside the range 1 through 8) and we can remedy that by having the application not change the drawing color, and the user is informed with an error message.

**Priority**: Medium

**When available**: Present in the initial release.

**Channel to actor**: The user interacts with the application through the graphical user interface (GUI), using the keyboard to select the desired color.

**Secondary Actor**: None

**Channels to Secondary Actors**: None

**Open Issues**: Need to provide a user guide for color selection.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
