import re
s = input("введите строку \n")
m = re.findall(r"(([0-2]\d)(:[0-5][0-9]){1,2})", s)
if m != None: 
    for i in m:
      s = s.replace(i[0], "(TDS)", 1)
print(s)