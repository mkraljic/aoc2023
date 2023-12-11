
file = open('11/_input.txt', 'r').read().strip()
Lines = file.split('\n')
old = 1000000

def findPairSteps(i, j):
    sumPairs = 0
    for x in range(j+1, len(Lines[0])):
        if Lines[i][x] == '#':
            sumPair = x-j
            for emptyPlot in Lines[i][min(x,j):max(x,j)]:
                if emptyPlot == '*':
                    sumPair += old - 1
            sumPairs += sumPair
    
    distanceSum = 0
    for y in range(i+1, len(Lines)):
        if all(c == '*' for c in Lines[y]):
            distanceSum += old - 1

        for x in range(0, len(Lines[0])):
            if Lines[y][x] == '#':
                sumPair = abs(x-j) + abs(y-i) + distanceSum
                for emptyPlot in Lines[y][min(x,j):max(x,j)]:
                    if emptyPlot == '*':
                        sumPair += old - 1

                sumPairs += sumPair
    return sumPairs

for i in reversed(range(len(Lines))):
    if all(c=='.' for c in Lines[i]):
        Lines.pop(i)
        Lines.insert(i, "*" * len(Lines[i]))

for i in reversed(range(len(Lines[0]))):
    col = ""
    for line in Lines:
        col += line[i]
    if all(c in ['.','*'] for c in col):
        for x in range(len(Lines)):
            Lines[x] = Lines[x][:i]+('*')+Lines[x][i+1:]

# for line in Lines:
#     print(line)

sum = 0
for i in range(len(Lines)):
    for j in range(len(Lines[0])):
        if Lines[i][j] == '#':
            sum += findPairSteps(i,j)
# sum += old-1
print(sum)