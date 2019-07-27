a = 10

def something():
    a = 9
    x = globals()['a']
    print('in function', a)
    print('in function', x)

something()
print('outside',a)