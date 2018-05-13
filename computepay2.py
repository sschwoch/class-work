hours = float(input('Enter hours worked: '))
try:
    hours = float(hours)
except:
    print('Error, please enter a numeric input')
rate = float(input('Pay rate : '))
try:
    rate = float(rate)
except:
    print('Error, please enter a numeric input')
if hours > 40:
    pay = (hours - 40) * (rate * 1.5) + (40 * rate)
    print(pay)
elif hours < 41:
    pay = rate * hours
    print(pay)