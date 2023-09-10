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

#Sets
stem_pricing = {2, 3, 4, 7, 9, 10}
arrangement_pricing = {12, 30, 40, 50, 60}

logger.info(f"The retail stem prices are {stem_pricing}")
logger.info(f"The arrangement prices are {arrangement_pricing}")

