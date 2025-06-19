import math
# to access math functions and constants like math.pi

# --- Functions ---
def areaRectangle(length, width):
  area = length * width
  return area

def areaTriangle(base, height):
  area = base * height * 0.5
  return area

def areaCircle(radius):
   area = math.pi * radius * radius
   return area    

# --- Main Program ---
 
print("Welcome to the Shape Area Calculator!")
print("Enter 'R' for Rectangle, 'T' for Triangle, or 'C' for Circle.")

shape = input("Your choice: ").strip().lower()

# these are called conditionals, there will be more information about them next week
# they are meant to check if a condition is true, if so, it runs
# for now, just use this template we gave you :)
if shape == "r":
    # TODO: Ask for length and width as floats
    # length = float(input("Enter the length: "))
    length = float(input("Please enter the length of your rectangle: "))
    # width = float(input("Enter the width: "))
    width = float(input("Please enter the width of your rectangle: "))
    # TODO: Calculate area using areaRectangle()
    area = areaRectangle (length, width)
    # TODO: Print the result nicely formatted
    print ("The area of this rectangle is " + str(area) + ".")
    pass

elif shape == "t":
    # TODO: Ask for base and height as floats
    # base = float(input("Enter the base: "))
    base = float(input("Please enter the base of your triangle: "))
    # height = float(input("Enter the height: "))
    height = float(input("Please enter the width of your rectangle: "))
    # TODO: Calculate area using areaTriangle()
    area = areaTriangle (base, height)
    # TODO: Print the result nicely formatted
    print ("The area of this triangle is " + str(area) + ".")    
    pass

elif shape == "c":
    # TODO: Ask for radius as a float
    # radius = float(input("Enter the radius: "))
    radius = float(input("Please enter the radius of your circle: "))
    # TODO: Calculate area using areaCircle()
    area = areaCircle (radius)
    # TODO: Print the result nicely formatted
    print ("The area of this circle is " + str(area) + ".")
    pass

else:
    print("Invalid shape choice. Please run the program again and choose R, T, or C.")
