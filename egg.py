fname = input('Enter the file name: ')
try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU TOO! - Gotchya!')
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        colonpos = line.find(':')
        number = line[colonpos+1:].rstrip()
        Confidence = float(number)
        total = total + Confidence
average = total/count
print('Count', count)
print('Total', total)
print('Average Spam Confidence', average) 