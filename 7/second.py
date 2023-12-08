import math 

file1 = open('7/_input.txt', 'r')
Lines = file1.readlines()

def getLineValues(line):
    cards = line.strip().split()[0]
    # print(cards)
    cardValue=0

    cardDict=[
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ]
    jacks = 0
    for i in cards:
        cardValue *= 100
        j = 0
        if i == 'T':
            j = '10'
        elif i == 'J':
            j = '1'
        elif i == 'Q':
            j = '12'
        elif i == 'K':
            j = '13'
        elif i == 'A':
            j = '14'
        else:
            j = int(i)
        cardValue += int(j)
        if j == '1':
            jacks +=1
        else: 
            cardDict[int(j)] +=1
    combinationValue=0
    cardDict.sort()
    cardDict[len(cardDict)-1] += jacks
    for y in cardDict:
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
    # print(cards[i],value,'*',i+1)
    print(cards[i][1].split()[0])
    sum += (i+1)*value
    # print(value)

print("sum",sum)