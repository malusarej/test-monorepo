**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Change Pixel Color on Mouse Left-Click

**Primary Actor**: User

**Goal in Context**: The primary actor, a User, intends to change the pixel color on the drawing canvas by left-clicking the mouse at a specific location, facilitating a drawing action similar to using a pencil on a piece of paper.

**Preconditions**: (1) The drawing application is running and accessible. (2) The drawing canvas is displayed and ready for user interaction.

**Trigger**: The user initiates a left-click with the mouse.
  
**Scenario 1**: The user launches the drawing application.

**Scenario 2**: The application displays a drawing canvas.

**Scenario 3**: The user positions the mouse cursor at a specific location on the canvas where they want to change the pixel color.

**Scenario 4**: The user initiates a left-click action on the canvas.

**Scenario 5**: The application recognizes the left-click event.

**Scenario 6**: The application determines the current selected drawing color (e.g., based on a previous color selection).

**Scenario 7**: The application changes the pixel color at the clicked location to the selected color, allowing the user to draw or make edits.

**Scenario 8**: The user can continue dragging and left-clicking to draw or edit on the canvas.

**Exceptions**: (1) The user might initiate a click outside the boundaries of the canvas and in that case the application does not perform any drawing action and informs the user to click within the canvas area. (2) If there is an error in recognizing the selected color, then the application defaults to a predefined color or prompts the user to select a color before proceeding with drawing.

**Priority**: High-priority

**When available**: Present in the initial release.

**Channel to actor**: The user interacts with the application through the graphical user interface (GUI) using the mouse to trigger the pixel color change action.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: None

**Open Issues**: We may need to implement more complex color pickings and introduce concepts like shading etc.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
