num = input("<<< ")
string = ""
for i in num:
    if i == '6':
        string += '9'
    elif i == '9': 
        string += '6'
    elif i == '0':
        string += '0'
if num == string[::-1]:
    print(True)
else:
    print(False)  