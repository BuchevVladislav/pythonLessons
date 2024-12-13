def isSimple(a):
    for i in range(2, a):
        if a % 2 == 0:
            return False
            break
    return True
def reverse(a):
    b = ""
    for i in range(len(a) - 1, -1, -1):
        b += a[i]
    return b
n = int(input("Введите верхнюю границу \n"))
for i in range(n + 1):
    if isSimple(i):
        b = bin(i)[2:]
        if b == reverse(b):
            print(i)