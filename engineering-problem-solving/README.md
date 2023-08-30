# DEN 161: Engineering Problem Solving

## Current State

DEN 161 currently teaches two weeks of data analysis using Python packaged by Anaconda in Spyder. This comes directly after two weeks of data analysis using Excel. The class also utilizes an Arduino Uno and the Arduino IDE to program three LEDs as a stoplight.

## Proposed Changes

The two weeks of Python in Spyder will be switched to using Visual Studio Code. This change is made for three primary reasons:

* Visual Studio Code is the industry standard for code developement. This means it has the highest level of support for both extensions and bug fixes.
* Anaconda is a package of Python that includes many data-analytics and machine learning focused packages. While this can be convenient, it adds a layer of confusion to new users regarding the difference between Python/Anaconda/Spyder that could be avoided.
* Visual Studio Code has an extension made for microPython. While an more user-friendly IDE for the Raspberry Pi Pico does exist, the ability to use one environment for both Python and microPython makes for a more seamless experience.

The Arduino portion of the class will transition to use Raspberry Pi Picos with microPython. This change brings consistency to both the language and environment used in the Python section of the class. The Pico also comes with the benefit of being cheaper, holding multiple files at a time, and having a faster processor.

## Files in the Repo

* `intro_to_python.ipynb`: a Jupyter Notebook that walks through a data analytics problem without using any libraries. This file is intended to be part of the bridge from Excel to Python. Two .csv files have been prepared for the purpose of showing how much easier repeat runs are with programming instead of Excel.
* `intro_to_python_lib.ipynb`: a Jupyter Notebook that walks through a data analytics problem while using libraries. This file is intended to be part of the bridge from Excel to Python. Two .csv files have been prepared for the purpose of showing how much easier repeat runs are with programming instead of Excel.
* `intro_to_python.py`: a Python script that has the same functionality as intro_to_python_lib.ipynb. Purpose is to show how little code is needed. The Jupyter Notebook may seem unwieldy because of the documentation and comments.
* `tire_rpm.csv/tire_rpm_2.csv`: two csv files with wheel rpm data. Intended to be used to show data analytics for Excel and then Python. Only need to change the file name in Python to use a different file.
* `main.py`: light flashing program for the RPi Pico. This is the default file for the Pico that will flash three LEDs.
* `sos.py`: program that flashes LEDs in the morse code pattern for SOS.
* `stoplight.py`: program to make the LEDs emulate a stoplight.
