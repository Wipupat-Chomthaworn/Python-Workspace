"""Row row your boat"""
def main(numm, weight, bbbb):
    """put n print"""
    list1 = weight.split(" ")
    list1 = [int(i)for i in list1]
    list1.sort()
    for _ in range(numm - 1):
        mylist2 = []
        for i in range(len(list1) - 1):
            final = int(list1[i+1]) - int(list1[i])
            mylist2.append(final)
        maxmin = min(mylist2)
        aaaa = mylist2.index(maxmin)
        list1.pop(aaaa)
        list1.pop(aaaa)
        bbbb.append(maxmin)
    ans = sum(bbbb)
    print(ans)

main(int(input()), input(), [])
