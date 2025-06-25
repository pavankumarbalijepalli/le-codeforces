s1 = sorted([ord(i) for i in input().lower()])
s2 = sorted([ord(i) for i in input().lower()])
print(s1, s2)
count = 0

for i in range(len(s1)):
    if s1[i] > s2[i]:
        count += 1
    elif s1[i] < s2[i]:
        count -= 1
    else:
        count += 0

if count > 0:
    print(1)
elif count < 0:
    print(-1)
else:
    print(0)