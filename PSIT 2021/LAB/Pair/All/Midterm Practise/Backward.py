"""main"""
def main():
    """main"""
    list1 = []
    while True:
        var = input()
        list1.append(var)
        if var == 'NULL':
            list1.pop()
            break
    # print("+++++")
    list1.reverse()
    for i in list1:
        print(i)
main()
