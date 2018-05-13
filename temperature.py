inp = input('Enter Fahrenheit Temperature: ')
except:
    print('Error, please print a numeric input')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)