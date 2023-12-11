
file = open('11/_input.txt', 'r').read().strip()
Lines = file.split('\n')

def findPairSteps(i, j):
    sumPairs = 0
    for x in range(j+1, len(Lines[0])):
        if Lines[i][x] == '#':
            sumPairs += x-j
    
    for y in range(i+1, len(Lines)):
        for x in range(0, len(Lines[0])):
            if Lines[y][x] == '#':
                sumPairs += abs(x-j) + abs(y-i)
    return sumPairs

for i in reversed(range(len(Lines))):
    if all(c=='.' for c in Lines[i]):
        Lines.insert(i, "." * len(Lines[i]))

for i in reversed(range(len(Lines[0]))):
    col = ""
    for line in Lines:
        col += line[i]
    if all(c=='.' for c in col):
        for x in range(len(Lines)):
            Lines[x] = Lines[x][:i]+'.'+Lines[x][i:]

sum = 0
for i in range(len(Lines)):
    for j in range(len(Lines[0])):
        if Lines[i][j] == '#':
            sum += findPairSteps(i,j)

print(sum)