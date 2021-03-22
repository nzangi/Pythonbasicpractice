numbers = []
for i in range(5):
    number = input(f"Enter the number {i + 1} of values you need to be your list : ")  # is digit
    number = int(number)
    numbers.append(number)

# numbers = [1,2,3,4,5]

even_number = [] if numbers else None
odd_number = [] if numbers else None
addition = 0
average = 0
product = 1
largest_number = numbers[0] if numbers else None
smallest_number = numbers[0] if numbers else None

for number in numbers:
    addition = addition + number
    average = addition / len(numbers)
    product = product * number
    if number > largest_number:
        largest_number = number
    if number < smallest_number:
        smallest_number = number
    if number % 2 == 0:
        even_number.append(number)
    else:
        odd_number.append(number)

print(f"The addition of the list is: {addition}")
print(f"The average of the list is: {average:.3f}")
print(f"The product of the list is: {product}")
print(f"Largest number in the list is: {largest_number}")
print(f"Smallest number in the list is: {smallest_number}")
print(f"This is a list of all even numbers in your list: {even_number}")
print(f"This is a list of all odd number numbers in your list: {odd_number}")
