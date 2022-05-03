# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_names =len(names)
random_name = random.randint(0,total_names-1)
print(random_name)
final_name = names[random_name]
print(final_name + " Will pay the bill")








