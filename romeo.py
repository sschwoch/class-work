mylist = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        mylist.append(word)
print(sorted(mylist))