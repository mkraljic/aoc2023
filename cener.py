N = int(input())
zbroj = 0
for i in range(1, N):
    minuta, sekunda = map(int, input().split())
    zbroj += minuta*60 + sekunda

ukupnoM, ukupnoS = map(int, input().split())
ukupno = ukupnoM*60 +ukupnoS

preostalo = ukupno - zbroj

print(preostalo//60,preostalo%60)