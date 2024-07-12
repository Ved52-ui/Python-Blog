#General way
#Iterating over a list containing the list lst, instead of iterating directly over the elements of lst.
lst = [1,2,3,4,5,6]
l =[]
for i in lst:
    l.append(i**2)
print(l)
print('-'*30)

#If you want to print the list at each step of the iteration, you should place the print(l) statement inside the loop:
lst = [1,2,3,4,5,6]
l =[]
for i in lst:
    l.append(i**2)
    print(l)
print('-'*30)

#Using list comprehension
lst1 = [1,2,3,4,5,6]
print(lst1)
print('-'*30)
lst2 = [i for i in lst1]
print(lst2)
print('-'*30)
lst2 = [i**2 for i in lst1]
print(lst2)
print('-'*30)

#Finding even numbers without creating list with using range
lst3 = [i for i in range(20) if i%2 == 0]   #here first forloop works and then if condition check that after dividing i is remider zero or not and then it append in i(List)
print(lst3)
print('-'*30)

#want to find the math table
n=20    #n = int(input('Enter valid nuber: '))
lst4 = [i for i in range(n, n*10+1) if i%n == 0]   #here first forloop works and then if condition check that after dividing i with n is remider zero or not and then it append in i(List)
print(lst4)
print('-'*30)

#Finding even numbers without creating list with using range
lst5 = [i**2 for i in range(21) if i%2 == 0]   #here first forloop works and then if condition check that after dividing i is remider zero or not and then it append in i(List)
print(lst5)
print('-'*30)

#Multi-dimensional lists
print([[j for j in range(5)] for i in range(3)])    # here first for loop will run as a they create column and then second for loop run and as they create rows
print('-'*30)

print([[j**2 for j in range(5)] for i in range(3)])    # here first for loop will run as a they create column and then second for loop run and as they create rows
print('-'*30)

print([['-' for j in range(5)] for i in range(3)])    # here first for loop will decide what will go in loop and then second for loop define how many rows
print('-'*30)

#AAccessing all the elements of the multi-dimensions lists
print([[i for i in range(1,4)] for i in range(3)])
lst = [[j for j in range(1,4)] for i in range(3)]
print(lst)
print('-'*30)

#Accesign elements
print([j for i in lst for j in i])  #here range will not work insted of lst, first loop will assess the rows and second will assess column
print('-'*30)

#OR

print([num for row in lst for num in row]) #num = column
print('-'*30)


