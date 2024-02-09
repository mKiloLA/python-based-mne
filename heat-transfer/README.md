# ME 573: Heat Transfer

The repository contains one assignment to be given as a design project to students. Both a skeleton and a solution are provided. The skeleton contains the problem statements and the recommended structure for the results. 

Rather than utilizing open source libraries, this project uses a custom `MNE` library that replicates the contains a small example of what a full MNE module would contain. This question can be solved without the library using table data from a textbook (which is the source of the property information in the MNE module) or using multiple other libraries, such as `ht`, `fluids`, and `pyromat`.

## Files in the Repository

* [project](../heat-transfer/project/)
  * [project_skeleton.ipynb](../heat-transfer/project/project_skeleton.ipynb): Starting file to be given as a heat exchanger design project description to students.
  * [project_solution.ipynb](../heat-transfer/project/project_solution.ipynb): Potential solution to the heat exchanger design project.
  * [MNE](../heat-transfer/project/MNE/): Module containing property data and equations.
    * [heat_transfer.py](../heat-transfer/project/MNE/heat_transfer.py): File containing the heat transfer specific data.
    * [\_\_init__.py](../heat-transfer/project/MNE/__init__.py): Empty file needed to make the MNE folder a module.

## Software Requirements

Since this assignment would be completed by students, the following software would need to be installed by each student:

* Applications
  * Python 3
  * Visual Studio Code
* Python Packages
  * pandas
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

To solve the question in the same manner as the solution, students would also need to download the MNE module (which would likely be provided on Canvas) and place it in the project root directory.

For more information about the installation of any of these packages, see [Usage and Installation](../usage-and-installation/).
