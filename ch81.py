def middle(t):
    del t[0]
    del t[-1]
letters = ['q', 't', 'w', 'y']
letters2 = middle(letters)
print(letters)