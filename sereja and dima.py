n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
a = 0
b = 0
turn = 0

while left <= right:
    if cards[left] > cards[right]:
        value = cards[left]
        left += 1
    else:
        value = cards[right]
        right -= 1

    if turn == 0:
        a += value
    else:
        b += value

    turn = 1 - turn

print(a, b)
