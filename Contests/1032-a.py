t = int(input())

result = []
for i in range(t):
    n, pos = [int(i) for i in input().split(' ')]
    axis = [int(i) for i in input().split(' ')]
    l, r = axis[0], axis[-1]
    if l <= pos <= r:
        if pos-l <= r-pos:
            result.append(pos-l + r-l)
        else:
            result.append(r-pos + r-l)
    if pos < l:
        result.append(r-pos)
    if pos > r:
        result.append(pos-l)

for i in result:
    print(i)