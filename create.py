foods = ["Banh Mi",
"Rice Noodle Salad",
"Prawn Soup",
"Vietnamese Spring Rolls",
"Honey Chicken", 
"Lemon Chicken",
"Wonton Soup",
"Chinese Spring Rolls", 
"Sweet and Sour Pork", 
"Spanish Meatballs",
"Seafood Paella"]

import random, datetime
from random import randrange
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

for _ in range(0, 1000):
    f = foods[random.randint(0, len(foods)-1)]
    s = ("Order(\""+f+"\", datetime.datetime(2017, 1, 2, random.randint(6, 18)), " 
        + str(random.randint(0, 5)) + ", " + str(random.randint(12, 70)) + ", " + str(random.randint(1000, 5000))  + "),")
    print s






s = ("Order(\""+ foods[random.randint(0, len(foods)-1)] + 
        "\", \"" + random_date(datetime.datetime(2017, 1, 2, 6), datetime.datetime(2017, 1, 2, 18)).isoformat() + "\", " 
        + str(random.randint(0, 5)) + ", " + str(random.randint(12, 70)) + ", " + str(random.randint(1000, 5000))  + "),")
