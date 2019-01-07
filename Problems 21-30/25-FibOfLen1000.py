x = 2
y = 1
fib = 0
count = 3
while (True):
    fib = x + y
    count += 1
    y = x
    x = fib
    if len(str(fib)) == 1000:
        print(count)
        break