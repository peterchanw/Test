# read file in text format
f = open('MyData','r')
# write file in text format
f1 = open('abc','w')

for data in f:
    f1.write(data)

# read file in binary format
f2 = open('Sydney_Firework_2019.jpg','rb')
# write file in binary format
f3 = open('MyPic.jpg','wb')
for data in f2:
    f3.write(data)

# print(f.read())
# print(f.readline(), end ='')
# print(f.readline())

# append data to a file
# f1 = open('abc','a')
# f1.write('Hello')
# f1.writelines('Test')

"""
Use for documentation
"""