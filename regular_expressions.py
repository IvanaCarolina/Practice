#email checker
import re


pattern = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
string = 'carollolivei7@gmail.com'
password = re.compile(r"[A-Za-z0-9$%#@]{7,}[0-9]")
string2 = 'Ivana$@1788'

a = pattern.search(string)
check = password.fullmatch(string2)

print(a)
print(check)

#[A-Za-z0-9$%#@]{7,}[0-9]\d
#string2 = 'Ivana$@1788Carol2991'
#[A-Za-z0-9$%#@]{7,}[0-9]