name = input("введите название файла \n")
f = open(f"Lesson7/{name}.txt", "w+", encoding="utf-8")
print("введите строку для записи, enter для перехода на следующую строку, 1 для закрытия")
while True:
    s = input()
    if s == "1":
        f.close()
        break
    f.write(s + "\n")