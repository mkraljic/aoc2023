file1 = open('_input.txt', 'r')
Lines = file1.readlines()

pow = 1

times = Lines[0].strip().replace(" ","").split()
distances = Lines[1].strip().replace(" ","").split()

print(times,distances)
for i in range(0, len(times)):
    print(times[i])
    time = int(times[i])
    records = 0
    for j in range(0, time):
        distance = j*(time-j)
        if distance > int(distances[i]):
            records += 1

    print(records)
    pow *= records
print("pow",pow)