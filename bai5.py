def area(x1,y1,x2,y2,x3,y3):
    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2

xa,ya = map(float,input("A: ").split())
xb,yb = map(float,input("B: ").split())
xc,yc = map(float,input("C: ").split())
xm,ym = map(float,input("M: ").split())

S = area(xa,ya,xb,yb,xc,yc)

S1 = area(xm,ym,xb,yb,xc,yc)
S2 = area(xa,ya,xm,ym,xc,yc)
S3 = area(xa,ya,xb,yb,xm,ym)

if abs(S-(S1+S2+S3)) < 1e-6:
    if S1==0 or S2==0 or S3==0:
        print("M nam tren canh tam giac")
    else:
        print("M nam trong tam giac")
else:
    print("M nam ngoai tam giac")
