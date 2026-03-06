standard = float(input("Nhap diem chuan: "))

d1, d2, d3 = map(float, input("Nhap 3 mon: ").split())

region = input("Nhap khu vuc (A,B,C,X): ")
obj = int(input("Nhap doi tuong (1,2,3,0): "))

region_bonus = {"A":2,"B":1,"C":0.5,"X":0}
obj_bonus = {1:2.5,2:1.5,3:1,0:0}

total = d1 + d2 + d3 + region_bonus[region] + obj_bonus[obj]

if d1==0 or d2==0 or d3==0:
    print("Rot")
elif total >= standard:
    print("Dau")
else:
    print("Rot")

print("Tong diem:", total)
