fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    exit()
for line in fhand:
    shout = line.rstrip().upper()
    print(shout)