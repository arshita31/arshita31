temp = input().split()

n = int(temp[0])
x = int(temp[1])
y = int(temp[2])

s = input()
al = 0
bo = 0 
flag = 0 

for i in s:
    if i == "A":
        if flag:
            bo += x + y
            flag = 0
        else:
            al += x
    
    elif i == "B":
        if flag:
            bo += 2*y
            flag = 0
        else:
            flag = 1
            
print(al,bo)
            
            