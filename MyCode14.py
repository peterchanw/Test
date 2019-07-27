
class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')

class Laptop:
    # Duck Typing - similar behavior pass for execution
    def code(self,ide):
        ide.execute()

ide = MyEditor()
lap1 = Laptop()
# Looking for the similar behaviour method
lap1.code(ide)

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    # Operator Overloading - define additional add operation
    def __add__(self, other):
        # define the operation
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        # return the object
        s3 = Student(m1,m2)
        return s3

    # Operator Overloading - define additional string operation
    def __str__(self):
        return '({},{})'.format(self.m1,self.m2)

x1 = 5
x2 = 6
print(x1 + x2)
print(int.__add__(x1,x2))

s1 = Student(58,69)
s2 = Student(60,65)
s3 = s1 + s2
print(s3.m1, s3.m2)

# Need to redefine __str()__ to print the value of the object
print(s1)
print(s2)
print(s3)
