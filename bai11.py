import random

while True:
    user = input("Nhap b,d,k (khac de thoat): ")

    if user not in ['b','d','k']:
        break

    computer = random.choice(['b','d','k'])

    print("Computer:",computer)

    if user==computer:
        print("Hoa")
    elif (user=='b' and computer=='d') or \
         (user=='d' and computer=='k') or \
         (user=='k' and computer=='b'):
        print("User thang")
    else:
        print("Computer thang")
      
