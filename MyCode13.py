# Super class
class A:
    def __init__(self):
        print('in A Init')

    def feature1(self):
        print('Feature 1-A working')

    def feature2(self):
        print('Feature 2 working')

# Sub-class - Child class of A
class B(A):
    def __init__(self):
        # access Super class constructor
        super().__init__()
        print('in B Init')

    def feature1(self):
        super().feature1()
        print('Feature 1-B working')

    def feature4(self):
        print('Feature 4 working')

class D:
    def __init__(self):
        print('in D Init')

class C(B,D):
    def __init__(self):
        # MRO from left to right
        super().__init__()
        print('in C Init')

    def feat(self):
        super().feature1()

a1 = C()

a1.feature1()
a1.feat()


