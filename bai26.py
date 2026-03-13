import math

tu = int(input("Nhap tu so: "))
mau = int(input("Nhap mau so: "))

gcd = math.gcd(tu, mau)

tu //= gcd
mau //= gcd

if mau < 0:
    tu = -tu
    mau = -mau

if mau == 1:
    print("Rut gon:", tu)
else:
    print("Rut gon:", tu, "/", mau)
  
