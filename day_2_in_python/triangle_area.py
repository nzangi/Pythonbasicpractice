"""
we are calculating an area of a triangle of unequal dimensions
we calculate the are of the triangle b this formula
 area = (s*(s-a) * (s-b) * (s-c)) ** 0.5


"""

sides = []
for i in range(3):
    side = input(f"Enter the length of side {i+1} of the triangle: ")
    side = int(side)
    sides.append(side)

A = sides[0]
B = sides[1]
C = sides[2]

# calculating the perimeter of the triangle
perimeter = A + B + C

S = float(perimeter / 2)

# calculating the area of the triangle
area = float((S * (S - A) * (S - B) * (S - C)) ** 0.5)

print(f"The perimeter of your Triangle is:  {perimeter} cm ")
print(f"The Area of your Triangle is: {area:.3f} cm^2")
