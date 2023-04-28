'''lightinggggg'''
def main():
    '''main'''
    var_1 = int(input())
    var_2 = int(input())
    for i in range(var_2//2, 0, -1):
        print((i)*' '+'*'*var_1)
    print('*'*var_1)
    for j in range(1, var_2//2+1):
        print((j)*' '+'*'*var_1)
main()
# """Problem"""
# def main():
#     """Print AB"""
#     width = int(input())
#     high = int(input())
#     total = high//2
#     for i in range(high):
#         print((" "*total)+("*"*width))
#         if i < high//2:
#             total -= 1
#         else:
#             total += 1
# main()
