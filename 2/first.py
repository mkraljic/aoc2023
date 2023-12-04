
file1 = open('_input.txt', 'r')
Lines = file1.readlines()

red = 12
green = 13
blue = 14

sum = 0
for line in Lines:
    gamePossible = True
    game = line.strip().split(": ")
    gameNr = game[0].split(" ")[1]
    print (gameNr,game[1])
    rounds = game[1].split("; ")
    for round in rounds:
        # print(round)
        cubeSet = round.split(", ")
        # print(cubeSet)
        for hand in cubeSet:
            colorHand = hand.split(" ")
            if colorHand[1] == "red" and red < int(colorHand[0]):
                    gamePossible = False
            if colorHand[1] == "blue" and blue < int(colorHand[0]):
                    gamePossible = False
            if colorHand[1] == "green" and green < int(colorHand[0]):
                    gamePossible = False
            pass
    if gamePossible:
        sum += int(gameNr)
    pass

print(sum)