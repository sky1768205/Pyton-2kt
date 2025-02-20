
strings = ["apple", "banana", "cherry", "date"]


max_length = 0
for s in strings:
    if len(s) > max_length:
        max_length = len(s)


normalized_strings = []
for s in strings:
  
    new_string = s + "_" * (max_length - len(s))
    normalized_strings.append(new_string)


print("Нормализованный список строк:", normalized_strings)