total = 2
x = 2
y = 1
fib = 0
while (fib <= 4000000):
    fib = x + y
    y = x
    x = fib
    if (fib % 2 == 0 and fib <= 4000000):
        total = total + fib

print(total)