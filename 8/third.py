
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
allSteps = []
while atDestination == False:
    
    for lr in steps:
        count += 1
        step = nextStep[5]
        # for step in nextStep:
        if lr == 'L':
            allSteps.append(map[step][0])
            nextStep[5] = map[step][0]
        else:
            allSteps.append(map[step][1])
            nextStep[5] = map[step][1]
        if allSteps[len(allSteps)-1][2] == "Z":
            #compare steps
            print(count,step)
            if allSteps[:0-int(len(allSteps)/2)] == allSteps[int(len(allSteps)/2):]:
                print("found stepCount",int(len(allSteps)/2))
            elif allSteps[:0-int(len(allSteps)/2)-1] == allSteps[int(len(allSteps)/2)+1:]:
                print("found stepCount",int(len(allSteps)/2))
            
        
        
        
    
    
print("Final",count)