mass = str(input().split())
for i in range(len(mass), 0, -1):
    print(', '.join(mass[i-1]))