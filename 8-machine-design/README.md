# ME 533: Machine Design

The repository contains two questions from a homework and focus on solving and graphing beam loadings using singularity functions. The reaction forces and beam inertia are solved using SymPy and an .ipynb, but the equation creation and plotting are handled by a purpose built GUI. This application can be run from the terminal (or using Python, as shown in the skeleton and solution) and allows for students to easily create and edit beam loadings to see the deflection, slope, moment, and shear diagrams.

This singularity solver could be accessed directly through Python, rather than using the GUI. However, this would require a thorough understanding of the library and its structure, which may be overbearing. With some modifications and testing, a better API could be developed to allow for easier use. Also worth noting, the solver is missing several features that would be nice to have, such as the ability to directly enter inertia values, select different cross sections, and solve for reaction forces. While these could certainly be added later, they fall outside the proof of concept that this repository aims to achieve.

## Files in the Repository

* [homework](./homework/)
  * [homework_skeleton.ipynb](./homework/final_exam_skeleton.ipynb): Starting file to be given as homework questions in machine design.
  * [homework_solution.ipynb](./homework/final_exam_solution.ipynb): Potential solution to the homework questions.
  * [question_images](./homework/question_images/): Diagrams showing the beam loading for the problem statements.
  * [solution_images](./homework/solution_images/): Images showing the resulting graphs and equations.
  * [MNE/machine_design](./homework/MNE/machine_design): Module containing the GUI that students would use to get plots and equations.
    * [singularity](./homework/MNE/machine_design/singularity/): Module that contains the application code for the singularity solver and plotter.

## Software Requirements

Since this assignment would be completed by students, the following software would need to be installed by each student:

* Applications
  * Python 3
  * Visual Studio Code
* Python Packages
  * sympy
  * matplotlib (used in MNE package)
* Visual Studio Code Extensions
  * Python
  * Pylance
  * Jupyter
  * Jupyter Keymap
  * Jupyter Notebook Renderers
  * Jupyter Cell Tags
  * Jupyter Slide Show
  * IntelliCode
  * IntelliCode API Usage Examples

To solve the question in the same manner as the solution, students would also need to download the MNE module (which would likely be provided on Canvas) and place it in the project root directory. There may also be additional modules that need to be installed with the MNE module.

For more information about the installation of any of these packages, see [Usage and Installation](../usage-and-installation/).
