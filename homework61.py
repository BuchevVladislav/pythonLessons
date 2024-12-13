m = [ [1, 2, 3], [1, 4, 3], [10, 2, 3], [11, 2, 3], ]
mx = 0
for i in range(len(m)):
    s = 0
    for j in range(len(m[0])):
        s += m[i][j]
        mx = max(s, mx)
print(mx)