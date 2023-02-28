import logging

"read for 2 minutes"

''' Python Exception is represented in class hierarchy using built in or user define exception types
object of the class exception will be created when an exception is raised.
 exception class inherits from the base exception class

 Both the StandardError and Warning inherits from the Exception class.
 
 Standard errors will terminate program if not handle correctly
 Standard error like EOFError results in trying to read beyond the end of a file at run time.
 ZeroDivisionError trying to divide by zero.
 Indentation error improper indentation of programming/code blocks.'''

# An exception is at runtime error which will cause three issues if it is not handled to handle those
# Issues will have to handle the exceptions using try and except block.

"To Do: Predict, then Run, and then Investigate"

# different logging methods and severity

# comment to see what logging level will be displayed in the terminal
logging.basicConfig(level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")


"To Do: Task 1: Modify"
# Modify:
# 1. Change the level from level=logging.DEBUG to logging.INFO, run the code and explain the output from the terminal
# 2. Remove the level=logging.DEBUG or level=logging.INFO, run the code and explain the output from the terminal


# https://docs.python.org/3/library/logging.html
