n = int(input())
_list = []
for i in range(n):
    i = input()
    _list.append(i)

for string in _list:
    if len(string)>10:
        print(string[0] + str(len(string)-2) + string[-1])
    else:
        print(string)