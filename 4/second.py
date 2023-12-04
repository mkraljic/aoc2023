
file1 = open('_input.txt', 'r')
Lines = file1.readlines()

sum = 0
cards = []
cardNr = 0
for line in Lines:
    score = 0
    card = line.strip().split(": ")
    # print (cardNr,card[1])

    if cardNr < len(cards):
        cards[cardNr] += 1
    else:
        cards.append(1)

    winingNumbers = card[1].split(" | ")[0].split(" ")
    scrathedNumbers = card[1].split(" | ")[1].split(" ")
    # print(winingNumbers, scrathedNumbers)
    for nr in winingNumbers:
        if (nr != ''):
            if nr in scrathedNumbers:
                score += 1
        pass
    
    for j in range(0, cards[cardNr]):
        for i in range(1, score+1):
            if cardNr+i < len(cards):
                cards[cardNr+i] += 1
            else:
                cards.append(1)

    print(score,cards[cardNr])
    sum += score * cards[cardNr]
    sum += 1 # add current card
    cardNr += 1

print(sum)