with open('data2.txt') as data2:
    lines = data2.readlines()

#print(lines)

newlist = []

for i in lines:
    new = i.replace("\n","")
    newlist.append(new)

#print(newlist)

finallist = []

for i in newlist:
    splitting = i.split(" ")
    finallist.append(splitting)

#print(finallist)

x=0
y=0
aim=0

for sublist in finallist:
    #print(sublist)
    #print(sublist[0])
    if sublist[0] == 'forward':
        x=x+int(sublist[1])
        y=y+(int(aim)*int(sublist[1]))
    elif sublist[0] == 'down':
        aim=aim+int(sublist[1])
        #y=y+int(sublist[1])
    elif sublist[0] == 'up':
        aim=aim-int(sublist[1])
        #y=y-int(sublist[1])

print(x*y)