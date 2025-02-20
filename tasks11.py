list = [17, 4, 7, 10, 11, 12]

num = int(input("Введите число: "))

diff=max(list)-num
target=max(list)

for i in list:
    
    if abs (i-num)<=diff:
        diff=abs(i-num)
        target=i
print("Ближайшее число:", target)