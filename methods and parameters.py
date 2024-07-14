class person1:
    example="abcd"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_details(self):
        print(f"name: {self.name}, age: {self.age} ")

    def celebrate_birthday(self):
        self.age+=1
        print(f"happy birthday {self.name}! you are now {self.age} years old")

p1=person1("ved",17)


class calculator:
    def add(self,a,b):
        return a+b
    
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        return a/b

calc=calculator()
print(calc.add(10,20))
print(calc.mul(10,20))
print(calc.div(60,20))

#default parameters
class greeter:
    def greet(self,name="guest"):
        print(f"hello, {name}")

Greeter=greeter()

Greeter.greet("ved")
Greeter.greet()

#variable lengthh arguments

class massenger:
    def send_massage(self,*masseges):
        for massage in masseges:
            print(f"sending message: {massage}")

    def send_custom_massage(self,**massage_details):
        for key,value in massage_details.items():
            print(f"{key}, {value}")

Massenger=massenger()

Massenger.send_massage("hello","ved","how are you")


Massenger.send_custom_massage(subject="meeting",body="let's meet at 11AM",recipient="ved")