year = int(input("Nhap nam: "))
first_day = int(input("Nhap thu cua ngay dau tien (0=CN): "))
month = int(input("Nhap thang: "))

people = ["A","B","C","D","E"]

days = [31,28,31,30,31,30,31,31,30,31,30,31]

# năm nhuận
if (year%4==0 and year%100!=0) or year%400==0:
    days[1] = 29

start = first_day

print("Sun Mon Tue Wed Thu Fri Sat")

person_index = 0

for i in range(start):
    print("   ", end="")

for day in range(1, days[month-1]+1):

    print(f"{day:2}[{people[person_index]}]", end=" ")

    person_index = (person_index + 1) % 5
    start += 1

    if start % 7 == 0:
        print()

print()
