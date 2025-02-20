
number = input("Введите число: ")


count = 0
for digit in reversed(number): 
    if digit == '0':
        count += 1
    else:
        break 

print("Количество нулей в конце числа:", count)