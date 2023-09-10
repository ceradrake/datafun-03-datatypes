"""
Cera Drake 
9/10/23
Domain: Floral Industry 

"""

# imports first
import random
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)
import math
import statistics

#My lists in the floral industry 
order_type = ["pickup", "delivery", "carryout"]
type_of_flowers = ["gerbera daisy", "rose", "lily", "solidago", "alstromeria", "spider mum"]
payment_type = ["credit card", "check", "cash", "apple pay"]
arrangement_type = ["foam", "vase"]
funeral_flowers = ["casket spray", "standing spray", "open heart", "urn", "standing cross"]

# reusable functions next

#String Lists 1 

length = len(order_type)
funeral_flowers_set = set(funeral_flowers)
zipped = zip(arrangement_type, funeral_flowers)




# call functions and execute code
# use if __name__ == "__main__":
