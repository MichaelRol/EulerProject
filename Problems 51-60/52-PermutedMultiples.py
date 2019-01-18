def sameDigits(val1, val2):
    val1str = str(val1)
    val2str = str(val2)
    if len(val1str) != len(val2str):
        return False

    for digit in val1str:
        val2str = val2str.replace(digit, '',1)
    
    if val2str == '':
        return True
    else:
        return False


for x in range(10, 1000000):
    if sameDigits(x, 2*x) and sameDigits(x, 3*x) and sameDigits(x, 4*x) and sameDigits(x, 5*x) and sameDigits(x, 6*x):
        print(x)