#Homework day 2 Tuesday January 14th 2020

#Small

#1 Hello You!

# name = input("What is your name?")
# namelen = len(name)
# if namelen > 0 :
#     print("Hello, " + name)


#2 HELLO YOU!

# name = input("What is your name?")
# namelen = len(name)
# if namelen > 0 :
#     print("HELLO " + name.upper())
#     print("YOUR NAME HAS " + str(namelen) + " LETTERS IN IT! AWESOME!")


#3 Madlib

# madlib = "Please fill the blanks below: \n____(name)____'s favorite subject in school is ____(subject)____."
# print(madlib)

# name = input("What is name?")
# subject = input("What is Subject?")
# namelen = len(name)
# sublen = len(subject)

# if namelen > 0 and sublen > 0 :
#     madlibanswered = f"{name}'s favorite subject is {subject}."
#     print(madlibanswered)


#4 Day of the Week

# day = int(input('Day (0-6)? '))

# if day == 0 :
#     print("Sunday")

# elif day == 1 :
#     print("Monday")

# elif day == 2 :
#     print("Tuesday")

# elif day == 3 :
#     print("Wednesday")

# elif day == 4 :
#     print("Thursday")

# elif day == 5 :
#     print("Friday")

# elif day == 6 :
#     print("Saturday")

# else:
#     print("Invalid number!")


#5 Work or Sleep In?

# day = int(input('Day (0-6)? '))

# if day == 0 :
#     print("Sleep in!")

# elif day > 0 and day < 6 :
#     print("Go to work.")

# elif day == 6 :
#     print("Sleep in!")

# else:
#     print("Invalid number!")


#6 Celsius to Fahrenheit

# Celsius = (input("Whats the temperature in Celsius? "))
# print(str(int(Celsius) * (9/5) + 32) + "F")


#7 Looping from 1 to 10

# count = 0
# while count < 10:
#     count += 1
#     print(count)


#8 n to m

# count = 1
# while count < 8:
#     count += 1
#     print(count)


#9 Print a Square

# print("*****\n*****\n*****\n*****\n*****")


#10 Print a Square II

# size = int(input("How big is the square? "))

# for i in range((size)) :
#     print("*" * size)


# Medium

#1 Tip Calculator

# bill_amount = (input("Total bill amount? "))
# service = input("Level of service? i.e. good, fair, bad: ")
# bill_amount = float(bill_amount)

# if service == "good" :
#     print("Tip amount: " + str(bill_amount * 0.20))
#     print("Total amount: " + str((bill_amount * 0.20) + bill_amount))

# elif service == "fair" :
#     print("Tip amount: " + str(bill_amount * 0.15))
#     print("Total amount: " + str((bill_amount * 0.15) + bill_amount))

# elif service == "bad" :
#     print("Tip amount: " + str(bill_amount * 0.10))
#     print("Total amount: " + str((bill_amount * 0.10) + bill_amount))

# else:
#     print("INVALID!!!")


#2 Tip Calculator 2

# bill_amount = (input("Total bill amount? "))
# service = input("Level of service? i.e. good, fair, bad: ")
# bill_amount = float(bill_amount)
# split = (input("Slpit how many ways? "))
# split = float(split)

# if service == "good" :
#     print("Tip amount: " + str(bill_amount * 0.20))
#     print("Total amount: " + str((bill_amount * 0.20) + bill_amount))
#     print("Amount per person: " + str(((bill_amount * 0.20) + bill_amount) / split))

# elif service == "fair" :
#     print("Tip amount: " + str(bill_amount * 0.15))
#     print("Total amount: " + str((bill_amount * 0.15) + bill_amount))
#     print("Amount per person: " + str(((bill_amount * 0.20) + bill_amount) / split))

# elif service == "bad" :
#     print("Tip amount: " + str(bill_amount * 0.10))
#     print("Total amount: " + str((bill_amount * 0.10) + bill_amount))
#     print("Amount per person: " + str(((bill_amount * 0.20) + bill_amount) / split))

# else:
#     print("INVALID!!!")


#3 How many coins?

# coins = 0
# while True :
#     print(f"You have {coins} coin(s).")
#     response = input("Do you want another? ")
    
#     if response == "yes":
#         coins += 1
    
#     if response == "no":
#         print("Bye")
#         break


#4 Print a Box

# width = int(input("What is the width? "))
# height = int(input("What is the height? "))

# print("*" * width)

# for i in range((height - 2)):

#     print("*" + " " * (width - 2) + "*")
# print("*" * width)


#5 Print a Triangle

# n = 4
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))


#6 Multiplication Table

for i in range(1, 11):
    for n in range(1, 11):
        result = i * n
        print(str(i) + " " + "X" + " " + str(n) + "=" + str(result))















