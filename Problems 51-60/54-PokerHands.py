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
                    if isThereFour(hands) != -1:
                        return(7, isThereFour(hands))
                    return (5, cards[max])
    if isStraight(hands)[0]:
        return(4, isStraight(hands)[1])
    if isThereThree(hands) != -1:
        return (3, isThereThree(hands))
    if twoPairs:
        return (2, highestPair(hands))  
    if highestPair(hands) != -1:
        return (1, highestPair(hands))
    highest = 0
    for hand in hands:
        for max in range(12, -1, -1):
            if cards[max] in hand and max > highest:
                highest = max
                break
    return (0, cards[max])

def twoPairs(hand):
    count = 0
    for card in hand:
        more = 0
        for other in hands:
            if card[0] == other[0]:
                more += 1
                if more == 2:
                    count += 1
    if count == 4:
        return True
    else:
        return False

def highestPair(hand):
    highestCard = -1
    for card in hand:
        count = 0
        for comp in hand:
            if card[0] == comp[0]:
                count += 1
                if count == 2 and card[0] > highestCard:
                    highestCard = card[0]
    return highestCard

def isThereThree(hand):
    for card in hand:
        count = 0
        for comp in hand:
            if card[0] == comp[0]:
                count += 1
                if count == 3:
                    return card[0]
    return -1

def isThereFour(hand):
    for card in hand:
        count = 0
        for comp in hand:
            if card[0] == comp[0]:
                count += 1
                if count == 4:
                    return card[0]
    return -1

def isStraight(hand):
    vals = []
    for card in hand:
        if card[0] == 'A':
            vals.append(1)
        elif card[0] == 'T':
            vals.append(10)
        elif card[0] == 'J':
            vals.append(11)
        elif card[0] == 'Q':
            vals.append(12)
        elif card[0] == 'K':
            vals.append(13)
        else:
            vals.append(int(card[0]))
    if int(max(vals)) - 1 in vals and int(max(vals)) - 2 in vals and int(max(vals)) - 3 in vals and int(max(vals)) - 4 in vals:
        return (True, max(vals))
    else:
        return (False, 0)


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