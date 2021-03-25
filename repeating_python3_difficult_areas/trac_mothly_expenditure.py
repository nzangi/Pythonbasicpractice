house_hold = []
name = input("Your name: ")
months_in_year = [1,2,3,4,5,6,7,8,9,10,11,12]
savings = []

for month in months_in_year:
    monthly_expenditure = int(input(f"Enter your monthly expenditure in this year 1 in month {month}: "))
    savings_account = int(1/3 * monthly_expenditure)
    savings.append(sum(savings_account))
    print(savings)



