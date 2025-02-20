list1 = [1, 2, 3]
list2 = [11, 22, 33]


result = []


for i in range(len(list1)):
    result.append(list1[i])  
    result.append(list2[i]) 


print("Результат:", result)