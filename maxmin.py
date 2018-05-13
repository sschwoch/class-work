mylist = []
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    mylist.append(inp)
print('Max:', max(mylist))
print('Min:', min(mylist))
    