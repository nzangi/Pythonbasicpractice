age = input("Enter your Current :  ")
age = int(age)

days_lived = age * 365
week_lived = age * 52
hours_lived = days_lived * 24
minutes_lived = hours_lived * 24
second_lived = minutes_lived * 60
milliseconds_lived = second_lived * 1000
nanoseconds_lived = milliseconds_lived * pow(10, 9)
print(f"You are old", age, week_lived, days_lived, minutes_lived,
      second_lived, milliseconds_lived, nanoseconds_lived)
