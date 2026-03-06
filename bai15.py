day, month, year = map(int, input("Nhap ngay thang nam: ").split())

# kiểm tra năm nhuận
leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

sum_day = int(30.42 * (month - 1)) + day

if month == 2:
    sum_day += 1
elif month > 2 and leap:
    sum_day += 1

if 2 < month < 8:
    sum_day -= 1

print("Ngay thu:", sum_day)
