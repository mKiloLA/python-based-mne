# ME 570: Control of Mechanical Systems

This folder contains three lab assignments that could be used to replace current lab assignments of the same name. The lab assignments themselves have not been changed, only the implementation and skeletons have changed. Thanks to the control package and a few custom functions, the Python implementation mimics the equivalent MATLAB implementation very closely. The three chosen labs represent different key features of MATLAB that need to be replicated: transfer functions, plotting, root locus plots, bode plots, and the motorlab.

All three labs make use of the motorlab. While the motorlab originally ran through MATLAB, it has since been turned into a standalone executable which can be found in the [motorlabGUI](../usage-and-installation/motorlabGUI) folder.

## Files in the Repository

* [assignment-1](../9-control-of-mechanical-systems/assignment-1/): Lab 4
  * [Lab4Assign.pdf](../9-control-of-mechanical-systems/assignment-1/Lab4Assign.pdf): Assignment description for Lab 4 as given in ME 570. No changes have been made.
  * [Lab_4_skeleton.ipynb](../9-control-of-mechanical-systems/assignment-1/Lab_4_skeleton.ipynb): Skeleton code to be given to students with the Lab 4 assignment. The provided information is identical to the original skeleton.
  * [Lab_4.ipynb](../9-control-of-mechanical-systems/assignment-1/Lab_4.ipynb): Solution to the Lab 4 assignment.
  * [stepdata.csv](../9-control-of-mechanical-systems/assignment-1/stepdata.csv): Data taken from the motorlab using the motorlabGUI.exe application.
  * [custom_functions.py](../9-control-of-mechanical-systems/assignment-1/custom_functions.py): Custom functions that allow Python to be used more similarly to how MATLAB is used. It currently contains a plotting function that hijacks matplotlib's `plot` and adds data tips.
  * [fig_4.png](../9-control-of-mechanical-systems/assignment-1/fig_4.png): Image showing the data tip customizations on a result from Lab 4.

* [assignment-2](../9-control-of-mechanical-systems/assignment-2/): Lab 10
  * [Lab10Assign.pdf](../9-control-of-mechanical-systems/assignment-2/Lab10Assign.pdf): Assignment description for Lab 10 as given in ME 570. No changes have been made.
  * [Lab_10_skeleton.ipynb](../9-control-of-mechanical-systems/assignment-2/Lab_10_skeleton.ipynb): Skeleton code to be given to students with the Lab 10 assignment. The provided information is identical to the original skeleton.
  * [Lab_10.ipynb](../9-control-of-mechanical-systems/assignment-2/Lab_10.ipynb): Solution to the Lab 10 assignment.
  * [data1.csv](../9-control-of-mechanical-systems/assignment-2/data1.csv): Data taken from the motorlab using the motorlabGUI.exe application.
  * [data2.csv](../9-control-of-mechanical-systems/assignment-2/data2.csv): Data taken from the motorlab using the motorlabGUI.exe application.
  * [data3.csv](../9-control-of-mechanical-systems/assignment-2/data3.csv): Data taken from the motorlab using the motorlabGUI.exe application.
  * [custom_functions.py](../9-control-of-mechanical-systems/assignment-2/custom_functions.py): Custom functions that allow Python to be used more similarly to how MATLAB is used. It currently contains a plotting function that hijacks matplotlib's `plot` and adds data tips.

* [assignment-3](../9-control-of-mechanical-systems/assignment-3/): Lab 13
  * [Lab13Assign.pdf](../9-control-of-mechanical-systems/assignment-3/Lab13Assign.pdf): Assignment description for Lab 13 as given in ME 570. No changes have been made.
  * [Lab_13_skeleton.ipynb](../9-control-of-mechanical-systems/assignment-3/Lab_13_skeleton.ipynb): Skeleton code to be given to students with the Lab 13 assignment. The provided information is identical to the original skeleton.
  * [Lab_13.ipynb](../9-control-of-mechanical-systems/assignment-3/Lab_13.ipynb): Solution to the Lab 13 assignment.

## Software Requirements

Since ME 570 labs are completed in-person, the following software would need to be installed on every computer in the Controls lab:

* Applications
  * Python 3
  * Visual Studio Code
  * motorlabGUI
* Python Packages
  * numpy
  * scipy
  * ipympl
  * ipykernel
  * matplotlib
  * pandas
  * control
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
  * vscode-pdf

For more information about the installation of these packages, see [Usage and Installation](../usage-and-installation/).
