import sys

L = []
for arg in sys.argv[1:] :
    L.append(int(arg))
#print(L)    
min = 0
max = 0
cycle = []

while cycle.count(False) < (len(L)-1) :
    cycle = []
    for i in range(len(L)-1):
        if L[i] < L[i+1] :
            min = L[i]
            max = L[i+1]
            L[i] = max
            L[i+1] = min
        else :
            cycle.append(False)
print(L)
