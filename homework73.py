def longest_words(file):
    f = open(file, encoding="utf-8").readlines()
    mx = 0
    slova = []
    for i in f:
        i = i.split()
        for j in i:
            mx = max(mx, len(j))
    for i in f:
        i = i.split()
        for j in i:
            if len(j) == mx:
                slova.append(j)
    print(mx, slova)
longest_words("Lesson7/article.txt")