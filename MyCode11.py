
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # Create instant object of sub-class variable
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        # display instant object of sub-class
        self.lap.show()

    # Inner class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu ='i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Navin',2)
s2 = Student('Jenny',3)

s1.show()