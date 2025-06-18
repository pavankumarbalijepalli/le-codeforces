input_string = input()
out= ''
for i in input_string:
    if i.upper() in ["A", "O", "Y", "E", "U", "I"]:
        out += ''
    else:
        out += '.'
        out += i.lower()
print(out)