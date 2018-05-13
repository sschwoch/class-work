hours = float(input('Enter hours worked: '))
rate = float(input('Pay rate : '))
if hours > 40:
    pay = (hours - 40) * (rate * 1.5) + (40 * rate)
    print(pay)
if hours < 41:
    pay = rate * hours
    print(pay)