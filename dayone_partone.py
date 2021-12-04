with open('data.txt') as data:
    lines = data.readlines()

#print(lines)

newlist = []

for i in lines:
    new = i.replace("\n","")
    newlist.append(int(new))

#print(newlist)
#print(len(newlist))

count = 0
for x in newlist:
    if x < (x+1):
        newcount = count + 1
        print(newcount)
    else:
        newcount = count
print(newcount)

# for i in range(len(newlist)):
#     for j in range(i + 1, len(newlist)):
#         compare(mylist[i], mylist[j])
