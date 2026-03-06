import math

x = int(input("Nhap so phut: "))

degree = x/60
radian = degree*math.pi/180

print("cos(x) =",math.cos(radian))

goc = int(degree//90)+1
print("x thuoc goc vuong thu",goc)
