x =int(input())
y =input()
a=1
for i in range(x-1):
    z=input()
    if y != z:
        a += 1
    y = z
print(a)
    
