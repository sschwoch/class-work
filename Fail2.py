fhand = open('exercise8.txt')
for line in fhand:
    words = line.split()
        #Debug
    if len(words) == 0 and len(words) < 2 : continue
    if words[0] != 'From' : continue
    print(words[2])