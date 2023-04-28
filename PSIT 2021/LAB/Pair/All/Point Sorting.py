"""Point Sorting"""
def main():
    """main"""
    test = int(input())
    list1 = []
    for _ in range(test):
        for _ in range(int(input())):
            list1.append(input().split())
        # list1.sort()
        list1.sort(key=lambda x: x[1], reverse=True)
        # list1.reverse()
        list1.sort(key=lambda x: int(x[0])+int(x[1]))
        for j in list1:
            print(*j)
            # print('==%s'%j)
        list1 = []
main()
# """Point Sorting"""
# def plus(score):
#     """Point Sorting"""
#     return int(score[0])+int(score[1])
# def find_y(score):
#     """Point Sorting"""
#     return score[1]
# def main():
#     """Point Sorting"""
#     lis = []
#     for i in range(int(input())):
#         for _ in range(int(input())):
#             lis.append(input().split())
#         lis.sort(key=find_y, reverse=True)
#         lis.sort(key=plus)
#         for i in lis:
#             print(*i)
#         lis = []
# main()
