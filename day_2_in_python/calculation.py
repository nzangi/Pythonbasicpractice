import math

def sum(a,b): return a+b

def difference(a,b): return a-b

def product(a,b): return a*b

def quotient(a,b): return a/b

def sqrt(a): return(math.sqrt(a))

def selectMenu():
    print('Python Calculator Program')
    print('         MENU')
    print('1)Add')
    print('2)Subtract')
    print('3)Multiply')
    print('4)Divide')
    print('5)Square Root')
    print('6)Exit')
    print('Enter Your Choice:')
    return input('Choose a number 1 - 6: ')


def main():
ans = "" #declare ans because if we try to see if ans == "" and ans doesnt exist, the
         #program will crash
operator = "" # "" is not 6, therefore the while loop will run at least once
while operator != '6': #as long as the variable operator is not 6  // operator != '6'
                       #is your condition
    operator = selectMenu() #this will get the user's choice
    operation = "" #our placeholder for the operation string
    if operator == '1' or operator.lower() == 'add': #.lower() will convert the
                                                     #entire string to lowercase, so
                                                     #that you dont have to test for
                                                     #caps
        a=float(input('Enter the fist number that you wish to add: '))
        b=float(input('Enter the second number that you wish to add: '))
        operation = "sum"
        ans= sum(a,b)

    elif operator == '2' or operator.lower() == 'subtract':
        a=float(input('Enter the fist number that you wish to subtract: '))
        b=float(input('Enter the second number that you wish to subtract: '))
        operation = "difference"
        ans = difference(a, b)


    elif operator == '3' or operator.lower() == 'multiply':
        a=float(input('Enter the fist number that you wish to multiply: '))
        b=float(input('Enter the second number that you wish to multiply: '))
        operation = "product"
        ans=product(a,b)

    elif operator == '4' or operator.lower() == 'divide':
        a=float(input('Enter the dividend: '))
        b=float(input('Enter the divisor: '))
        operation = "quotient"
        ans=quotient(a,b)


    elif operator == '5' or operator.lower() == 'square root':
        a=float(input('Enter the number you wish to find the square root of: '))
        operation = "square root"
        ans=sqrt(a)

    elif operator =='6':
       print('CALCULATOR: ON [OFF]')
       operation = ""
       ans = ""
       #break // while break technically works, its a bad habit to get in to. your
       #loops should naturally terminate themselves by causing the condition to
       #become false

    else:
        print('Enter the math operator as displayed')

         if ans != "": # since we're always gonna print the answer no matter what
                       #they pick, its easier to do it after your if statements.
             print() #print empty lines for spacing
             print("The ", operation, " is: ", ans)
             print()

 main()

