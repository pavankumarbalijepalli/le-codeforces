n = int(input())
_sum = [0, 0, 0]
for i in range(n):
    _in = [int(x) for x in input().split(' ')]
    _sum[0] += _in[0]
    _sum[1] += _in[1]
    _sum[2] += _in[2]

print('YES' if (_sum[0]==0 and _sum[1]==0 and _sum[2]==0) else 'NO')
