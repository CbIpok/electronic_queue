import re

def push (l,el):
    l.append(el)

def pop(l):
    el = l[0]
    del l[0]
    return el

# print(re.sub(r'[0-9][0-9][0-9][0-9]\s[a-zA-Z0-9][a-zA-Z0-9]\s[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9][0-9][0-9]\s[0-9][0-9]\r','0002 C1 01:13:02.877 00\r'))

matches = re.findall(r'[0-9]',"12345 6789")

for match in matches:
    print(match)