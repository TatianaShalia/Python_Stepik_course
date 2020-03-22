a = int(input('Enter your first value '))
b = int(input('Enter your second value '))
a += -a%3
b -= b%3
avg = (a+b)/2
print(avg)