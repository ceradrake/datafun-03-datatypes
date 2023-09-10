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

#Intersection and union of sets

price_intersection = stem_pricing & arrangement_pricing
price_union = stem_pricing | arrangement_pricing

logger.info(f"The intersection of the 2 sets is {price_intersection}")
logger.info(f"The union of the prices is {price_union}")

#Creating Dictionaries 
daisy_dict = {"retail" : "$1.99", "Difficulty level" : "Easy", "Pack size": 13}
rose_dict = {"retail" : "$1.99", "Difficulty level" : "Moderate", "Pack size" : 8}

logger.info(f"Daisy dictionary is {daisy_dict}")
logger.info(f"Rose dictionary is {rose_dict}")

with open("text_names_in.txt") as file_object: 
    word_list = file_object.read().split()
    word_counts_dictionary = {}
    for word in word_list: 
        if word in word_counts_dictionary: 
            word_counts_dictionary[word] += 1 
        else: 
            word_counts_dictionary[word] = 1
logger.info(f"Given text_names_in, the word counts dictionary is {word_counts_dictionary}")

word_counts_dictionary2 = {word: word_list.count(word) for word in word_list}
logger.info(f"The word count dictionary 2 is {word_counts_dictionary2}")
