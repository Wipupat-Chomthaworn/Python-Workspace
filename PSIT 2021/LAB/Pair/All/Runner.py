"""Runner"""
def main():
    """main"""
    num = int(input())
    num2 = int(input())
    list1 = []
    lsttest = "fir"
    for i in range(1, num2 + 1):
        list1.append(str(str(i) + " " + str(input())).split(" "))
    for i in list1:
        if lsttest == 'fir':
            lsttest = i
        else:
            first = (num - int(i[2])) / int(i[1])
            lff = (num - int(lsttest[2])) / int(lsttest[1])
            if first <= lff:
                if first == lff and i[1] > lsttest[1]:
                    lsttest = i
                if first != lff:
                    lsttest = i
    print(lsttest[0])
main()
