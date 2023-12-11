
file1 = open('8/_input.txt', 'r')
Lines = file1.readlines()

nextStep = "AAA"
lastStep = "ZZZ"
steps = Lines[0].strip()
map = {}
for i in range(2, len(Lines)):
    line = Lines[i].strip()
    pos = line.split(" = ")    
    map[pos[0]]=pos[1][1:-1].split(", ")

count = 0
atDestination = False
while atDestination == False:
    
    for lr in steps:
        count += 1
        if lr == 'L':
            nextStep = map[nextStep][0]
        else:
            nextStep = map[nextStep][1]
        if nextStep == lastStep:
            atDestination = True
            break
    
    print("Step",count)
    
print("Final",count)