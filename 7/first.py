import math 

file1 = open('7/_input.txt', 'r')
Lines = file1.readlines()

def getLineValues(line):
    cards = line.strip().split()[0]
    # print(cards)
    cardValue=0

    cardDict={
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        'T': 0,
        'J': 0,
        'Q': 0,
        'K': 0,
        'A': 0
    }

    for i in cards:
        cardValue *= 100
        j = 0
        if i == 'T':
            j = 10
        elif i == 'J':
            j = 11
        elif i == 'Q':
            j = 12
        elif i == 'K':
            j = 13
        elif i == 'A':
            j = 14
        else:
            j = int(i)
        cardValue += j
        cardDict[i] +=1
    combinationValue=0
    for x, y in cardDict.items():
        if y > 1:
            combinationValue += pow(y,3)
    cardValue *= math.pow(10,combinationValue)
    # print(line.strip(),cardValue)
    return cardValue

sum = 0

cards = []
for line in Lines:
    cardSet = []
    cardSet.append(getLineValues(line))
    cardSet.append(line.strip())
    cards.append(cardSet)
    # print(cardSet)

cards.sort()
# print(cards)

for i in range(0, len(cards)):
    value = int(cards[i][1].split()[1])
    # print(sum)
    print(cards[i],value,'*',i+1)
    # print(cards[i][0])
    sum += (i+1)*value
    # print(value)

print("sum",sum)