
file1 = open('8/_input.txt', 'r')
Lines = file1.readlines()

nextStep = []
lastStep = []
steps = Lines[0].strip()
map = {}
for i in range(2, len(Lines)):
    line = Lines[i].strip()
    pos = line.split(" = ")    
    map[pos[0]]=pos[1][1:-1].split(", ")
    if pos[0][2] == "A":
        nextStep.append(pos[0])
    elif pos[0][2] == "Z":
        lastStep.append(pos[0])

count = 0
atDestination = False
while atDestination == False:
    
    for lr in steps:
        interStep = []
        count += 1
        isLastStep = True
        multipleEnds = 0
        for step in nextStep:
            if lr == 'L':
                interStep.append(map[step][0])
            else:
                interStep.append(map[step][1])
            if interStep[len(interStep)-1][2] != "Z":
                isLastStep = False
            else:
                multipleEnds += 1
        
        if multipleEnds > 2:
            print("Zss",multipleEnds,"on step",count,interStep)
        
        nextStep = interStep.copy()
        if isLastStep:
            atDestination = True
            break
    
    
print("Final",count)