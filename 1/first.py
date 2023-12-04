file1 = open('_input.txt', 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    cur_char = ""
    for ch in range(0, len(line)):
        if line[ch].isnumeric():
            cur_char += line[ch]
            break

    for ch in reversed(range(0, len(line))):
        if line[ch].isnumeric():
            cur_char += line[ch]
            break
    sum += int(cur_char)

print(sum)