import math

a,b,c = map(float,input("Nhap a b c: ").split())

if a==0:
    if b==0:
        print("Vo nghiem")
    else:
        print("x =",-c/b)
else:
    delta = b*b-4*a*c

    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        x = -b/(2*a)
        print("x =",x)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("x1 =",x1)
        print("x2 =",x2)
