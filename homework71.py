def read_last(lines, file):
   f = open(file, encoding='utf-8').readlines()
   for i in range(1, lines + 1):
       i = -1 * i
       print(f[i])
read_last(3, "Lesson7/article.txt")