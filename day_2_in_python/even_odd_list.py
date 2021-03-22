numbers = [60,38,33,45,24,89,39,99,47,90]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f"Even numbers are {even_numbers}")
print(f"Odd numbers are {odd_numbers}")
