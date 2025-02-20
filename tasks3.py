list1=list()
list2=[1,2,3,4,5]
list3=[1,2,3,6,7]
for a in list2:
    if a in list3:
        list1.append(a)
print(list1)