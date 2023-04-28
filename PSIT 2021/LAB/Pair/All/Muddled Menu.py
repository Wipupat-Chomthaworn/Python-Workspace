"""main"""
def main():
    """main"""
    list1 = list()
    while True:
        var = input()
        if var == 'DONE':
            break
        elif "Can't do:" in var:
            list1.remove(var[10:])
        elif "CLOSED" in var:
            break
        elif var == "SOMETHING'S WRONG":
            list1.clear()
        else:
            if var[-1] == "N":
                list1.append(var[:-3])
            else:
                # if int(var[var.find("#")+1:])-1 > 9:
                #     list1.insert((int(var[-1])-1), var[:-3])
                list1.insert(int(var[var.find("#")+1:])-1, var[0:var.find('#')-1])
                # list1.insert((int(var[-1])-1), var[:-3])
        # print(list1)

    # ans = list1
    # rev = reversed(list1)
    # print(ansset)
    if var == "CLOSED":
        print('Full Course: [] Reversed: []')
    else:
        print("Full Course:", end=' ')
        print(list1, end=' ')
        list1.reverse()
        print("Reversed:", end=' ')
        print(list1)
main()
