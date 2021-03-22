print("if you press a 'q' you will quit the program")
while True:
    user_input = input("Enter a number or a character of your wish: ")
    if user_input == 'q':
        print("Good Bye, you are quiting the program")
        break
    elif user_input.isdigit():
        print(f"you have entered a Number {user_input}")
    else:
        user_input_length = len(user_input)
        if user_input_length > 1:
            print(f"Your input is a string '{user_input}' with {user_input_length} characters ")
        else:
            print(f"Your input is a string '{user_input}' with {user_input_length} character ")
