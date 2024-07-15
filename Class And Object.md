<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <h1>--MY-BLOG.</h1>
    <h1>Class And Object</h1><br>
    
 <h2>How We Create The Class</h2><br>
 
    class person:
        name="ved"
        city="ahemedabad"
        p1=person()
        print(p1.name)
    
<h2>How We Can Change The Value Of Class</h2><br>
    
    p1.name="rohit"
    p1.city="mumbai"
    print(p1.name) 

<h1>How To Make An Object</h1><br>

    #object
     class student:
        def __init__(self,name,age):
          self.name=name
          self.age=age


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

      #creatig object
     p1=person1("ved",17)
    p2=person1("virat",20)


    #accesing class atributs
    print(p1.example)
    print(p2.example)

    #accesing the instance atributes and methods
    print(p1.name)
    print(p1.age)

     p1.display_details()
    p2.display_details()
    p1.celebrate_birthday()

</head>
<body>
    
</body>
</html>
