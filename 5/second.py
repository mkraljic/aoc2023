
file1 = open('5/_input.txt', 'r')
Lines = file1.readlines()

locations = []
newLocations = []

for line in Lines:
    lineValues = line.strip().split(":")
    # print (lineValues)
    if lineValues[0] == "seeds":
        seedList = list(map(int, lineValues[1].split()))
        j = 0
        while j < len(seedList):
            startSeed = seedList[j]
            seedSize = seedList[j+1]
            seeds = []
            seeds.append(startSeed)
            seeds.append(startSeed + seedSize)
            locations.append(seeds)
            j += 2
            pass
        # newLocations = locations.copy()
        print (newLocations)
    else:
        if len(lineValues) > 1:
            for i in locations:
                if i[0] >= 0:
                    newLocations.append(i)
            locations.clear()
            locations = newLocations.copy()
            newLocations.clear()
        else:
            directions = list(map(int, lineValues[0].split())) 
            if len(directions) > 1:
                # print(locations)
                for i in locations:
                    if i[0] in range(directions[1], directions[1]+directions[2]):
                        # print ("1",i,directions)
                        if directions[1]+directions[2] >= i[1]: 
                            # print ("1.1") # kompletni
                            newStartLocation = directions[0] + i[0] - directions[1]
                            newEndLocation = directions[0] + i[1] - directions[1]
                            local = []
                            local.append(newStartLocation)
                            local.append(newEndLocation)
                            newLocations.append(local)
                            i[0] = -1
                            i[1] = -1
                            continue
                        else:
                            # print ("1.2") # right overflow
                            newStartLocation = directions[0] + i[0] - directions[1]
                            newEndLocation = directions[0] + directions[2]
                            local = []
                            local.append(newStartLocation)
                            local.append(newEndLocation)
                            newLocations.append(local)
                            i[0] = directions[1] + directions[2] + 1 

                    if i[1] in range(directions[1], directions[1]+directions[2]):
                        # print ("2",i)
                        if True:
                        # print ("2.1") #left overflow
                            newStartLocation = directions[0]
                            newEndLocation = directions[0] + i[1] - directions[1]
                            local = []
                            local.append(newStartLocation)
                            local.append(newEndLocation)
                            newLocations.append(local)
                            i[1] = directions[1] - 1

                    if directions[1] in range(i[0], i[1]):
                        # print ("3",i)
                        if directions[1]+directions[2] < i[1]: 
                            # print ("3.1") # kompletni
                            newStartLocation = directions[0]
                            newEndLocation = directions[0] + directions[2]
                            local = []
                            local.append(newStartLocation)
                            local.append(newEndLocation)
                            newLocations.append(local)

                            # add overflows
                            lOverflow = []
                            lOverflow.append(i[0])
                            lOverflow.append(directions[1]-1)
                            locations.append(lOverflow)

                            rOverflow = []
                            rOverflow.append(directions[1]+directions[2]+1)
                            rOverflow.append(i[1])
                            locations.append(rOverflow)

                            i[0] = -1
                            i[1] = -1
                            continue
                        else:
                            print ("3.2") # right overflow
                            newStartLocation = directions[0] 
                            newEndLocation = directions[0] + i[1]-i[0]
                            local = []
                            local.append(newStartLocation)
                            local.append(newEndLocation)
                            newLocations.append(local)
                            i[0] = directions[1] + directions[2] + 1 
                        
                    if directions[1]+directions[2] in range(i[0], i[1]):
                        print ("4",i)
                        pass
                    
                pass
            # change location
            # print(locations, newLocations)

for i in locations:
    if i[0] >= 0:
        newLocations.append(i)

print("min",min(newLocations),newLocations)