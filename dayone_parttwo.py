with open('data.txt') as data:
    lines = data.readlines()

newlist = []

for i in lines:
    new = i.replace("\n","")
    newlist.append(int(new))

three=[]
for i in range(2,len(newlist)):
    total = newlist[i] + newlist[i-1] + newlist[i-2]
    three.append(total)

print(three)

count = 0
for i in range(1, len(three)):
    if three[i] > three[i-1]:
        count = count + 1

print(count)
