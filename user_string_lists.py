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

#String lists 2 
def random_sentence(): 
    logger.info(f"Calling random_sentence()")
    sentence = (f"The arrangement type is {random.choice(arrangement_type)}" f"The type of flowers used will be {random.choice(type_of_flowers)} ")

    logger.info(f"Random sentence: {sentence}")
#String lists 3 
def process_text_names_in(): 
    logger.info("Calling process_text_names_in()")

    with open("text_names_in.txt", "r") as fileObject: 
        text = fileObject.read()
        list_words = text.split()
        unique_words = set(list_words)
        sortedlist = sorted(unique_words)
        list_length = len(unique_words)

        logger.info(f"This text has {list_length} names")
        
        

    






# call functions and execute code
# use if __name__ == "__main__":
    logger.info("CALLING create_random_sentence")
