list1=[1,2,3,4,5]
list2=['apple','banana','carrot','dates','eggplant','fig']


list1.extend(list2)
print(list1)

list2.append("Elderberry")
print(list2)

list1.remove(5)
print(list1)

print(list2.index('eggplant'))
