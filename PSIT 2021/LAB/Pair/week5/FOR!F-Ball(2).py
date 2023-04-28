"""FOR!F-Ball"""
def findwhere(var, pos):
    '''Find where'''
    if pos == 1:
        altpos = pos1(var)
    elif pos == 2:
        altpos = pos2(var)
    elif pos == 3:
        altpos = pos3(var)
    return altpos
def pos1(alpha):
    '''Find where'''
    if alpha == 'a':
        return 2
    elif alpha == "b":
        return 1
    elif alpha == "c":
        return 3
def pos2(alpha):
    '''Find where'''
    if alpha == 'a':
        return 1
    elif alpha == "b":
        return 3
    elif alpha == "c":
        return 2
def pos3(alpha):
    '''Find where'''
    if alpha == 'a':
        return 3
    elif alpha == "b":
        return 2
    elif alpha == "c":
        return 1
def main():
    """main function"""
    var = input().lower()
    pos = 1
    for i in range(len(var)):
        ans = findwhere(var[i], pos)
        pos = ans
    print(pos)
main()
# """ FOR!F-Ball """
# def main():
#     """ FOR!F-Ball """
#     txt = input()
#     txt_a = 1
#     txt_b = 0
#     txt_c = 0
#     for i in txt:
#         if i == "A":
#             txt_a, txt_b = txt_b, txt_a
#         elif i == "B":
#             txt_b, txt_c = txt_c, txt_b
#         elif i == "C":
#             txt_a, txt_c = txt_c, txt_a
#     if txt_a == 1:
#         print(1)
#     elif txt_b == 1:
#         print(2)
#     else:
#         print(3)
# main()
