"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# TODO: import from local util_datafun_logger.py 

# TODO: Call the setup_logger function to create a logger and get the log file name

# TODO: Create some shared data lists if you like - or just create them in your functions

list1 = [1, 5, 3, 7, 40, 24, 30, 14, 23, 150, 100, 97, 13, 66, 179, 12, 54, 7, 23, 125]
listx = [30, 87, 65, 45, 77, 84, 35, 56, 47, 48]
listy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: define some custom functions

mean_list1 = statistics.mean(list1)

logger.info(f" The average sale is {mean_list1}")

median_list1 = statistics.median (list1)

logger.info (f" The median of sales is {median_list1}")

mode_list1 = statistics.mode (list1)

logger.info(f" The mode of the sales is {mode_list1}")

stdev_list1 = statistics.stdev (list1)

logger.info(f" The standard deviation of sales is {stdev_list1}")

variance_list1 = statistics.variance(list1)

logger.info(f" The variance of sales is {variance_list1}")

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Replace this with calls to your functions." )



