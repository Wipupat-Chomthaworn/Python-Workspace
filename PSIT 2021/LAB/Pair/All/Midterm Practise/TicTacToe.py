"""main"""
def matric():
    """main"""
    lst = []
    lst2 = []
    for _ in range(3):
        var = input()
        for i in var:
            var2 = i
            lst2.append(var2)
        lst.append(lst2)
        lst2 = []
    if lst[0][-1] == lst[1][1] == lst[-1][0] \
        or lst[0][0] == lst[1][1] == lst[-1][-1]:
        print("%s WIN"%lst[1][1])
    elif lst[0][0] == lst[0][1] == lst[0][-1] \
        or lst[0][0] == lst[1][0] == lst[-1][0]:
        print("%s WIN"%lst[0][0])
    elif lst[1][0] == lst[1][1] == lst[1][-1] \
        or lst[0][1] == lst[1][1] == lst[-1][1]:
        print("%s WIN"%lst[1][1])
    elif lst[-1][0] == lst[-1][1] == lst[-1][-1] \
        or lst[0][-1] == lst[1][-1] == lst[-1][-1]:
        print("%s WIN"%lst[-1][-1])
    else:
        print("DRAW")
    # for i in lst:
    #     print(*i, sep=" ")
matric()
# """main"""
# def matric():
#     """main"""
#     lst = []
#     lst2 = []
#     for _ in range(3):
#         var = input()
#         for i in var:
#             var2 = i
#             lst2.append(var2)
#         lst.append(lst2)
#         lst2 = []
#     if lst[0][-1] == lst[1][1] == lst[-1][0] \
#         or lst[0][0] == lst[1][1] == lst[-1][-1]:
#         if lst[1][1] in ('X', 'O'):
#             print("%s WIN"%lst[1][1])
#         else:
#             print("DRAW")
#     elif lst[0][0] == lst[0][1] == lst[0][-1] \
#         or lst[0][0] == lst[1][0] == lst[-1][0]:
#         if lst[1][1] in ('X', 'O'):
#             print("%s WIN"%lst[0][0])
#         else:
#             print("DRAW")
#     elif lst[1][0] == lst[1][1] == lst[1][-1] \
#         or lst[0][1] == lst[1][1] == lst[-1][1]:
#         if lst[1][1] in ('X', 'O'):
#             print("%s WIN"%lst[1][1])
#         else:
#             print("DRAW")
#     elif lst[-1][0] == lst[-1][1] == lst[-1][-1] \
#         or lst[0][-1] == lst[1][-1] == lst[-1][-1]:
#         if lst[1][1] in ('X', 'O'):
#             print("%s WIN"%lst[-1][-1])
#         else:
#             print("DRAW")
#     else:
#         print("DRAW")
#     # for i in lst:
#     #     print(*i, sep=" ")
# matric()
