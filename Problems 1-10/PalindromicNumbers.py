pal = 0
for i in range(100, 999):
    for j in range(100, 999):
        if str(i * j) == str(i * j)[::-1]:
            if pal < i * j:
                pal = i * j
print(pal)