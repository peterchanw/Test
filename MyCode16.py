
class TopTen:

    def __init__(self):
        self.num = 1

    # Create your own iterator object
    def __iter__(self):
        return self

    # Redefine the next method for next object
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()
for i in values:
    print(i)
print('*'*30)

# Demo the Generators
def topten():
    n = 1
    while n<= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)