# numbers = []
# for i in range()
# while True:
#     number = input("Enter the values of the numbers you want to calculate: ").lower()
#     number = int(number)
#     if number == "q":
#         break
import math


def addition(first_number, second_number):
    addition = first_number + second_number
    return addition


def substraction(first_number, second_number):
    return first_number - second_number


def product(first_number, second_number):
    product = first_number * second_number
    return product


def division(first_number, second_number):
    division = first_number / second_number
    return division


def square_root(first_number):
    root = math.sqrt(first_number)
    return root


print("Python calculator Program")
print("        MENU          ")
print("1)Addition")
print("2)Subtraction")
print("3)Multiplication")
print("4)Division")
print("5)SquareRoot")
print("6)Exit")

while True:
    print("Enter your operator you need to use: ")
    operator = input("Choose a Operator between 1-6: ")

    if operator == "5" or operator == "squareroot":
        first_number = int(input("Enter the number you want to use with the operator you have chosen: "))
        second_number = 0
    else:

        first_number = int(input("Enter the number you want to use with the operator you have chosen: "))
        second_number = int(input("Enter the number you want to use with the operator you have chosen: "))

    if operator == "6" or operator.lower() == "exit":
        print("You have quit the calculator ")
    elif operator == '1' or operator.lower() == "addition":
        print(f"The sum of the two numbers is : {addition(first_number, second_number)}")

    elif operator == '2' or operator.lower() == "subtraction":
        print(f"The sum of the two numbers is : {substraction(first_number, second_number)}")

    elif operator == '3' or operator.lower() == "multiplication":
        print(f"The sum of the two numbers is : {product(first_number, second_number)}")

    elif operator == '4' or operator.lower() == "division":
        print(f"The sum of the two numbers is : {division(first_number, second_number):.2f}")

    elif operator == '5' or operator.lower() == "squareroot":
        # first_number = int(input("Enter the number you want to find the square root of: "))
        print(f"The square root of your number is: {square_root(first_number)}")
