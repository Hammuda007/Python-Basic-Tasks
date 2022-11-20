# 1 : Create a simple function that takes 2 numbers and print their values

def num(x,y):
    print('num')
   

print(10,5)


# 2 : Create a simple function that takes 2 numbers and return their values

def num(x,y):
    print('num')
    return
   

print(3,7)


# 3 : In the above return function, use keyword arguments when calling the function

def sum(x,y=1):
    result=x+y
    return result
f=sum(7)
   

print(f)


# 4 : In the above return function , give x and y default values of 0 and call the function with no arguments

def sum(x=0,y=0):
    result=x+y
    return result
f=sum()
   

print(f)


# 5 : Creat a function that can take any number of arguments and print the sum of them

def mysum(arg,*vartuple):
    result=arg + sum(vartuple)
    return result
f=mysum(4,5,6,8,9,0,1)
   

print(f)


# 6 : Creat the same sum function using the lambda


def mysum(arg,*vartuple):
    result=arg + sum(vartuple)
    return result
f=mysum(4,5,6,8,9,0,1)
   

print(f)




mysum2= lambda arg,*vartuple : arg + sum(vartuple)

f=mysum(4,5,6,8,9,0,1)
   

print(f)


# 7 : call the lambda function at the same definition line

x=(lambda a,b : a+b)(12,5)
print (x)


# 8 : Write the difference between the local variable and global variabel
'''
any change seening on the def ist local , that mean out this def code do not seeing , out the code is Global , so when i want to make change into the def i need to use or write global in this def  the de
'''


