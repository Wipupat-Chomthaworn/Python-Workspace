"""main"""
def main():
    """main"""
    list1 = []
    for i in range(int(input())):
        list1.append(input())
    list1.sort(key=len)
    for i in list1:
        print(i)
main()
