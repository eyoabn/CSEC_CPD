x = list(map(int,input().split()))
a=x[0]
b= x[1]
years=0
while a <= b:
    a = a * 3
    b = b * 2
    years += 1
print(years)
