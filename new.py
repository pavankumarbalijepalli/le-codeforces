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

nums = [3,2,3]
counter = {}
for num in nums:
    if counter.get(num):
        counter[num] += 1
        if counter[num] > len(nums)//2:
            print(num)
    else:
        counter[num] = 1
                


