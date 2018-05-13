count = 0
newdictionary = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count = count + 1
        if word in newdictionary : continue
        newdictionary[word] = count

inp = input('Check word: ')
if inp in newdictionary:
    print('True')
else:
    print('False')