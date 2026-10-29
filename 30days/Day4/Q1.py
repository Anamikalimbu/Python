#Classify a triangle (equilateral, isosceles, scalene) from three sides, and check validity first.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if the sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Classify the triangle
    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The sides do not form a valid triangle.")