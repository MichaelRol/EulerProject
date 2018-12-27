n = input("Enter a number: ")
i = 1
val = 0
while i <= n:
    if n % i == 0:
        j = 2
        prime = True
        while prime and j < i:
            if i % j == 0:
                prime = False
            else:
                j = j + 1
        if prime:
            val = i
    i = i + 1

print(val)


