onetonineteen = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', \
                 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = 7
and_ = 3
count = 0

for num in range(1, 1001):
    if num < 20:
        count = count + len(onetonineteen[num])
    if (num >= 20 and num < 40) or (num >= 80 and num < 100) :
        count = count + 6 + len(onetonineteen[num % 10])
    if (num >= 40 and num < 70):
        count = count + 5 + len(onetonineteen[num % 10])
    if num >= 70 and num < 80:
        count = count + 7 + len(onetonineteen[num % 10])
    if num >= 100 and num < 1000:
        if num % 100 == 0:
            count = count + hundred + len(onetonineteen[num / 100])
        else:
            remainder = num % 100
            count = count + len(onetonineteen[int(num/100)]) + hundred + and_
            if remainder < 20:
                count = count + len(onetonineteen[remainder])
            if (remainder >= 20 and remainder < 40) or (remainder >= 80 and remainder < 100) :
                count = count + 6 + len(onetonineteen[remainder % 10])
            if (remainder >= 40 and remainder < 70):
                count = count + 5 + len(onetonineteen[remainder % 10])
            if remainder >= 70 and remainder < 80:
                count = count + 7 + len(onetonineteen[remainder % 10])           
    if num == 1000:
        count = count + len("onethousand")
print(count)
