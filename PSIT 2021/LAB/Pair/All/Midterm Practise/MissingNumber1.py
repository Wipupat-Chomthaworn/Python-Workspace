"""main"""
def main():
    """main"""
    list1 = []
    num = int(input())
    check = []
    for i in range(1, num+1):
        list1.append(int(input()))
    for i in range(num, 0, -1):
        check.append(i)
    # print(check)
    ans = sorted(list(set(check).difference(set(list1))))
    # print(ans)
    for i in ans:
        print(i)
main()
