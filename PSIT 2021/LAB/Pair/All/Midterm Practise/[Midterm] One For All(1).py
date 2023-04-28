# """[Midterm] One For All"""
# def main():
#     """main"""
#     num = int(input())
#     for i in range(num):
#         var = input()
#         if i %2 == 0:
#             print('-'*i+var, end='')
#         else:
#             print('*'*i+var, end='')
#     print('_%d'%(num))
# main()
"""[Midterm] One For All"""
def main():
    """main"""
    num = int(input())
    keep = ''
    if num == 0:
        print()
    else:
        for i in range(num):
            var = input()
            if i %2 == 0:
                keep += '-'*i+var
            else:
                keep += '*'*i+var
        print('%s_%d'%(keep, num))
main()
