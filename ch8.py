def chop(t):
    del t[0]
    del t[-1]
letters = ['q', 't', 'w', 'y']
letters2 = chop(letters)
print(letters2)