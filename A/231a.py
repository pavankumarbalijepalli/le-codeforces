n = int(input())
count = 0
for i in range(n):
    p, v, t = [int(val) for val in input().split(' ')]
    if (p + v + t) >= 2:
        count += 1

print(count)