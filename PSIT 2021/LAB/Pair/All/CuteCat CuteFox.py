"""main"""
def main():
    """main"""
    # import json
    cat = {"Cat01" : "Garfield"}
    fox = {"Fox01" : "Fubuki"}
    for i in range(int(input())):

        var = input()
        # print(var[1:var.find(":")].strip() in list(fox.keys()))
        foxkey = list(fox.keys())
        foxvar = list(fox.values())
        catkey = list(cat.keys())
        catvar = list(cat.values())
        # print(foxvar.index(var[1:var.find(":")].strip()))
        # print(foxkey[foxvar.index(var[1:var.find(":")].strip())])
        var2 = var[1:var.find(":")].strip().replace("\"", "").replace("\'", "")
        var3 = var[var.find(":")+1:-1].strip().replace("\"", "")
        # print(catkey[catvar.index(var2)])
        if var.find('Cat') != -1:
            if var2 in foxvar:
                fox.pop(foxkey[foxvar.index(var2)])
            elif var2 in catvar:
                cat.pop(catkey[catvar.index(var2)])
            # elif var3 in foxkey:
            #     fox.pop(foxvar[foxkey.index(var2)])
            # elif var3 in catvar:
            #     cat.pop(catkey[catkey.index(var2)])
            cat[var[var.find(":")+1:-1].strip().replace("\"", "")] = var2
        elif var.find('Fox') != -1:
            if var2 in foxvar:
                fox.pop(foxkey[foxvar.index(var2)])
            elif var2 in catvar:
                cat.pop(catkey[catvar.index(var2)])
            # elif var3 in foxkey:
            #     fox.pop(foxvar[foxkey.index(var2)])
            # elif var3 in catvar:
            #     cat.pop(catkey[catkey.index(var2)])
            fox[var[var.find(":")+1:-1].strip().replace("\"", "")] = var2
        # print(cat)
    # print(cat, list(cat.values()))
    print('Cat : %d'%len(list(cat.values())))
    print('Fox : %d'%len(list(fox.values())))
    for i in sorted(cat.keys()):
        print('%s : %s'%(cat[i], i))
    for i in sorted(fox.keys()):
        print('%s : %s'%(fox[i], i))

main()
