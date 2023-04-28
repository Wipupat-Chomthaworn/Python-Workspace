"""main"""
def main():
    """main"""
    list1 = list()
    while True:
        var = input()
        if var == 'END':
            break
        elif var == "IT'S A DOG":
            list1.pop()
        else:
            list1.extend(var.split(', '))

    ans = sorted(list1)
    ansset = sorted(list(set(ans)))
    # print(ansset)
    for i in ansset:
        where = list1.index(i)
        print(ans[ans.index(i)], \
            where+1, ans.count(i))
main()
