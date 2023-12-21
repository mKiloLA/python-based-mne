# ME 400: Computer Applications in Mechanical Engineering

This repository contains what would be the concluding assignment in a string of exercises working towards the creation of a Simon Says game. This project is a direct translation of an existing assignment in ME 400 that utilizes the ESP32 and several other circuit components. With that being said, the students do not do any circuit building. Everything is plug-and-play thanks for PCBs designed by the instructors of the class. No circuit board was designed for this project, so the wirings were all done by hand. Because of this, the project description will still show an ESP32 despite using the Raspberry Pi Pico.

## Files in the Repository

* [exercise_07](../computer-applications-in-me/exercise_07)
  * [exercise_07_assignment.pdf](../computer-applications-in-me/exercise_07/exercise_07_assignment.pdf): This file contains the project description and instructions. It is largely a translation of the original assignment.
  * [exercise_07_skeleton.py](../computer-applications-in-me/exercise_07/exercise_07_skeleton.py): This file contains the code to be given to students as a starting point. They will have already written this code as part of doing previous exercises, but it is convinient to give every student the same starting point each project.
  * [exercise_07_solution.py](../computer-applications-in-me/exercise_07/exercise_07_solution.py): This file contains a working solution to Exercise 7 and the Simon Says game.
  * [lcd_display_driver.py](../computer-applications-in-me/exercise_07/lcd_display_driver.py): This file contains the code needed to operate the LCD display. This file must be saved on the Pico's local file system for any other code file to make use of it. Being in the same folder on the PC will not be sufficient, even if you are running the main file from the PC.
  * [ir_remote_driver.py](../computer-applications-in-me/exercise_07/ir_remote_driver.py): This file contains the code needed to interact with the IR remote. This file must be saved on the Pico's local file system for any other code file to make use of it. Being in the same folder on the PC will not be sufficient, even if you are running the main file from the PC.
  * [fonts](../computer-applications-in-me/exercise_07/fonts/): This folder contains different fonts available to the LCD display drivers. This folder, as well as the fonts that are going to be used, must be saved on the Pico's local file system for any other code file to make use of it. Being in the same folder on the PC will not be sufficient, even if you are running the main file from the PC. This assignment only makes use of the [EspressoDolce18x24.c](../computer-applications-in-me/exercise_07/fonts/EspressoDolce18x24.c) font.

## Software Requirements

Since this assignment would be completed by students, the following software would need to be installed by each student:

* Applications
  * Python 3
  * Visual Studio Code
* Visual Studio Code Extensions
  * Python
  * Pylance
  * MicroPico
  * IntelliCode
  * IntelliCode API Usage Examples
  * vscode-pdf

For more information about the installation of any of these packages, see [Usage and Installation](../usage_and_installation/).
