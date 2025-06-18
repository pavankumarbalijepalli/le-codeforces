n = int(input())
stack = []
for i in range(n):
    stack.append(str(input()))

count = 0
for operation in stack:
    if  '++' in operation:
        count += 1
    else:
        count -= 1

print(count)