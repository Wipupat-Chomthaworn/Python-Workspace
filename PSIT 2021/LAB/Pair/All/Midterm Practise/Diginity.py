'''[Midterm] Diginity'''
# def sumans(ans):
#     '''sum ans'''
#     keep = 0
#     while True:
#         for i in str(ans):
#             keep += int(i)
#         if keep<=9:
#             # return keep
#             break
#         else:
#             ans = keep
#     print(keep)
#     return keep
#     # print(ans)
#     # return ans
# sumans(int(input()))
def main():
    '''main'''
    ans = 0
    while True:
        var = int(input())
        if var == 0:
            break
        elif var > 9:
            if var > 99:
                print(str(var)[-1])
            # for i in var:
            #     ans += i
    print(ans)
main()
# ans = 0
#     while True:
#         var = int(input())
#         if var == 0:
#             break
#         elif var > 9:
#             for i in var:
#                 ans += i
#             if not ans >9: