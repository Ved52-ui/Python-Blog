![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
print('''hello wolrd's''')
a='ved'
print(a, type(a))

x=100
y=10ved
print(type(y))

print(False**False)

x=100
y=6.57
v=(x+y)
print(v)

c=['ved',10,90,'hello']

w=set(c)
print(w)

print(bool(1))

print(type(int(float('2.178'))))

a='hello'
b='wolrd'
print(a+' '+b)

dir(a)

['__add__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']


 i=int(input('enter the number:'))
if(i==0):
    print('zero')
elif(i>0):
    print('positive')
else:
    print('nwgative')

if 1<5:
    print(True)
else:
    print(False)

    name='ved' #use in input function also
    age=17
    print("{name} age {age}" .format(name=name,age=age))
#to check year wether it is lip year or not
year=int(input('enter the year:'))
if(year %4 == 0 and year %100!= 0) or (year % 400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")
