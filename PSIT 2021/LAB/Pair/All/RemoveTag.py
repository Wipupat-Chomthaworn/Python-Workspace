"""RemoveTag"""
def strstip(anslist, word):
    """Remove space for i in word"""
    if word.strip() != "":
        anslist.append(word)
def main():
    """main"""
    var = input()
    var = var.replace(">", ">dummy").replace("<", "dummy<")
    var = var.split("dummy")
    anslist = []
    for i in var:
        if (i.find("<") == -1) or i.find(">") == -1:
            if i.strip() != "":
                if i.find(" ") != -1:
                    for j in i.split(" "):
                        strstip(anslist, j)
                else:
                    anslist.append(i)
    print(anslist)
main()
