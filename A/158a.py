n, k = [int(x) for x in input().split(' ')]
stack = [int(x) for x in input().split(' ')]
result = len([i for i in stack if i>=stack[k-1] and i>=1])
print(result)
             