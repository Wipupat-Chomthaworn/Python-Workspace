'''[Recommend] Run Length Encoding'''
def main():
    '''main func'''
    var = input()
    keep = 0
    first = ""
    for i in var:
        if first != i:
            if first != "":
                print("%d%s" %(keep, first), end="")
            first = i
            keep = 1
        else:
            keep += 1
    print("%d%s" %(keep, first), end="")
main()
