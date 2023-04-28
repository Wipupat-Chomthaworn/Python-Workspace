# """Triangle I"""
# def main():
#     """docstring"""
#     var = float(input())
#     var2 = float(input())
#     var3 = float(input())
#     var12 = int((var**2)+(var2**2))
#     varlast = int(var3**2)
#     if abs(varlast - var12) <= 0.1 or varlast == var12:
#         print('Yes')
#     else:
#         print('No')
# main()
"""Triangle I"""
def main():
    """docstring"""
    var = float(input())
    var2 = float(input())
    var3 = float(input())
    if var > var2 and var > var3 and var2 >= var3:
        most = var
        sec = var2
        low = var3
    elif var > var2 and var > var3 and var2 <= var3:
        most = var
        sec = var3
        low = var2
    elif var2 > var and var2 > var3 and var >= var3:
        most = var2
        sec = var
        low = var3
    elif var2 > var and var2 > var3 and var <= var3:
        most = var2
        sec = var3
        low = var
    elif var3 > var and var3 > var2 and var >= var2:
        most = var3
        sec = var
        low = var2
    else:
        most = var3
        sec = var2
        low = var

    var12 = float((sec**2)+(low**2))
    varlast = float(most**2)
    if abs(varlast % var12) - 0.01 <= 0 or varlast == var12\
        or abs(var12 -varlast) <= 0.01:
        print('Yes')
    else:
        print('No')
main()
