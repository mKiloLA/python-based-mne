# DEN 161: Engineering Problem Solving

## Instructor's Guide

This repository contains in-class examples, assignments, and solutions for data analysis in Excel, data analysis in Python, and programming the Raspberry Pi Pico. It also contains an installation guide, source code for the custom extension pack, and videos walking through the setup and completition of the different assignments. I will lead with the intended schedule and then walk through each file in the repository.

## Schedule

* **Step 1**: Introduction to Excel
  * No changes were made to the existing Excel introduction.

* **Step 2**: Introduction to Python
  * No changes were made to the existing Python introduction.

* **Step 3**: Data Analysis with Excel
  * **In-Class Example**: Using the data in [tire_rpm_excel.csv](intro_to_excel\tire_rpm_excel.csv), find the maximum, minimum, mean, median, and mode speed of the vehicle. Assume a tire diameter of 20 inches. Graph the speed of the vehicle at any given time.
  * **Homework**: Have students repeat the process using [tire_rpm_homework.csv](intro_to_excel\tire_rpm_homework.csv) as their data and 18" wheels. Graph the speed of the vehicle at any given time. This should be a 1-to-1 copy of what was done in class, just with different numbers.

* **Step 4**: Data Analysis using Python
  * **In-Class Example**: Using the data in [tire_rpm_example.csv](intro_to_python/tire_rpm_example.csv) and the Jupyter Notebook [python_rpm_example.ipynb](intro_to_python\python_rpm_example.ipynb), find the maximum, minimum, mean, median, and mode speed of the vehicle. Assume a tire diameter of 20 inches. Graph the speed of the vehicle at any given time. This should give identical solutions to the Excel problem.
  * **Homework**: Have students create a .py file that finds the maximum, minimum, mean, median, and mode speed of the vehicle using [tire_rpm_homework.csv](intro_to_python/tire_rpm_homework.csv). Assume a tire diameter of 18 inches. Graph the speed of the vehicle at any given time.
    * **Extra Credit**: How long did it take this car with 22" wheels to go 0-60 if the sensor data was taken at 300Hz?

* **Step 5**: Programming the RPi Pico
  * **In-Class Example**: Walk through the code in [example.py](pico\example.py) to show students how to blink the LEDs.
  * **Homework**: Task students with altering the code provided in class to make the LEDs function like a stoplight. A potential solution is provided in [stoplight.py](pico\stoplight.py).
    * **Extra Credit**: Make the LEDs spell your name in morse code. An example of looping morse code is shown in [sos.py](pico\sos.py).

## Files in the Repo

* `installation_guides`
  * [Installation_Guide.pdf](installation_guides\Installation_Guide.pdf): a guide that walks through downloading Anaconda, Visual Studio Code, and the KSU Extensions in Visual Studio Code.

* `intro_to_excel`
  * [tire_rpm_example.csv](intro_to_excel\tire_rpm_example.csv): a data file that contains RPM data for a car wheel. Use this data for the example questions.
  * [tire_rpm_homework.csv](intro_to_excel\tire_rpm_homework.csv): a data file that contains RPM data for a car wheel. Use this data for the homework questions.
  * [tire_rpm_example_solution.xlsx](intro_to_excel\tire_rpm_example_solution.xlsx): a solution to the in-class problem posed in Step 1.
  * [tire_rpm_homework_solution.xlsx](intro_to_excel\tire_rpm_homework_solution.xlsx): a solution to the homework problem posed in Step 1.

* `intro_to_python`
  * [tire_rpm_example.csv](intro_to_python\tire_rpm_example.csv): a data file that contains RPM data for a car wheel. Use this data for the example questions.
  * [tire_rpm_homework.csv](intro_to_python\tire_rpm_homework.csv): a data file that contains RPM data for a car wheel. Use this data for the homework questions.
  * [python_rpm_example.ipynb](intro_to_python\intro_to_python_example.ipynb): a Jupyter Notebook file that walks through solving the in-class example problem. This file is intended to bridge the gap between Excel and Python.
  * [python_rpm_homework.py](intro_to_python\python_rpm_homework.py): a Python script to be handed to students as a homework question. They are responsible for adding an input statement for the tire diamter, changing the data file, and adding comments.
  * [python_rpm_homework_solution.py](intro_to_python\python_rpm_homework_solution.py): a Python script that solves the homework question from Step 2. This could also be done in a Jupyter Notebook, but I chose to do it in a Python script. This also contains the solution to the extra credit question.

* `intro_to_pico`
  * [example.py](intro_to_pico\example.py): LED flashing program for the RPi Pico. This file is intended to be used as the in-class example in Step 3 and the base code provided for the homework.
  * [stoplight.py](intro_to_pico\stoplight.py): this is a potential solution to the Stoplight Activity. Many different variations of this file could exist.
  * [sos.py](intro_to_pico\sos.py): this is an example of using morse code with the Pico. It is not a particularly good solution to the problem, but it does work.

* `ksu_den_161_extension_pack`
  * [package.json](ksu_den_161_extension_pack\package.json): this file contains the code used to create the Extension Package in the Microsoft Marketplace. As it stands, this file (and folder) can be ignored. In the future, an instructor will need to make sure the extension pack stays up to date.

Changes to add input for tire diameter. Give them a py file and add comments, still make the two changes. Do not give students the ipynb just the code in a py file and make them change the file and tire size and then add comments about the functionality. In class quiz questions