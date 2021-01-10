string = input()

result = ""
for i in range(len(string)):
    
    if ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z'):
        num = ord(string[i]) - ord('a')
        num = (num + 13) % 26
        result += chr(num + ord('a'))
    elif ord(string[i]) >= ord('A') and ord(string[i]) <= ord('Z'):
        num = ord(string[i]) - ord('A')
        num = (num + 13) % 26
        result += chr(num + ord('A'))
    else:
        result += string[i]
        
print("%s" % result)