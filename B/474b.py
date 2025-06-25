n = int(input())
worms = [int(i) for i in input().split(' ')]
k = int(input())
juicy_worms = [int(i) for i in input().split(' ')]

sum_worms = [worms[0]]
for i in range(1, len(worms)):
    sum_worms.append(worms[i] + sum_worms[i-1])
sum_worms.insert(0, -1)

for j in range(len(juicy_worms)):
    left = 0
    right = len(sum_worms)
    mid = (left + right)//2
    
    def bin_search(left, mid, right):
        if juicy_worms[j] <= sum_worms[mid]:
            if juicy_worms[j] > sum_worms[mid-1]:
                print(mid)
                return
            else:
                right = mid
                mid = (left + right)//2
                bin_search(left, mid, right)
        elif juicy_worms[j] > sum_worms[mid]:
            left = mid
            mid = (left+right)//2
            bin_search(left, mid, right)
        return
        
    bin_search(left, mid, right)