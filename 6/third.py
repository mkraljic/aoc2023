file1 = open('6/_input.txt', 'r')
Lines = file1.readlines()

pow = 1

time = int(Lines[0].strip().replace(" ",""))
distance = int(Lines[1].strip().replace(" ",""))

print(time,distance)

testTime = time
minTime = 0
maxTime = time
count =0

found = False
while not found:
    count +=1
    testDistance = minTime*(time-minTime)
    testTime = testTime//2
    if testDistance == distance:
        found = True
    elif testDistance > distance:
        if testTime == 0:
            found = True
            minTime-=1
        minTime -= testTime
    else:
        if testTime == 0:
            found = True
            minTime+=1
        minTime += testTime


testTime = time
found = False
while not found:
    count +=1
    testDistance = maxTime*(time-maxTime)
    testTime = testTime//2
    if testDistance == distance:
        found = True
    elif testDistance > distance:
        if testTime == 0:
            found = True
            maxTime+=1
        maxTime += testTime
    else:
        if testTime == 0:
            found = True
            maxTime-=1
        maxTime -= testTime


print("records",maxTime - minTime + 1," in ",count," tries")