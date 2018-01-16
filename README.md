# Name: pd_test

# About
This repository contains Python test code for a Test Engineer Automation role at company called PD. The application will print out information related to lists to stdout.


# Contents
PerspectumDiagnostics.py - methods for the application
tests/test_perspectuamDiagnostics.py - unit tests for the application


# Versions and Environment
Python Version - 2.7.13
Use a python virtual enviornment

# How to use this repository

Git clone this repository
```
git clone <repository_name_goes_here >
```

# Application execution
```
# Import the methods
from PerspectumDiagnostics import perspectum_diagnostics_test as pdt

#call the method

       # input list of lists
       test_list_in = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]

       # method call
       pdt(test_list_in)


```

# Expected Output
```
Strings appearing in multiple lists: ‘gh’
Number of unique strings: 7
Total number of strings processed: 9
```