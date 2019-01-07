import decimal

d = 0
largest = 0

for x in range (1, 1000):
    val = decimal.Decimal(1.00)/decimal.Decimal(x)
    strval = str(val)
