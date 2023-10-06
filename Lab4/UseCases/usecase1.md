**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>

**Use Case**: Set Window and Canvas Dimensions

**Primary Actor**: System Configuration

**Goal in Context**: The primary actor aims to configure the window and drawable canvas to specific dimensions.

**Preconditions**: (1) The system is initialized and ready for configuration. (2) The primary actor has the necessary permissions to modify the window and canvas dimensions.

**Trigger**: System configuration settings are being adjusted.
  
**Scenario 1**: The primary actor, "System Configuration," selects the "Configure Dimensions" option in the system settings menu.

**Scenario 2**: The system presents a configuration interface.

**Scenario 3**: The secondary actor, the "User," specifies the desired width and height for the window and drawable canvas, setting them to 600 pixels wide and 400 pixels high.

**Scenario 4**: The "User" confirms the configuration settings.

**Scenario 5**: The system validates the dimensions to ensure they are within acceptable limits and feasible for the current environment.

**Scenario 6**: If the dimensions are valid, the system applies the new dimensions to the window and drawable canvas.

**Scenario 7**: The system updates the display to reflect the new dimensions.

**Exceptions**: User can input dimensions that are unrealistic. If the specified dimensions are outside the acceptable limits (e.g., too large for the hardware), the system displays an error message. The user can then resubmit more correct dimensions.

**Priority**: Medium-priority

**When available**: Targeted for the next software release.

**Channel to actor**: The primary actor, "System Configuration," interacts with the system through the Graphical User Interface (GUI), using input devices such as a keyboard and mouse to navigate the configuration interface and enter the desired dimensions.

**Secondary Actor**: User

**Channels to Secondary Actors**: The "User" interacts with the system through the same Graphical User Interface (GUI) to provide input and confirm configuration settings.

**Open Issues**: It is not clear if the system should automatically save the configured dimensions or if the "User" should explicitly save them.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
