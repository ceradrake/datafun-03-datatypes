"""
Cera Drake 
Tuples
9/10/23

"""
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#Create my tuples 
wholesale_locations = ("Florida", "Ecuador", "Canada", "California", "Bolivia")
biggest_months = ("February", "May", "June", "September")

logger.info(f"Wholesale locations = {wholesale_locations}")
logger.info(f"Busies months in the floral industry are: {biggest_months}")
