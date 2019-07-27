# Demo the threading

from time import sleep
from threading import *

class Hello(Thread):
    # There is a run method within threading
    def run(self):
        for i in range(8):
            print('Hello')
            sleep(1)

class Hi(Thread):
    # There is a run method within threading
    def run(self):
        for i in range(8):
            print('Hi')
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
# avoid 2 threads collision
sleep(0.2)
t2.start()

# Wait for completion of t1 thread and t2 thread (Stop the thread)
t1.join()
t2.join()
print('Bye')