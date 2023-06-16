# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1Lower = name1.lower()

name2Lower = name2.lower()

true1 = name1Lower.count("t") + name1Lower.count("r") + name1Lower.count("u") + name1Lower.count("e")

love1 = name1Lower.count("l") + name1Lower.count("o") + name1Lower.count("v") + name1Lower.count("e")

true2 = name2Lower.count("t") + name2Lower.count("r") + name2Lower.count("u") + name2Lower.count("e")

love2 = name2Lower.count("l") + name2Lower.count("o") + name2Lower.count("v") + name2Lower.count("e")

trueTotal = true1 + true2

loveTotal = love1 + love2

finalScore = int(str(trueTotal) + str(loveTotal))

if finalScore < 10 or finalScore > 90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.")
elif finalScore > 40 and finalScore < 50:
    print(f"Your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}.")
