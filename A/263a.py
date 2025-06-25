x, y = 0, 0

for i in range(5):
    _in = input().split(' ')
    for j in range(len(_in)):
        if _in[j] == '1':
            x, y = i, j
        
print(abs(x-2) + abs(y-2))