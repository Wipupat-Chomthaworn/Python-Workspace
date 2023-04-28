"""Ecid dist"""
def main():
    """main"""
    list1 = []
    for _ in range(int(input())):
        var = list(map(int, input().split()))
        print(var)
        print(list1)
        list1.append(zip(var[0], var[1]))

    # for i in range(2):
    #     dis = ((var[]))**0.5

main()
