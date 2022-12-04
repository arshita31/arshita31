i = int(input())
s = input().split()
std = list(range(1,i+1))
l = []
for x in s:
    l.append(int(x))

for j in std:
    if j not in l:
        print(j)
    
