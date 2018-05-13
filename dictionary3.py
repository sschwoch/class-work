daydictionary = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': continue
    else:
        if words[2] not in daydictionary:
            daydictionary[words[2]] = 1
        else:
            daydictionary[words[2]] += 1
print(daydictionary)