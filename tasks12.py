string = input("Введите строку: ")
start_char = input("Введите начальный символ-ограничитель: ")
end_char = input("Введите конечный символ-ограничитель: ")


start_index = string.index(start_char)  
end_index = string.index(end_char)

print(string[start_index +1:end_index])