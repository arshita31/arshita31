# all elements will be divisible only when all elements of the list are same 
t = int(input())

for case in range(t):
    l = int(input())
    s = input().split()
    arr = []
    for i in s:
        arr.append(int(i))
    ele = arr[0]
    flag = 1
    for i in arr:
        if ele != i:
            print("NO")
            flag =  0
            break

    if (flag):
        print("YES")