cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def bestHand(hands):
    if hands[0][1] == hands[1][1] == hands[2][1] == hands[3][1] == hands[4][1]:
        if "A" + hands[0][1] in hands and "K" + hands[0][1] in hands and "Q" + hands[0][1] in hands and "J" + hands[0][1] in hands and "T" + hands[0][1] in hands:
            return (9, "A")
        else:
            for max in range(12, 4, -1):
                if cards[max] + hands[0][1] in hands:
                    if cards[max - 1] + hands[0][1] in hands and cards[max - 2] + hands[0][1] in hands \
                        and cards[max - 3] + hands[0][1] in hands and cards[max - 4] + hands[0][1] in hands:
                        return (8, cards[max])
                    return (5, cards[max])
    highest = 0
    for hand in hands:
        for max in range(12, -1, -1):
            if cards[max] in hand and max > highest:
                highest = max
                break
    return (0, cards[max])


handslist = open("poker.txt", "r")

player1wins = 0
for hands in handslist:
    hands = hands.replace("\n", "")
    hands = hands.split(" ")
    firsthand = hands[0:5]
    secondhand = hands[5:10]
    bestHand1 = bestHand(firsthand)
    bestHand2 = bestHand(secondhand)
    if bestHand1[0] > bestHand2[0]:
        player1wins += 1
    if bestHand1[0] == bestHand2[0]:
        if bestHand1[1] > bestHand2[1]:
            player1wins += 1
print(player1wins)