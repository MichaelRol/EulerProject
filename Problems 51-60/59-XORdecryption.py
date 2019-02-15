cipherwhole = open("p059_cipher.txt", "r")
for line in cipherwhole:
    cipher = line.split(",")



for x in range(97, 123):
    for y in range(97, 123):
        for z in range(97, 123):
            intmessage = []
            message = []
            for byte in range(0, len(cipher), 3):
                intmessage.append(int(cipher[byte]) ^ x)
                intmessage.append(int(cipher[byte+1]) ^ y)
                intmessage.append(int(cipher[byte+2]) ^ z)
            for byte in intmessage:
                message.append(str(chr(byte)))
            if ['t', 'h', 'e'] in message:
                print(''.join(message))

    


