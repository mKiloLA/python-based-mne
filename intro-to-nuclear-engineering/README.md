# NE 495: Intro to Nuclear Engineering

This repository contains three problems, two homework questions and one exam question, that could be given as assignments in Intro to Nuclear Engineering. A skeleton to be given to students as well as a solution for instructors is provided. The skeleton contains the problem statement and the necessary imports for generating a solution.

These questions make use of three different libraries for constants, attenuation coefficients, and elemental properties. While the current use of these libraries are not consistant, the proposed solution would wrap around these packages and create functions that have consistant usage. The solution to [homework_20](../intro-to-nuclear-engineering/homework_20/homework_20_solution.ipynb) has a function `get_attenuation_co` that demonstrates how a wrapper library might make for easy use of different tables.

## Files in the Repository

* [homework_20](../intro-to-nuclear-engineering/homework_20/)
  * [homework_20_skeleton.ipynb](../intro-to-nuclear-engineering/homework_20/homework_20_skeleton.ipynb): Starting file to be given as an assignment description to students.
  * [homework_20_solution.ipynb](../intro-to-nuclear-engineering/homework_20/homework_20_solution.ipynb): One possible solution for Homework 20 questions 1 and 2.
* [exam_1](../intro-to-nuclear-engineering/exam_1/)
  * [exam_1_skeleton.ipynb](../intro-to-nuclear-engineering/exam_1/exam_1_skeleton.ipynb): Starting file to be given as an assignment description to students, or in this case, as part of an exam.
  * [exam_1_solution.ipynb](../intro-to-nuclear-engineering/exam_1/exam_1_solution.ipynb): One possible solution Exam 1 question 9.

## Software Requirements

Since this assignment would be completed by students, the following software would need to be installed by each student:

* Applications
  * Python 3
  * Visual Studio Code
* Python Packages
  * scipy
  * numpy
  * mendeleev
  * physdata
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
