import re


pattern = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
string = 'carollolivei7'

a = pattern.search(string)
print(a)