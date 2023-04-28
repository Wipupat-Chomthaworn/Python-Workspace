"""Sequence V"""
def main():
    """main func"""
    var = int(input())
    for i in range(var+1, 1, -1):
        a = i-1
        for _ in range(a):
            print(a, end=" ")
        print()
            

main()
# """Virus I"""
# def main():
#     """main func"""
#     num = int(input())
#     keep = 0
#     for _ in range(num-1):
#         for _ in range(num-1):
#             keep += 1
#             last = num-keep+1
#             if last >= 1:
#                 print(last, end=" ")
#             elif last == 0:
#                 break
#         print()
# main()
