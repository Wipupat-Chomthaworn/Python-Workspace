"""main"""
def main():
    """main"""
    list1 = []
    for _ in range(int(input())):
        list1.append(int(input()))
    list1.sort()
    # print(list1)
    if len(list1) %2 == 0:
        # print(list1[len(list1)//2])
        ans = (list1[len(list1)//2-1]+list1[(len(list1)//2)])/2
    else:
        ans = (list1[len(list1)//2])
    print('%.1f'%(ans))
main()
