<!DOCTYPE html>
<html lang="en">
<head>
    <h1>--MY-BLOG.</h1>
    <h1>Class And Object</h1><br>
    
    <h2>How We Create The Class</h2><br>
    <p>
class person:<br>
name="ved"<br>
city="ahemedabad"<br>
p1=person()<br>
print(p1.name)<br>
    </p>
    <h2>How We Can Change The Value Of Class</h2><br>
    <p>
    p1.name="rohit"<br>
    p1.city="mumbai"<br>
    print(p1.name) <br> 
</p>
<h1>How To Make An Object</h1><br>
<p>
    #object<br>
class student:<br>
    def __init__(self,name,age):<br>
        self.name=name<br>
        self.age=age<br>


class person1:<br>
    example="abcd"<br>
 def __init__(self,name,age):<br>
        self.name=name<br>
        self.age=age<br>

 def display_details(self):<br>
     print(f"name: {self.name}, age: {self.age} ")<br>

def celebrate_birthday(self):<br>
    self.age+=1
    print(f"happy birthday {self.name}! you are now {self.age} years old")<br>

#creatig object<br>
p1=person1("ved",17)<br>
p2=person1("virat",20)<br>


#accesing class atributs<br>
print(p1.example)<br>
print(p2.example)<br>

#accesing the instance atributes and methods<br>
print(p1.name)<br>
print(p1.age)<br>

p1.display_details()<br>
p2.display_details()<br>
p1.celebrate_birthday()<br>
</p>
</head>
<body>
    
</body>
</html>
