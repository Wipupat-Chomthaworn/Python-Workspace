"""main"""
def main():
    """main"""
    num = int(input())
    list1 = []
    # list1.append(num)
    check = []
    while True:
        text = int(input())
        if text == 0:
            break
        else:
            list1.append(text)
    for i in range(1, num+1):
        check.append(i)
    # print(list1)
    # print(check)
    ans = sorted(list(set(list1).symmetric_difference(set(check))))
    # print(ans)
    for j in ans:
        print(j)

main()
