"""main"""
def main():
    """main"""
    string = input().lower()
    dict1 = {}
    for i in string:
        if i.isalpha():
            var = string.count(i)
            dict1[i] = var
    vald = list(dict1.values())
    list1 = sorted(vald)[-1]
    keyd = list(dict1.keys())
    most = vald.index(list1)
    print(keyd[most])
main()
