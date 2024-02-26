# DEN 161: Engineering Problem Solving

## Instructor's Guide

This repository contains in-class examples for using Excel and Python to analyze tire RPM data. It also contains homework homework questions that correlate to the tire RPM examples. These files serve as an example to show the benefits of using a programming language, like Python, over Excel.

The repository also has the code needed to make a stoplight using a Raspberry Pi Pico. This is a microcontroller project intended to introduce students to basic circuit compenents and embedded programming. No problem statement is given for this project because no changes have been made to the original assignment.

## Files in the Repo

* [assignment-1](../3-engineering-problem-solving/assignment-1/): Tire RPM Example
  * [python_rpm_example.ipynb](../3-engineering-problem-solving/assignment-1/python_rpm_example.ipynb): a solution to the in-class tire RPM question using Python as the solver.
  * [tire_rpm_example_solution.xlsx](../3-engineering-problem-solving/assignment-1/tire_rpm_example_solution.xlsx): a solution to the in-class tire RPM question using Excel as the solver.
  * [tire_rpm_example.csv](../3-engineering-problem-solving/assignment-1/tire_rpm_example.csv): a data file that contains RPM data for a car wheel. Use this data for the example questions.

* [assignment-2](../3-engineering-problem-solving/assignment-2/): Tire RPM Homework
  * [python_rpm_homework.py](../3-engineering-problem-solving/assignment-2/python_rpm_homework.py): a Python script to be handed to students as a homework question. They are responsible for adding an input statement for the tire diamter, changing the data file, and adding comments.
  * [python_rpm_homework_solution.py](../3-engineering-problem-solving/assignment-2/python_rpm_homework_solution.py): a Python script that solves the tire RPM homework question. This could also be done in a Jupyter Notebook, but I chose to do it in a Python script. This also contains the solution to the extra credit question.
  * [tire_rpm_homework_solution.xlsx](../3-engineering-problem-solving/assignment-2/tire_rpm_homework_solution.xlsx): an Excel file that solves the ture RPM homework question.
  * [tire_rpm_homework.csv](../3-engineering-problem-solving/assignment-2/tire_rpm_homework.csv): a data file that contains RPM data for a car wheel. Use this data for the homework questions.

* [assignment-3](../3-engineering-problem-solving/assignment-3/): Stoplight Project
  * [example.py](../3-engineering-problem-solving/assignment-3/example.py): LED flashing program for the RPi Pico. This file is intended to be used as the in-class example for the stoplight project and the base code provided to the students.
  * [stoplight.py](../3-engineering-problem-solving/assignment-3/stoplight.py): this is a potential solution to the Stoplight Activity. Many different variations of this file could exist.
  * [sos.py](../3-engineering-problem-solving/assignment-3/sos.py): this is an example of using morse code with the Pico.

## Software Requirements

Since this assignment would be completed by students, the following software would need to be installed by each student:

* Applications
  * Python 3
  * Visual Studio Code
* Python Packages
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
  * Excel Viewer

For more information about the installation of any of these packages, see [Usage and Installation](../usage-and-installation/).
