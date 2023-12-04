
file1 = open('_input.txt', 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    red = 0
    green = 0
    blue = 0
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
            if colorHand[1] == "red":
                red = max(int(colorHand[0]), red)
            if colorHand[1] == "blue":
                blue = max(int(colorHand[0]), blue)
            if colorHand[1] == "green":
                green = max(int(colorHand[0]), green)
            pass
    pow = red * green * blue
    print(pow)
    sum += pow
    pass

print(sum)