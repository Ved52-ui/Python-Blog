lst = ['Rahul','Nadola','Avani','Dharmesh', True, 1, 2, 2.23, "2.34", "4", False, True, 1]
print(lst)

#Access the elements through indexing
print(lst[0])
print(lst[-0])
print(lst[-1])
print('-'*20)

# Modify value
print(lst)
lst[2] = 'Varsha'
print(lst)
print('-'*20)

#Slicing
print(lst)
print(lst[2:5])
print('-'*20)

#Reverse a string
print(lst)
print(lst[::-1])
print('-'*20)

#Reverse a string by steps
print(lst)
print(lst[::-2])
print('-'*20)

#Appending
print(lst)
lst.append('Mona')
print(lst)
print('-'*20)

#Removing elements
print(lst)
lst.remove('Nadola')
print(lst)
print('-'*20)

#Length
print(lst)
print(len(lst))
print('-'*20)

#Sorting 
lst1 = [2,5,8,23,45,21,94,5,8,6]
print(lst1)
print(sorted(lst1))

#Find element 
print(lst)
print(lst.index('Rahul'))
print('-' * 20)

print(lst)
print(lst.index(True))
print('-' * 20)

#Count
print(lst)
print(lst.count(True))
print('-' * 20)

#Merge two lists
#Using the + Operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print(merged_list)
print('-' * 20)

#Using the extend() Method
print(lst)
lst.extend(['Manish', 3, 4.23, '54.23', 'Manish'])
print(lst)
'''
OR
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)
print('-' * 20)

#Using List Comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = [item for sublist in [list1, list2] for item in sublist]
print(merged_list)
print('-' * 20)

#Using the * Operator (Python 3.5+)
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = [*list1, *list2]
print(merged_list)
print('-' * 20)

#Using the chain() Function from itertools
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list(chain(list1, list2))
print(merged_list)
print('-' * 20)


#Finding Min and Max 
lst1 = [2,5,8,23,45,21,94,5,8,6]
print(lst1)
print(min(lst1))
print(max(lst1))
print('-' * 20)

#Iterating element of list | Direct way
lst1 = [2,5,8,23,45,21,94,5,8,6]
print(lst1)
for i in lst1:
    print(i)
print('-' * 20)


print(lst)
for i in lst:
    print(i)
print('-' * 20)

#Iterating element of list | Indexing
lst1 = [2,5,8,23,45,21,94,5,8,6]
print(lst1)
for i in range(len(lst1)):
    print(i, lst1[i])
print('-' * 20)


print(lst)
for i in range(len(lst)):
    print(i, lst[i])
print('-' * 20)

#Iterating element of list | Indexing | reverse
lst1 = [2,5,8,23,45,21,94,5,8,6]
print(lst1)
for i in range(len(lst1)-1, -1, -1):    #First -1 is starting from last element, Second -1 is ending from last element and Third -1 is steps to go back one by one steps
    print(i, lst1[i])
print('-' * 20)


print(lst)
for i in range(len(lst)-1, -1, -1):
    print(i, lst[i])
print('-' * 20)

#Multidimensional list
lst2 = [[1,2,3],[4,5,6],[7,8,9]]
lst3 = [2.3, '23.43', 'Rahul', [1,2,3],[4,5,6],[7,8,9], [['Varsha', 25], ['Dharmesh', 30]]]
print(lst3)
print('-' * 20)

#Accessing the Elements
print(lst2)
print(lst2[0])
print(lst2[0][0])
print(lst2[1][1])
print(lst2[2][2])
print(lst2[0:2])
print(lst2[0:3])
print('-' * 20)

#Modifying elements under the list of lists
print(lst2)
lst2[0][0] = 0
print(lst2)
print('-' * 20)

#Modifying elements under the list of lists
print(lst2)
lst2[1] = ['Rahul', 11]
print(lst2)
print('-' * 20)

#Appending the values
print(lst2)
lst2.append([12, 13, 14])
print(lst2)
print('-' * 20)

#Delete the index or sublist under nested list
print(lst2)
del lst2[0]
print(lst2)
print('-' * 20)

#Length of list
lst4 = [1,2,5,8,[11,14,3],'Rahul',True,10.3,6,8]
print(len(lst4))
print('-' * 20)

#Reverse
print(lst4)
print(lst4[::-1])
print('-' * 20)

#Accessing all the elements
print(lst4)
for i in lst4:
    print(i)
print('-' * 20)

#It will give error since in list4 they have integer value and it will not be iterable
#print(lst4)
#for i in lst4:
#    for j in i:
#        print(j)
#print('-' * 20)

list5 = [[1,2,3],[4,6],[7,8,9]]
print(list5)
for i in list5:
    print(i)
print('-' * 20)

list5 = [[1,2,3],[4,6],[7,8,9]]
print(list5)
for i in list5:
    for j in i:
        print(j)
print('-' * 20)