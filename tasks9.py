
my_list = [1, 44, 7, 9, 3, 2, 1, 44]


index1 = int(input("Введите первый индекс: "))
index2 = int(input("Введите второй индекс: "))


result = [my_list[i] for i in range(len(my_list)) if i != index1 and i != index2]


print("Результат:", result)