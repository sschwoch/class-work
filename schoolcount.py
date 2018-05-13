schoolcount = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': continue
    else:
        atposition = words[1].find('@')
        domain = words[1][atposition+1:]
        if domain not in schoolcount:
            schoolcount[domain] = 1
        else:
            schoolcount[domain] += 1
print(schoolcount)