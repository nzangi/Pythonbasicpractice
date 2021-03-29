# a function which calculates number of cheese and box crackers
def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheese")
    print(f"You have {box_of_crackers} in your box ")
    print("That is enough for a Man's Party")
    print("Get a blanket to sleep \n")


# assigning our function directly
print("I can just give the function number directly.")
cheese_and_crackers(20, 10)

# assigning our function with variables of your own
print("OR we just the variables from our script")
amount_of_cheese = int(input("Enter the amount of cheese that you need for your party: "))
amount_of_crackers = int(input("Enter the number of crackers that you need for your party: "))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# assigning values to your function by calculation
print("We ca also do some calculation to our function")
cheese_and_crackers(10 + 30, 6 * 5)

# assigning our values of the function by combining variable and our math
print("And we combine the Two, variable and the math")
cheese_and_crackers(amount_of_cheese + 1000, amount_of_crackers * 30)
