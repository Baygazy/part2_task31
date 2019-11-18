with open("task31.txt", "r") as file_:
    s = file_.read().split()
    print("Слов: ", len(s))
    together = ""
    for i in s:
        together += i
    print("Букв: ", len(together))
    print(s)


