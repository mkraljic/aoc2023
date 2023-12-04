
file1 = open('_input.txt', 'r')
Lines = file1.readlines()

red = 12
green = 13
blue = 14

sum = 0
for line in Lines:
    pow = 0
    card = line.strip().split(": ")
    cardNr = card[0].split(" ")[1]
    print (cardNr,card[1])
    winingNumbers = card[1].split(" | ")[0].split(" ")
    scrathedNumbers = card[1].split(" | ")[1].split(" ")
    print(winingNumbers, scrathedNumbers)
    for nr in winingNumbers:
        if (nr != ''):
            if nr in scrathedNumbers:
                if pow == 0:
                    pow = 1
                else:
                    pow *= 2
        pass
    print(pow)
    sum += pow

print(sum)