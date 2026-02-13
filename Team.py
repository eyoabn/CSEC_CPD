x =int(input())
p=0
for i in range(x):
    y = list(map(int,input().split()))
    n=y[0]+y[1]+y[2]
    if n >= 2:
        p += 1
print(p)
