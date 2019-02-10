def bestHand(hand):
    if isRoyalFlush(hand):
        return (9, 14)
    if isStraightFlush(hand) != -1:
        return (8, isStraightFlush(hand))
    if isThereFour(hand) != -1:
        return (7, isThereFour(hand))
    if isFullHouse(hand) != -1:
        return (6, isFullHouse(hand))
    if isFlush(hand) != -1:
        return (5, isFlush(hand))
    if isStraight(hand) != -1:
        return (4, isStraight(hand))
    if isThereThree(hand) != -1:
        return (3, isThereThree(hand))
    if twoPairs:
        return (2, highestPair(hand))  
    if highestPair(hand) != -1:
        return (1, highestPair(hand))
    highest = 0
    for card in hand:
        if card[0] > highest:
            highest = card[0]
    return (0, highest)

def isFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        for max in range(14, 4, -1):
            for card in hand:
                if card[0] == max:
                    return card[0]
    return -1

def isStraightFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        for max in range(14, 4, -1):
            if (max, hand[0][1]) in hand:
                if (max - 1, hand[0][1]) in hand and (max - 2, hand[0][1]) in hand \
                        and (max - 3, hand[0][1]) in hand and (max - 4, hand[0][1]) in hand:
                    return max
    return -1

def isRoyalFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        if (14, hand[0][1]) in hand and (13, hand[0][1]) in hand and (12, hand[0][1]) in hand and (11, hand[0][1]) in hand and (10, hand[0][1]) in hand:
            return True
    return False

def twoPairs(hand):
    count = 0
    for card in hand:
        more = 0
        for other in hand:
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

def isFullHouse(hand):
    if isThereThree(hand) != -1 and isThereFour == -1:
        threeCard = isThereThree(hand)
        for card in hand:
            if threeCard == card[0]:
                hand.remove(card)
        if hand[0][0] == hand[1][0]:
            return threeCard
    return -1

def isStraight(hand):
    vals = []
    for card in hand:
        vals.append(card[0])
    if max(vals) in vals and (max(vals) - 1) in vals and (max(vals) - 2) in vals and (max(vals) - 3) in vals and (max(vals) - 4) in vals:
        return max(vals)
    return -1

def whoHasHighCard(hand1, hand2):
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest1:
            highest1 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2
    for card in hand1:
        if card[0] == highest1:
            hand1.remove(card)
    for card in hand2:
        if card[0] == highest1:
            hand2.remove(card)
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest1:
            highest1 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2
    for card in hand1:
        if card[0] == highest1:
            hand1.remove(card)
    for card in hand2:
        if card[0] == highest1:
            hand2.remove(card)
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest1:
            highest1 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2

        


handslist = open("poker.txt", "r")
player1wins = 0
count = 0
for hands in handslist:
    hands = hands.replace("\n", "")
    hands = hands.split(" ")
    firsthand = []
    for hand in hands[0:5]:
        if hand[0] == 'A':
            firsthand.append((14, hand[1]))
        elif hand[0] == 'T':
            firsthand.append((10, hand[1]))
        elif hand[0] == 'J':
            firsthand.append((11, hand[1]))
        elif hand[0] == 'Q':
            firsthand.append((12, hand[1]))
        elif hand[0] == 'K':
            firsthand.append((13, hand[1]))
        else:
            firsthand.append((int(hand[0]), hand[1]))
    secondhand = []
    for hand in hands[5:10]:
        if hand[0] == 'A':
            secondhand.append((14, hand[1]))
        elif hand[0] == 'T':
            secondhand.append((10, hand[1]))
        elif hand[0] == 'J':
            secondhand.append((11, hand[1]))
        elif hand[0] == 'Q':
            secondhand.append((12, hand[1]))
        elif hand[0] == 'K':
            secondhand.append((13, hand[1]))
        else:
            secondhand.append((int(hand[0]), hand[1]))
    bestHand1 = bestHand(firsthand)
    bestHand2 = bestHand(secondhand)
    if bestHand1[0] > bestHand2[0]:
        player1wins += 1
    if bestHand1[0] == bestHand2[0]:
        if bestHand1[1] > bestHand2[1]:
            player1wins += 1
        if bestHand1[1] == bestHand2[1]:
            print(firsthand, secondhand)
            if whoHasHighCard(firsthand, secondhand) == 1:
                player1wins += 1
print(player1wins)