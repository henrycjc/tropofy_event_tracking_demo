import random

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

if __name__ == "__main__":
    for _ in range(0, 1000):
        f = foods[random.randint(0, len(foods) - 1)]
        quantity = str(random.randint(0, 5))
        age = str(random.randint(12, 70))
        postcode = str(random.randint(1000, 5000)) # Yeah, I know
        s = ("Order(\"" + f + "\", datetime.datetime(2017, 1, 2, random.randint(6, 18)), " + quantity + ", " + age + ", " + postcode + "),")
        print(s)
