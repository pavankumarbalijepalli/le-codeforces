t = int(input())

result = []
for i in range(t):
    n, j, k = [int(x) for x in input().split(' ')]
    players = [int(x) for x in input().split(' ')]
    player = players[j-1]
    # print(set(players))
    if player in list(set(players))[-k:]:
        result.append('YES')
    else:
        result.append('NO')

for res in result:
    print(res)
