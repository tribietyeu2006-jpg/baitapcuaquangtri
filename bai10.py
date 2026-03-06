sin = input("Nhap SIN: ")

if len(sin)!=9 or not sin.isdigit():
    print("SIN khong hop le")
else:
    digits = list(map(int,sin))

    s1 = digits[0]+digits[2]+digits[4]+digits[6]
    
    s2 = 0
    for i in [1,3,5,7]:
        x = digits[i]*2
        if x>9:
            x = x//10 + x%10
        s2 += x

    total = s1+s2+digits[8]

    if total%10==0:
        print("SIN hop le")
    else:
        print("SIN khong hop le")
