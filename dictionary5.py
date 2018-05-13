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
    for key in addressdictionary:
        print(key, addressdictionary[key])

maximum_loop = 0
for address in addressdictionary:
    if addressdictionary[address] > maximum_loop:
        maximum_loop = addressdictionary[address]
        maximum_loop_address = address
print('Maximum:', maximum_loop_address, maximum_loop)
