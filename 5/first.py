
file1 = open('_input.txt', 'r')
Lines = file1.readlines()

seeds = []
locations = []
newLocations = []

nextMap = False
for line in Lines:
    lineValues = line.strip().split(":")
    # print (lineValues)
    if lineValues[0] == "seeds":
        seeds = list(map(int, lineValues[1].split()))
        locations = list(map(int, lineValues[1].split()))
        newLocations= list(map(int, lineValues[1].split()))
        # print (seeds)
    else:
        if len(lineValues) > 1:
            locations = newLocations.copy()
        else:
            nextMap = False
            directions = list(map(int, lineValues[0].split())) 
            if len(directions) > 1:
                for i in locations:
                    if i in range(directions[1], directions[1]+directions[2]):
                        index = locations.index(i)
                        # print(i-directions[1],newLocations)  
                        newLocations[index] = directions[0] + i - directions[1]
    pass

print("min",min(newLocations),newLocations)