# 1 Create a new class names SciCalc with 3 methods ,sum , mull , power all of them takes 2 argument x, y

class SciCalc:
    def sum(self,x,y):
        pass
    def mull(self,x,y):
        pass
    def power(self,x,y):
        pass
    


# 2 Sum return the sum of x and y

class SciCalc:
    def sum(self,x,y):
       print(x+y)
    


c1= SciCalc()



#3 Mull return the multiplication of x and y

class SciCalc:
    def mull(self,x,y):
       print(x*y)
    


c1= SciCalc()


# 4 The power return x power y

class SciCalc:
    def power(self,x,y):
       print(x**y)
    


c1= SciCalc()


# 5 Take an object from the class and call the 3 methods with any numbers

class SciCalc:
    def sum(self,x,y):
       print(x+y)
    def mull(self,x,y):
       print(x*y)
    def power(self,x,y):
       print(x**y)
c1= SciCalc()
c1.sum(3,5)
c1.mull(7,9)
c1.power(2,5)


# 6 Can we inherit from the class we created in the first task Calc
'''
yes we can 
'''
# 7 Inherit from the Calc class , now remove the unneeded code the the SciCalc after inheriting

class Calc:
    def sum(self,x,y):
        print(x+y)

    def mull(self,x,y):
        print(x*y)

class SciCalc(Calc):
    def power(self,x,y):
       print(x**y)







# 8 call the 3 methods again from the SciCalc object


class Calc:
    def sum(self,x,y):
        print(x+y)

    def mull(self,x,y):
        print(x*y)

class SciCalc(Calc):
    def power(self,x,y):
       print(x**y)



c1= SciCalc()
c1.sum(3,5)
c1.mull(7,9)
c1.power(2,5)


# 9 Now you should see the same result as before
'''
yes, i have the same result
'''

# 10  Explain in few words what happened after inheriting
'''
after that we have a short code and we do not need to repeat the instructions again in other class
'''
