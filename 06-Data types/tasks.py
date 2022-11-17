# 1 : What the different between '' ""  ''' '''
'''
'' "" the same when we need to print string
''' ''' we use it when we need to print more than one string in one line
'''

# 2 : Create a string with the name 'mystro'
''''
x='mystro'
print (x)
'''

# 3 : Make the string letters capital
'''
x='mystro'
print(x.upper())
'''

# 4 : Create a list of values from 10 to 20
'''
x=[10,11,12,13,14,15,16,17,18,19,20]
print (x)
'''

# 5 : Add 30 to the end of the list
'''
x=[10,11,12,13,14,15,16,17,18,19,20]
x.append(30)
print (x)
'''

# 6 : Add 40 as the second element of the list
'''
x=[10,11,12,13,14,15,16,17,18,19,20]
x.append(30)
x.insert(1,40)
print (x)
'''

# 7 : Print how many elements in the list
'''
x=[10,11,12,13,14,15,16,17,18,19,20]
print(len(x))
'''

# 8 : replace the second element in the list with 100
'''
x=[10,11,12,13,14,15,16,17,18,19,20]
x[1]=100
print(x)
'''

# 9 : Create a tuple with values from 1 to 5
'''
x= (1,2,3,4,5)
print(x)
'''

# 10 : Can we add 10 to the end of the tuple
'''
yes but we need first to convert tuple to the list

x= (1,2,3,4,5)
y=list(x)
y.append(10)
print(y)
'''

# 11 : Create a dict of value Mahmoud:28, ahmed:30
'''
p={'Mahmoud':28, 'ahmed':30}
print(p)
'''

# 12 : Print Mahmoud age from the dict
'''
p={'Mahmoud':28, 'ahmed':30}
print(p['Mahmoud'])
'''

# 13 : What is the different between mutable and immutable data types
'''
mutable:In Python programming language whenever an object is susceptible to internal change or has the ability to change its values is known as a mutable object. Mutable objects in Python are generally changed after creation. 

For mutable objects in Python, their values can be changed but the identity of the object remains intact. The objects in Python which are mutable are provided below:

Lists
Dicts
Sets
User-Defined Classes 
Dictionaries

immutable: Similarly, when the objects in the Python are not susceptible to the internal change are known as the immutable objects. They can not be modified once they are created. For example, int in Python is immutable hence they can not be modified once they are created.

Objects in Python which are immutable are shown below:


int
float
bool
string
Unicode
tuple
Numbers
Frozen Sets
User-Defined Classes    
    
'''

