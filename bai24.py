n = int(input("Nhap n: "))

# a. Đếm chữ số
dem = len(str(n))
print(n, "co", dem, "chu so")

# b. Chữ số cuối
print("Chu so cuoi cung la:", n % 10)

# c. Chữ số đầu
print("Chu so dau tien la:", int(str(n)[0]))

# d. Tổng chữ số
tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tong cac chu so la:", tong)

# e. Số đảo ngược
dao = int(str(n)[::-1])
print("So dao nguoc la:", dao)
