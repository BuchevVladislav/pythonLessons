def print_dir(dir):
    import os
    s = list(os.listdir(dir))
    for i in os.walk(dir):
        print(i)
print_dir(r"C:/MyCode")