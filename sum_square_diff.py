tests = int(input())
for case in range(tests):
    n = int(input())
    print(int((n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6))