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

n, m, a = [int(x) for x in input().split(' ')]
row, column = 0, 0
if n<=a:
    row += 1
else:
    if n%a == 0:
        row += n//a
    else:
        row += n//a + 1

if m<=a:
    column += 1
else:
    if m%a == 0:
        column += m//a
    else:
        column += m//a + 1
print(row*column)



