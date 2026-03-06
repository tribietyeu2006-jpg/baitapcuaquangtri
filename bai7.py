a,b = map(float,input("Nhap a b: ").split())

if a==0:
    if b==0:
        print("Vo so nghiem")
    else:
        print("Vo nghiem")
else:
    x = -b/a
    print("x =",x)
