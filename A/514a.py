val = ''
for i in input():
    if int(i) < 5:
        val += i
    else:
        if not val and i == '9':
            val += i
        else:
            val += str(9-int(i))
print(val)
