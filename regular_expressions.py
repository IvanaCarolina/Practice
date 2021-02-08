import re


pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search inside of this text please!'

a = pattern.search(string)

print(a.group(2))