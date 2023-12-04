
file1 = open('_input.txt')
Lines = file1.readlines()

def findNumber(line, i):
    num = ""
    for j in range(i, len(line)):
        if line[j].isnumeric():
            num += line[j]
        else:
            if num != "":
                return map(int, [int(num), i, j-1])
            else:
                return map(int, [-1, -1, -1])
    return map(int, [-1, -1, -1])

def findAdjacentSymbol(lineNr, start, end):
    if lineNr > 0:
        for i in range(start, end+1):
            ch = Lines[lineNr-1][i]
            if ch != "." and ch.isnumeric() == False and ch!="\n":
                return True
    if lineNr < len(Lines) - 1:
        for i in range(start, end+1):
            ch = Lines[lineNr+1][i]
            if ch != "." and ch.isnumeric() == False and ch!="\n":
                return True
    ch = Lines[lineNr][start]
    if ch != "." and ch.isnumeric() == False and ch!="\n":
        return True
    ch = Lines[lineNr][end]
    if ch != "." and ch.isnumeric() == False and ch!="\n":
        return True
    return False

sum = 0
for i in range(0,len(Lines)):
    print (Lines[i].strip())
    j = 0
    while j < len(Lines[i]):
        num, start, end = findNumber(Lines[i], j)
        if num > 0:
            j = end
            # print(num,start,end)
            if start > 0:
                start -= 1
            if end < len(Lines[i]):
                end += 1
            if findAdjacentSymbol(i, start, end):
                sum += num
        j += 1
        pass
    pass

print(sum)