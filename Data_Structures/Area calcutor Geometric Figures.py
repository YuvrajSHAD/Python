## Calculator For Geometric Figures includes 1.cube, 2.Traingle, 3.Rectangle, 4.Square, 5.Circle
def Geometric():
    area=0
    pie=3.14
    n=input("Enter Desired Figures in Smalle Letters:")
    if (n=="square"):
        side=int(input("Enter the Side value: "))
        area+=(side**2)
    elif n=="cube":
        side=int(input("Enter the Side value: "))
        area+=(6*(side**2))
    elif n== "Circle":
        radius = int(input("Enter the value of radius: "))
        area = area + (2 * pie * radius)
    elif n == "Rectangle":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of length: "))
        area = area + (length * width)
    elif n == "Triangle":
        base = int(input("Enter the value of base: "))
        height = int(input("Enter the value of height: "))
        area = area +(0.5 * base * height)
    else:
        print("Select a Valid Shape")
    print("Your area is %.2f"%area)
Geometric()