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

list1 = [1, 5, 3, 7, 40, 24, 30, 14, 23, 3, 100, 97, 13, 66, 2, 12, 54, 7, 23, 125]
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

# Correlation

correlationxy = statistics.correlation (listx, listy)
logger.info(f" The correlation between list x and list y is {correlationxy}")

# Slope and Intercept 
slope, intercept = statistics.linear_regression(listx, listy)
logger.info(f" The equation of the best fit line is: y = {slope}x + {intercept}")

#Predict

x_max = max(listx)
newx = 15
newy = slope * newx + intercept

logger.info(f" We predict that when x is {newx}, y will be {newy}")

#Lists3. Lists Built in Python Functions

logger.info(f" Info about list 1 using built in functions")

min = min(list1)
max = max(list1)
len = len(list1)
sum = sum(list1)
average = max / min
set = set(list1)
sorted = sorted(list1)
descsorted = sorted(list1, reverse=True)

logger.info(f" The min of list 1 is {min}")
logger.info(f" The max of list 1 is {max}")
logger.info(f" The length of list 1 is {len}")
logger.info(f" The total of list 1 is {sum}")
logger.info(f" The average of the maximum and minimum is {average}")
logger.info(f" The set of list 1 is {set}")
logger.info(f" The list sorted in ascending order is {sorted}")
logger.info(f" The list sorted in reverse is {descsorted}")

#Lists 4 Lists Methods
lst = [12, 75, 23, 5, 2]
#append
lst.append(36)
#extend
lst.extend([32, 6, 5])
#insert
i = 2
newvalue= 22
lst.insert(i, newvalue)
#remove
item_to_remove = 5
lst.remove(item_to_remove)
#count how many times a value appears
count_2 = lst.count(2)
#sort
sort_lst = sorted(lst)
#descending sort
descsort_lst = sorted(lst, reverse=True)
#Copy to a new list
new_lst = lst.copy
#Remove the first item 
first = new_lst.pop(0)
#Remove the last item 
last = new_lst.pop(-1)

#Lists 5 : List Transformations 
logger.info(f"Sales list: {list1}")

sales_less_than_4 = list(filter(lambda x: x < 4, list1))
logger.info(f" Sales less than 4: {sales_less_than_4}")

doubled_sales = list(map(lambda x: math.cbrt(x), list1))
logger.info(f"Doubled sales is {doubled_sales}")

list_value = 3
volume = (list_value * 5 *5)
logger.info(f"The volume of a cube with a side of 3 is {volume}")







# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Replace this with calls to your functions." )



