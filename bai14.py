import datetime

d,m,y = map(int,input("Nhap ngay thang nam: ").split())

day = datetime.date(y,m,d)
yesterday = day - datetime.timedelta(days=1)

print("Hom qua:",yesterday.strftime("%d/%m/%Y"))
