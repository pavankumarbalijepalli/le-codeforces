n, l = [int(i) for i in input().split(' ')]
lights = sorted([int(i) for i in input().split(' ')])

res = []

if lights[0] != 0:
    res.append(lights[0])
    
if lights[-1] != n:
    res.append(l - lights[-1])
    
for i in range(n-1):
    res.append((lights[i+1] - lights[i])/2)


print(max(res))
