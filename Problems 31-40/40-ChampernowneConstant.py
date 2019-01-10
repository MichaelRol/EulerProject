

const = ""
for x in range(1, 1000000):
    const = const + str(x)

print(int(const[0]) * int(const[9]) * int(const[99]) * int(const[999]) * int(const[9999]) * int(const[99999]) * int(const[999999]))