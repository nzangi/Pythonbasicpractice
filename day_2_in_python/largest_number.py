"""
find the largest,middle and smallest in a list from user of three numbers
"""
numbers = [1,2,3]
# for i in range(3):
#     number = input(f"Enter your number {i + 1}: ")
#     number = int(number)
#     numbers.append(number)

# first_number = numbers[0]
# second_number = numbers[1]
# third_number = numbers[2]

# if first_number > second_number and first_number > third_number:
#     print("Fisrt number is the largest in the list ")
# if second_number > first_number and second_number > third_number:
#     print("Second number is the largest number in list ")
# if third_number > second_number and third_number > first_number:
#     print("Third Number is the largest number in the list ")
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number

print(f"The largest number is:  {largest_number}")
