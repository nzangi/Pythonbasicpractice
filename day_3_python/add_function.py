
numbers = []
for i in range(2):
    number = input(f"Enter the number {i+1} you need to add in your list: ")
    number = int(number)
    numbers.append(number)


def sum(numbers):
    total= 0
    for number in numbers:
        total = total + number
    return total


total = (sum(numbers))
print(f"The sum of your numbers in the list is: {total}")

