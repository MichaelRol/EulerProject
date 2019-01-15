# Solution adapted from https://www.mathblog.dk/project-euler-26-find-the-value-of-d-1000-for-which-1d-contains-the-longest-recurring-cycle/

sequenceLength = 0
d = 0
for i in range(1000, 1, -1):
    if sequenceLength >= i:
        break
 
    foundRemainders = [0]*i
    value = 1
    position = 0
 
    while foundRemainders[value] == 0 and value != 0:
        foundRemainders[value] = position
        value *= 10
        value %= i
        position += 1
    
 
    if position - foundRemainders[value] > sequenceLength:
        sequenceLength = position - foundRemainders[value]
        d = i

print(d)

