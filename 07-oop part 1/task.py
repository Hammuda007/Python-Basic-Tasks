# 1 Explain in few words what we mean by a class give and example
'''
A Python class is like an outline for creating a new object. An object is anything that you wish to manipulate or change while working through the code.
For example, __doc__ gives us the docstring of that class
'''

# 2 create a simple class names calculator

class Calc:


# 3 Create a constructor that prints Welcome message

class Calc:
    def __init__(self):
        print('Welcome')
    
c1=Calc()


# 4 Add 2 methods to the class sum & mull

class Calc:
    def __init__(self):
        print('Welcome')
    def sum(self):
        pass
        
    def mull(self):
        pass
        


# 5 The sum method return the sum of 2 arguments x and y

class Calc:
    def sum(self,x,y):
        print(x+y)


# 6  The mull method return the multiplication of the arguments x and y

class Calc:
    def mull(self,x,y):
        print(x*y)


# 7 Take an object from the class

class Calc:
    def sum(self,x,y):
        print(x+y)

    def mull(self,x,y):
        print(x*y)



c1=Calc()



# 8 Call the sum method with 10 , 20

class Calc:
    def sum(self,x,y):
        print(x+y)

    def mull(self,x,y):
        print(x*y)



c1=Calc()
c1.sum(10,20)


# 9 Call the mull method with 10 , 20

class Calc:
    def sum(self,x,y):
        print(x+y)

    def mull(self,x,y):
        print(x*y)



c1=Calc()
c1.mull(10,20)


# 10 Explain in few words why we call the self in methods
'''
By using the “self”  we can access the attributes and methods of the class in python.
It binds the attributes with the given arguments
'''

# 11 What we mean with OOP 4 Pillars
'''
.Abstraction
.Encapsulation
.Inheritance
.Polymorphism
'''

# 12 Why we use OOP in our code
'''
OOP language allows to break the program into the bit-sized problems that can be solved easily (one object at a time). 
'''



        






    

        
