import datetime

d,m,y = map(int,input("Nhap ngay thang nam: ").split())

try:
    day = datetime.date(y,m,d)
    print("Hop le")
    print(day.strftime("%A"))
except:
    print("Ngay khong hop le")
