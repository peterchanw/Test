
class Computer:
    # class variables (static variables)
    monitor = 'XGA'
    resolution = '1024 x 768'

    # initialiation method for object
    def __init__(self):
        self.CPU = 'i7'
        self.RAM = '2gb'
        self.HDD = '250MB'

    # instant method - pass values
    def update(self,CPU,RAM,HDD):
        self.CPU = CPU
        self.RAM = RAM
        self.HDD = HDD

    # instant method - pass object
    def compare(self,obj):
        CPU = False
        RAM = False
        HDD = False
        if self.CPU == obj.CPU:
            print("Same CPU")
            CPU = True
        else:
            print("Different CPU")
        if self.RAM == obj.RAM:
            print("Same RAM")
            RAM = True
        else:
            print("Different RAM")
        if self.HDD == obj.HDD:
            print("Same HDD")
            HDD = True
        else:
            print("Different HDD")
        if CPU==True and RAM==True and HDD==True:
            print("They are the same")

    # class method example
    @classmethod
    def type(cls):
        return cls.monitor, cls.resolution

    # static method - information of the class
    @staticmethod
    def info():
        print ('This is the test of class')

com1 = Computer()
com2 = Computer()

com1.update('i5','2gb','250MB')

# update class variable
Computer.monitor = 'VGA'
Computer.resolution = '640 x 480'

print(com1.CPU,com1.HDD,com1.RAM,com1.monitor,com1.resolution)
print(com2.CPU,com2.HDD,com2.RAM,com2.monitor,com2.resolution)
com1.compare(com2)

# demo class method
print(Computer.type())
# demo the static method
Computer.info()
