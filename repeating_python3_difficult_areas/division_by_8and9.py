numbers_divisible_by_8 = []
numbers_divisible_by_9 = []
for i in range(15, 56):
    if i % 8 == 0:
        numbers_divisible_by_8.append(i)
    if i % 9 == 0:
     numbers_divisible_by_9.append(i)
joined_list = numbers_divisible_by_8 + numbers_divisible_by_9
joined_list.sort(reverse=True)
print(joined_list)
