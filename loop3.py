largest = None
smallest = None
num = None
while True:
    inp = input('Enter number here: ')
    if inp == 'done' :
        break
    try:
        num = float(inp)
    except:
        print('Invalid input')
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
print('Maximum is ', largest)
print('Minimum is ', smallest)