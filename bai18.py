hours = int(input("Nhap so gio: "))

weeks = hours // (7*24)
hours = hours % (7*24)

days = hours // 24
hours = hours % 24

print(weeks, "tuan,", days, "ngay,", hours, "gio")
