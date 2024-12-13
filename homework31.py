n = int(input())
sum = 0
if n <= 100:
    for n in range(1, n+1):
        sum = (n**3)+sum
    print(sum)
else:
    print('иди сам считай')