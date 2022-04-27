# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
print(combined_string)
lowercase_string = combined_string.lower()
print(lowercase_string)
t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e


l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")


love = l + o + v + e

True_love = str(true) + str(love)
print(True_love)
TL = int(True_love)
if TL < 10 or TL > 90 :
    print(f"Your score is {TL}, you go together like coke and mentos.")
elif TL > 40 and TL < 50 :
    print(f"Your score is {TL}, you are alright together.")

else :
    print(f"Your score is {TL}.")