# When we rolling three dice will get probability at each time

for n in range(1,19):   #for three dice then max 19 and for two dice then 13 because 19 and 13 will excluded 
    number = 0
    for i in range(1,7):    #In one dice max 6 number so 7 will exclude
        for j in range(1,7):
            for k in range(1,7):
                if (i + j + k == n):
                    number = number + 1
    print(n, '=', round(number/216*100,2))  #If three dice then total iteration is 216 and when 2 dice then it will be 36 as a total probalility
