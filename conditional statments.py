# age =52
# if age>25:
#     print("age is eligible for voting")

#     1. Vowel Checker:
# Write a Python program that takes a character as input and checks whether
# it is a vowel or not. Use the 
# if-else statement.

# character= input("enter_character :")
# vowel = ['a','e','i','o','u','A','E','I','O','U']
# if character in vowel:
#     print("it is a vowel")
#     print(f"The character is a vowel {character}")
# else:
#     print(f"This character is not a vowel {character}")

# output;
# it is a vowel
# The character is a vowel a
#     enter_character :f
# This character is not a vowel f


# 2. Age Group Classification
# Write a program that takes an age as input and classifies the person into
# one of the following age groups:
# Child: 0-12 years
# Teenager: 13-17 years
# Adult: 18-64 years
# Senior: 65 years and older
# age =int(input("Enter your age in years:"))
# if age<=0:
#     print(f"Entered age {age} is invaild")
# if age<=13:
#     print(f"Entered age is {age} belongs child age group")
# if age<=17:
#     print(f"Entered age is {age} belongs Teenager age group")
# if age<=64:
#         print(f"Entered age is {age} belongs adult age group")
# if age >=65:
#      print(f"Entered age is {age} belongs senior citizen age group")

#      output:
#      Enter your age in years:68
# Entered age is 68 belongs senior citizen age group
# Enter your age in years:19
# Entered age is 19 belongs adult age group

# 3. Number Classifier:
# Write a program that takes an integer as input and classifies it as positive,
# negative, or zero. Use the 
# if-elif-else statement.

# number=int(input("Enter the number:"))
# if number > 0:
#     print(f"The enter number {number} is belongs to positive classification")
# elif number<0:
#     print(f"The enter number {number} is belongs to negetive classification") 
# else:
#     print(f"The enter number {number} is equals to zero") 

# output:
# Enter the number:5
# The enter number 5 is belongs to positive classification
# Enter the number:0
# The enter number 0 is equals to zero
# Enter the number:-1
# The enter number -1 is belongs to negetive classification



# 4. Leap Year Checker:
# Create a program that checks whether a given year is a leap year or not. A
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.

# year=int(input("Enter the year :"))
# if (year % 4 == 0 and year % 100 != 0)or(year % 400 == 0):
#     print(f"Entered year is {year} belongs to Leap year")
# else:
#     print(f"Entered year is {year} not a Leap year")

# output:
# Enter the year :2000
# Entered year is 2000 belongs to Leap year
# Enter the year :2024
# Entered year is 2024 belongs to Leap year

# 5. Calculator:
# Build a simple calculator program that takes two numbers and an operator
# (+, -, *, /) as input and performs the corresponding operation.
# opt_1= int(input("Enter number_1:"))
# opt_2=int(input("Enter numb_2:"))
# operator = (input("enter any operator:"))
# if operator == "+":
#     print(f"sum of two numbers is {opt_1+opt_2}")
# if operator == "*":
#          print(f"multiplication of two numbers is {opt_1*opt_2}")
# if operator == "/":
#         print(f"divison of two numbers is {opt_1/opt_2}")
# if operator == "-":
#        print(f"divison of two numbers is {opt_1-opt_2}")

# output:
# Enter number_1:20
# Enter numb_2:10
# enter any operator:-
# divison of two numbers is 10

# Enter number_1:20
# Enter numb_2:50
# enter any operator:*
# multiplication of two numbers is 1000

# Enter number_1:20
# Enter numb_2:50
# enter any operator:+
# sum of two numbers is 70

# 6. Short Hand If:
# Rewrite the following code using the short-hand 
# if statement:
# Quiz Questions: 3
# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd"

# x=8
# result = "x is even" if x % 2 == 0 else "x is odd "
# print(result)

# output:
# x is even


# 7. Discount Calculator:
# Create a program that calculates the final price after applying a discount.
# The program should take the original price and the discount percentage as
# input.

# list_price = int(input("Enter orginal price :"))
# discount=int(input("Enter discount percentage % :"))
# result=list_price*discount/100
# final_price= list_price - result
# print(f"The orginal price of product is {list_price} RS/- and Discount is {discount} %,final price of the product after discount {final_price}")

# output:
# Enter orginal price :1000
# Enter discount percentage % :20
# The orginal price of product is 1000 RS/- and Discount is 20 %,final price of the product after discount 800.0

# 8. BMI Calculator:
# Write a program that calculates the Body Mass Index (BMI) using the
# formula: BMI = weight (kg) / (height (m))^2. The program should take
# weight and height as input.

# weight=int(input("Enter your weight in kg:"))
# height= int(input("Enter your height in meters"))
# result=weight/height
# print(f"your height is {height} in meters and your weight is {weight} in kgs,then your BMI result is {result}")

# output:
# Enter your weight in kg:95
# Enter your height in meters146
# your height is 146 in meters and your weight is 95 in kgs,then your BMI result is 0.6506849315068494
                
       



    
