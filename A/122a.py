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

lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
n = int(input())
result = 'NO'
if n in lucky:
    result = 'YES'
else:
    for val in lucky:
        if n%val==0:
            result = 'YES'
            break
        else:
            result = 'NO'
print(result)


