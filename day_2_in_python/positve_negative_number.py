"""
the following programs is to check whether a digits negative,positrive or zero
"""
digits = [-45,23,45,0,-7]

for digit in digits:
    if digit < 0:
        print(f"The number is negative : {digit} ")
    elif digit > 0:
        print(f"The number is positive : {digit} ")
    else:
        print(f"The number is Zero : {digit}")

