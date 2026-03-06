n = int(input("Nhap n: "))

count = 0
total = 0

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
        count += 1
        total += i

print()
print("Co", count, "uoc so")
print("Tong la:", total)
