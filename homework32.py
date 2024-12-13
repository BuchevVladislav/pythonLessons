print('Ща будет магия!')
num = int(input('Скок надо? '))
tab = []
for a in range(1, num+1):
    for b in range(1,num+1):
        if a*b < 10:
            tab.append(str(a*b)+' ')
        else:
            tab.append(str(a*b))
        if b == num:
            tab.append('\n')
print('', ' '.join(tab))