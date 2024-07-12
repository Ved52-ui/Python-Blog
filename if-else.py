n = int(input('Enter the number : '))

if (n > 0):                     # If we can add ">=" and "<= then "0" takes by default as positive or negative
    print(n , 'is positive')

if (n < 0):
    print(n , 'is negative')

if (n == 0):                    # We can add here "else" at the last statement
    print('its a zero')
print('-'*35)



n = int(input('Enter the number : '))

if (n == 0):
    print('its a zero')
elif (n > 0):                       # Here we can add as many as number of "elif" condition       
    print(n , 'is positive')
else:
    print(n , 'is negative')
print('-'*35)


n = int(input('Enter the number : '))

if(n%5 == 0):
    print('its divisible by 5')
else:
    print('not divisible')
print('-'*35)


n = int(input('Enter the number : '))

if (n%5 == 0):
    if (n%3 == 0):
        print('its divisible by 5 and 3')
    else:
        print('its divisible by 5 but not 3')
else:
    print('its divisible by 3 but not 5')
print('-'*35)


n = int(input('Enter the number : '))

if (n%5 == 0) and (n%3 == 0):           # Here you can use "OR" and "Not" as well
     print('its divisible by 5 and 3')
else:
    print('not divisible')
print('-'*35)

