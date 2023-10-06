**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Clear Canvas

**Primary Actor**: User

**Goal in Context**: The primary actor, a User, wants to clear the entire drawing canvas in a drawing application, filling it with a solid color based on the last selected color.

**Preconditions**: (1) The mini-paint application is running and accessible. (2) The drawing canvas contains existing drawings. (3) The user has previously selected a drawing color.

**Trigger**: The user presses the space key to clear the canvas.
  
**Scenario 1**: The user launches the mini-paint application.

**Scenario 2**: The application displays a drawing canvas containing existing drawings.

**Scenario 3**: The user has previously selected a drawing color (e.g., by pressing a number key).

**Scenario 4**: The user decides to clear the canvas and presses the space key.

**Scenario 5**: The application recognizes the space key press as a request to clear the canvas.

**Scenario 6**: The application removes all existing drawings from the canvas.

**Scenario 7**: The entire canvas is filled with the last selected color, creating a solid-colored canvas.

**Scenario 8**: The user can now start drawing on the cleared canvas using the selected color.
 
**Exceptions**: The user presses the space key when there are no existing drawings on the canvas and a solution for that is the application does not perform any action and informs the user that there is nothing to clear.

**Priority**: Low

**When available**: Present in the initial release.

**Channel to actor**: The user interacts with the application through the graphical user interface (GUI), using the keyboard to trigger the canvas-clearing action.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: None

**Open Issues**: User may accidentally press space key when they don't mean to 

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
