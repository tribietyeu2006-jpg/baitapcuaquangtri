import math

xA = float(input("A(xA): "))
yA = float(input("A(yA): "))

xB = float(input("B(xB): "))
yB = float(input("B(yB): "))

AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("|AB| =", AB)
