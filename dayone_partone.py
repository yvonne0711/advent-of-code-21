#code for aoc21
#1819819-20211204-da7d2d88

with open('data.txt') as data:
    lines = data.readlines()

newlist = []

for i in lines:
    new = i.replace("\n","")
    newlist.append(int(new))

#print(newlist)

count = 0
for i in range(1, len(newlist)):
    if newlist[i] > newlist[i-1]:
        count = count + 1

print(count)
