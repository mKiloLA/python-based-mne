# ME 571: Fluid Mechanics

This repository contains one problem that could be given as an assignment in Fluid Mechanics. A skeleton to be given to students as well as a solution for instructors is provided. The skeleton contains the problem statement and the necessary imports for generating a solution.

The solution to problem 4.31 has two different solutions. The first solution only utilizes Python to numerically solve the question at the final step. To do this, three different libraries are used:

* matplotlib: used for plotting to get an intial estimate
* numpy: used for access to the constant e and linsapce for plotting
* scipy: used to numerically solve the problem

The second solution uses Python to take the derivative of the velocity equation rather than solving it by hand. This method also uses three libraries, two of which are scipy and matplotlib for the same reasons mentioned above. In addition to this, the sympy library is used to take the derivative of the velocity equation.

As with previous assignments, these libraries could be incorporated into an MNE library to make it easier for students to access and use these functions and methods.

## Files in the Repository

* [problem_4_31](../fluid-mechanics/problem_4_31/)
  * [problem_4_31_skeleton.ipynb](../fluid-mechanics/problem_4_31/problem_4_31_skeleton.ipynb): Starting file to be given as an assignment description to students.
  * [problem_4_31_solution.ipynb](../fluid-mechanics/problem_4_31/problem_4_31_solution.ipynb): Two possible solutions to problem 4.31 for instructor use.
  * [fig_p4_31.png](../fluid-mechanics/problem_4_31/fig_p4_31.png): Figure used for the problem description in problem 4.31.

## Software Requirements

Since this assignment would be completed by students, the following software would need to be installed by each student:

* Applications
  * Python 3
  * Visual Studio Code
* Python Packages
  * scipy
  * numpy
  * sympy
  * matplotlib
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

For more information about the installation of any of these packages, see [Usage and Installation](../usage-and-installation/).
