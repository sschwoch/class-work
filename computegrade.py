inp = input('Enter Grade here: ')
try:
    grade = float(inp)
except:
    print('Bad Score')
if grade > 1.0:
    print('Bad Score')
elif grade >= 0.9:
    print('A')
    print('Very good Score')
elif grade >= 0.8:
    print('B')
    print('Good Score')
elif grade >= 0.7:
    print('C')
    print('Okay Score')
elif grade >= 0.6:
    print('D')
    print('Bad Score')
elif grade < 0.6:
    print('F')
    print('Bad Score')