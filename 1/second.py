file1 = open('_input.txt', 'r')
Lines = file1.readlines()

def checkSubstringIsNumber(line, i):
    if line.find("one", i, i+len("one")) >= 0:
        return 1
    if line.find("two", i, i+len("two")) >= 0:
        return 2
    if line.find("three", i, i+len("three")) >= 0:
        return 3
    if line.find("four", i, i+len("four")) >= 0:
        return 4
    if line.find("five", i, i+len("five")) >= 0:
        return 5
    if line.find("six", i, i+len("six")) >= 0:
        return 6
    if line.find("seven", i, i+len("seven")) >= 0:
        return 7
    if line.find("eight", i, i+len("eight")) >= 0:
        return 8
    if line.find("nine", i, i+len("nine")) >= 0:
        return 9
    return 0

sum = 0
for line in Lines:
    cur_char = 0
    # print(line)
    for i in range(0, len(line)):
        chnum = checkSubstringIsNumber(line, i)
        if chnum > 0:
            cur_char += chnum * 10
            break
        if line[i].isnumeric():
            cur_char += int(line[i]) * 10
            break

    for i in reversed(range(0, len(line))):
        chnum = checkSubstringIsNumber(line, i)
        if chnum > 0:
            cur_char += chnum
            break
        if line[i].isnumeric():
            cur_char += int(line[i])
            break
    sum += int(cur_char)

print(sum)