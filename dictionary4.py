addressdictionary = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': continue
    else:
        if words[1] not in addressdictionary:
            addressdictionary[words[1]] = 1
        else:
            addressdictionary[words[1]] += 1
print(addressdictionary)