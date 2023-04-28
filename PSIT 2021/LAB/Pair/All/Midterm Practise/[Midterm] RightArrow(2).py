"""[Midterm] RightArrow"""
def main():
    '''main'''
    col = int(input())
    row = int(input())
    for i in range(row//2):
        print(' '*i, end='')
        for _ in range(col):
            print('*', end='')
        print()
    for i in range(-row//2, 0):
        print(' '*(abs(i)-1), end='')
        for _ in range(col):
            print('*', end='')
        print()
main()
# """[Midterm] RightArrow"""
# def main():
#     """mainfunction"""
#     num1 = int(input())
#     num2 = int(input())
#     space = (num2 // 2)-2
#     for i in range(num2):
#         print((" " * space) + ("*" * num1))
#         if i < num2 // 2:
#             space += 1
#         else:
#             space -= 1
# main()
# for i in range(-(height//2), (height//2)+1):
#         print("%s%s" % (" "*abs(i), ("*"*width)))
# *******
#  *******
#   *******
#  *******
# *******
#
# **********
#  **********
#   **********
#    **********
#     **********
#      **********
#     **********
#    **********
#   **********
#  **********
# **********
