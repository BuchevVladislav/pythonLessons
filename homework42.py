s = "slidufasdjdf;(a;sdiofjlksdjf;lksjdfaoidfsaklf)alsdkjfisdufeejlsd;jfa;fa"
flag = False
for i in s:
    if i == ")": flag = False
    if flag: print(i, end="")
    if i == "(": flag = True