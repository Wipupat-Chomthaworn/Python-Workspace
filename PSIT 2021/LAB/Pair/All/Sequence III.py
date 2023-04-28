"""Sequence V"""
def main():
    """main func"""
    var = int(input())
    for i in range(1, var+1):
        for _ in range(var):
            i += 1
            print(i, end=" ")
        print()
main()
# """Sequence V"""
# def main():
#     """main func"""
#     var = int(input())
#     for i in range(var+1, 1, -1):
#         for _ in range(var):
#             i -= 1
#             print(i, end=" ")
#         print()
# main()
