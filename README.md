# CS 5300 - Advanced Software Engineering
_Software Homeworks_

## Homework 1
Homework 1 contains a series of brief Python coding challenges to test our general knowledge of Python (as we will use this for larger projects later) and our understanding of typical programming concepts.

The homework is comprised of seven tasks, of which each has a numbered python module. Each module contains the necessary functions and/or classes to demonstrate the concept at hand.

The `homework1/tests` directory then contains one pytest module that corresponds to each task and unit-tests its functionality.

`rsc` folders exist in the `homework1` and the `tests` directory for files relating to the tasks and test modules respectively.

`homework1/tests/context.py` contains the boilerplate code to move the current working directory and path to `homework1`, allowing the pytest modules to reference the task modules without performing other system gymnastics. Each pytest module imports the `context` module first, then the relevant task module. If other files from the `tests` directory (like test resources, for example) are needed to perform tests, a call to `context.reset()` will move the cwd and path back to the `tests` directory.

