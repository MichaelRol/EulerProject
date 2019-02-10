def bestHand(hand):
    if isRoyalFlush(hand):
        return 9
    if isStraightFlush(hand):
        return 8
    if isThereFour(hand):
        return 7
    if isFullHouse(hand):
        return 6
    if isFlush(hand):
        return 5
    if isStraight(hand):
        return 4
    if isThereThree(hand):
        return 3
    if twoPairs(hand):
        return 2
    if highestPair(hand):
        return 1
    highest = 0
    for card in hand:
        if card[0] > highest:
            highest = card[0]
    return 0

def isFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        for max in range(14, 4, -1):
            for card in hand:
                if card[0] == max:
                    return True
    return False

def isStraightFlush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        for max in range(14, 4, -1):
            if (max, hand[0][1]) in hand:
                if (max - 1, hand[0][1]) in hand and (max - 2, hand[0][1]) in hand \
                        and (max - 3, hand[0][1]) in hand and (max - 4, hand[0][1]) in hand:
                    return True
    return False

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
    highestCard = False
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
                    return True
    return False

def isThereFour(hand):
    for card in hand:
        count = 0
        for comp in hand:
            if card[0] == comp[0]:
                count += 1
                if count == 4:
                    return True
    return False

def isFullHouse(hand):
    if isThereThree(hand) != False and isThereFour == False:
        threeCard = isThereThree(hand)
        for card in hand:
            if threeCard == card[0]:
                hand.remove(card)
        if hand[0][0] == hand[1][0]:
            return True
    return False

def isStraight(hand):
    vals = []
    for card in hand:
        vals.append(card[0])
    if max(vals) in vals and (max(vals) - 1) in vals and (max(vals) - 2) in vals and (max(vals) - 3) in vals and (max(vals) - 4) in vals:
        return True
    return False

def whoHasHighCard(hand1, hand2):
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest2:
            highest2 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2
    else:
        return 0
    for card in hand1:
        if card[0] == highest1:
            hand1.remove(card)
    for card in hand2:
        if card[0] == highest2:
            hand2.remove(card)
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest2:
            highest2 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2
    for card in hand1:
        if card[0] == highest1:
            hand1.remove(card)
    for card in hand2:
        if card[0] == highest2:
            hand2.remove(card)
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest2:
            highest2 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest2:
            highest2 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2
    highest1 = 0
    highest2 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    for card in hand2:
        if card[0] > highest2:
            highest2 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2

def bothFullHouse(hand1, hand2):
    three1 = 0
    three2 = 0
    pair1 = 0
    pair2 = 0
    count = 0
    for card in hand1:
        for other in hand1:
            if card[0] == other[0]:
                count += 1
        if count == 3:
            three1 = card[0]
        else:
            pair1 = card[0]
    for card in hand2:
        for other in hand2:
            if card[0] == other[0]:
                count += 1
        if count == 3:
            three2 = card[0]
        else:
            pair2 = card[0]
    if three1 > three2:
        return 1
    elif three2 > three1:
        return 2
    else:
        if pair1 > pair2:
            return 1
        else:
            return 2
        
def bothPair(hand1, hand2):
    high1 = highestPair(hand1)
    high2 = highestPair(hand2)
    if high1 > high2:
        return 1
    if high2 > high1:
        return 2
    for card in hand1:
        if card[0] == high1:
            hand1.remove(card)
    for card in hand2:
        if card[0] == high2:
            hand2.remove(card)
    highest1 = 0
    for card in hand1:
        if card[0] > highest1:
            highest1 = card[0]
    highest2 = 0
    for card in hand2:
        if card[0] > highest2:
            highest2 = card[0]
    if highest1 > highest2:
        return 1
    if highest2 > highest1:
        return 2
    

def bothFoaK(hand1, hand2):
    side1 = 0
    side2 = 0
    for card in hand1:
        for comp in hand1:
            if card[0] == comp[0]:
                for weird in hand1:
                    if weird[0] != card[0]:
                        side1 = weird[0]
    for card in hand2:
        for comp in hand2:
            if card[0] == comp[0]:
                for weird in hand2:
                    if weird[0] != card[0]:
                        side2 = weird[0]
    if side1 > side2:
        return 1
    else:
        return 2
    

    
handslist = open("poker.txt", "r")
player1wins = 0
for hands in handslist:
    hands = hands.replace("\n", "")
    hands = hands.split(" ")
    hand1 = []
    for hand in hands[0:5]:
        if hand[0] == 'A':
            hand1.append((14, hand[1]))
        elif hand[0] == 'T':
            hand1.append((10, hand[1]))
        elif hand[0] == 'J':
            hand1.append((11, hand[1]))
        elif hand[0] == 'Q':
            hand1.append((12, hand[1]))
        elif hand[0] == 'K':
            hand1.append((13, hand[1]))
        else:
            hand1.append((int(hand[0]), hand[1]))
    hand2 = []
    for hand in hands[5:10]:
        if hand[0] == 'A':
            hand2.append((14, hand[1]))
        elif hand[0] == 'T':
            hand2.append((10, hand[1]))
        elif hand[0] == 'J':
            hand2.append((11, hand[1]))
        elif hand[0] == 'Q':
            hand2.append((12, hand[1]))
        elif hand[0] == 'K':
            hand2.append((13, hand[1]))
        else:
            hand2.append((int(hand[0]), hand[1]))
    bestHand1 = bestHand(hand1)
    bestHand2 = bestHand(hand2)
    if bestHand1 > bestHand2:
        player1wins += 1
    if bestHand1 == bestHand2:
        if bestHand1 == 7:
            print("7")
            if bothFoaK(hand1, hand2) == 1:
                player1wins += 1
        elif bestHand1 == 6:
            print("6")
            if bothFullHouse(hand1, hand2) == 1:
                player1wins += 1
        elif bestHand1 == 5:
            print("5")
        elif bestHand1 == 4:
            print("4")
        elif bestHand1 == 3:
            print("3")
        elif bestHand1 == 2:
            print("2")
        elif bestHand1 == 1:
            if bothPair(hand1, hand2) == 1:
                player1wins += 1                
        elif whoHasHighCard(hand1, hand2) == 1:
            player1wins += 1
print(player1wins)
