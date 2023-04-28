# """Sequence VII"""
# def main():
#     """main func"""
#     var = int(input())
#     for i in range(var+1, 1, -1):
#         a = i-1
#         for _ in range(a):
#             print(i, end=" ")
#         print()
# main()
"""Sequence VII"""
def main():
    """main func"""
    var = int(input())
    for i in range(1, var+1):
        for j in range(1, i+1):
            if i == j:
                print(i, end=" ")
            else:
                print(j, end=" ")
        print()
    for i in range(var-1, 0, -1):
        for j in range(1, i+1):
            if i == j:

                print(i, end=" ")
            else:
                print(j, end=" ")
        print()
main()
