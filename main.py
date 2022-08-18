# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

name_length = len(names)

random_choice = random.randint(0, name_length - 1)

person_who_pays = names[random_choice]

print(person_who_pays + " is going to buy the meal today!")
