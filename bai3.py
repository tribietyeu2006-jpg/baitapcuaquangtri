import math

xC = float(input("Nhap Cx: "))
yC = float(input("Nhap Cy: "))
R = float(input("Nhap ban kinh R: "))

xM = float(input("Nhap Mx: "))
yM = float(input("Nhap My: "))

d = math.sqrt((xM - xC)**2 + (yM - yC)**2)

if d < R:
    print("M nam trong C")
elif d == R:
    print("M nam tren C")
else:
    print("M nam ngoai C")v
