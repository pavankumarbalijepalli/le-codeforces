t = int(input())

result = []

for i in range(t):
    n = int(input())
    string = input()
    l, r = string[0], string[-1]
    string = string[1:-1]
    if (l in string) or (r in string) or (len(list(string)) != len(set(string))):
        result.append('Yes')
        continue
    else:
        result.append('No')
        continue

for i in result:
    print(i)
        
