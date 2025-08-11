# t = int(input())
# 
# for i in range(t):
#     n, m = [int(i) for i in input().split(' ')]
#     matrix = []
#     for _ in range(n):
#         row = [int(i) for i in input().split(' ')]
#         matrix.append(row)
#     result = []
#     
#     row_sum = [sum(row) for row in matrix]
#     col_sum = [sum(col) for col in zip(*matrix)]
#     print(row_sum, col_sum)
#     print('----')    
# 
# ----------------

s = input()
target = 'hello'

while s and target:
    if s[0] == target[0]:
        target = target[1:]
    s = s[1:]

print('YES' if target=='' else 'NO')


