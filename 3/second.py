
file1 = open('_input.txt')
Lines = file1.readlines()
lineLength = len(Lines[0])

def findNumber(i, j, numbers):
    while j > 0 and Lines[i][j-1].isnumeric():
        j -= 1
    k = j
    ch = Lines[i][k]
    while Lines[i][k+1].isnumeric():
        k+=1
        ch += Lines[i][k]
    existingNr = False
    for num in numbers:
        if num[0] == int(ch) and num[1] == i and num[2] == j:
            existingNr = True
    if existingNr == False:
        numbers.append(list([int(ch), i, j, k]))
    return

def findAdjacentNumbers(lineNr, LineCol):
    numbers = []
    start = LineCol
    if LineCol > 0:
        start = LineCol - 1
    end = LineCol + 1
    if LineCol >= lineLength:
        end = LineCol

    if lineNr > 0:
        for i in range(start, end+1):
            ch = Lines[lineNr-1][i]
            if ch.isnumeric():
                findNumber(lineNr-1, i, numbers)

    if lineNr < len(Lines):
        for i in range(start, end+1):
            ch = Lines[lineNr+1][i]
            if ch.isnumeric():
                findNumber(lineNr+1, i, numbers)
    ch = Lines[lineNr][start]
    if ch.isnumeric():
        findNumber(lineNr, start, numbers)
    ch = Lines[lineNr][end]
    if ch.isnumeric():
        findNumber(lineNr, end, numbers)
    return numbers

sum = 0
for i in range(0,len(Lines)):
    print (Lines[i].strip())
    for j in range(0, len(Lines[i])):
        if Lines[i][j] == "*":
            lisOfNumbers = findAdjacentNumbers(i, j)
            if len(lisOfNumbers) == 2:
                sum += lisOfNumbers[0][0]*lisOfNumbers[1][0]

print(sum)