# """
#                 FUNCTIONS
#                     EXAMPLE 1
# 1. use functions together with loops,lists,dictionaries to write a program to do something.
# question to MUMO: why can't i see the numbers being appended in my list using function
# """
# numbers = []
# for i in range(5):
#     number = int(input(f"Input the {i + 1} number you need to be in your list: "))
#     numbers.append(number)
#
#
# def mathematics(numbers):
#     addition = 0
#     product = 1
#     for number in numbers:
#         addition = addition + number
#         product = product * number
#     return addition, product
#
#
# addition, product = mathematics(numbers)
# print(f"The sum of the numbers you have entered is {addition}")
# print(f"The sum of the numbers you have entered is {product}")
#
"""
           EXAMPLE 2 Question
Exercise 1: Create a function that can accept two arguments name and age and print its value
"""

#
# def age_function():
#     your_age = int(input('Input your own age: '))
#     your_name = input('Input your own name: ')
#     return your_name, your_age
#
#
# your_name,your_age,  = age_function()
# print(f"Your name is {your_name} and you are {your_age} years old ")

"""
Exercise 2: Write a function func1() such that it can accept a variable length of  argument and
 print all arguments value
"""

#
# def function_example(*args):
#     for i in args:
#         print(i)
#
#
#
# function_example(10,20,3,4)

"""
Exercise 3: Write a function calculation() such that it can accept two variables and calculate
 the addition and subtraction of them. And also it must return both addition and subtraction in a 
 single return call
"""
# numbers = []
# for i in range(5):
#     number = int(input(f"Input the {i + 1} you need to calculate the sum and product:  "))
#     numbers.append(number)
#
#
# def operator(numbers):
#     addition = 0
#     product = 1
#     for number in numbers:
#         addition = addition + number
#         product = product * number
#     return addition, product
#
#
# addition, product = operator(numbers)
# print(f"The sum of the list {addition} and product is {product}.")
#
"""
Exercise 4: Create a function showEmployee() in such a way that it should accept employee name, 
and its salary and display both. If the salary is missing in the function call assign default 
value 9000 to salary
"""

# names = []
# salaries = []
#
#
# def show_employees():
#     global name, salary
#     for i in range(5):
#         name = input(f"{i + 1}. Please enter you name: ")
#         names.append(name)
#         salary = int(input(f"{i + 1}. Enter you salary on every month: "))
#         salaries.append(salary)
#     return names, salaries
#
#
# name, salary = show_employees()
# for k in range(5):
#     print(f"Your name is {name[k]} and your salary is {salary[k]}\n")
# """"
# Exercise 5: Create an inner function to calculate the addition in the following way
# """
# # def sum_numbers():
# #     addition = a+b
# #     def sum_them():
# #         sum(a,b)
# #

"""
Exercise 6: Write a recursive function to calculate the sum of numbers from 0 to 10
"""

# def recursive_function():
#     numbers = []
#     addition = 0
#     for i in range(1, 11):
#         number = int(input(f"Enter the number {i} to add in the list: "))
#         numbers.append(number)
#         addition = addition + number
#     return addition
#
#
# addition = recursive_function()
# print(f"The sum of the numbers in the list is: {addition}")

"""
Exercise 7: Assign a different name to function and call it through the new name
"""

"""
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
"""


def even_numbers():
    even_numbers = []
    for i in range(4,31):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


even_numbers = even_numbers()
print(f"The numbers are: {even_numbers}")

"""
Exercise 9: Return the largest item from the given list
"""
