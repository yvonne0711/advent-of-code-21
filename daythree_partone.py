with open('data3.txt') as data3:
    lines = data3.readlines()

print(lines)

newlist = []

for i in lines :
    new = i.replace('\n','')
    bit = list(str(new))
    newlist.append(bit)

# for i in lines:
#     new = i.replace("\n","")
#     newlist.append(new)
#
# print(newlist)
# secondlist=[]

# for i in newlist:
#     bit = list(i)
#     secondlist.append(bit)

print(newlist)

# for binary line in newlist:
#    for every x entry:
#        if x entry = '0':
#              zero count add 1
#         if x entry = '1':
#               one count add 1
#    if zero count > one count:
#          gamma.binary.append('0')

# gamma
# epsilon
# pc = gamma*epsilon

# for each i in first index, return most common one
# store it and return as x

# or def function, first index = going through all the first indices of each line of binary
# if more 1s than 0s (if count(1)>count(0), x=1 or return 1, else x=0, return 0

# at the end xyzab

# most common bit in the corresponding position of all numbers ie most 1s in this position of each binary
# least common bit is epsilon
