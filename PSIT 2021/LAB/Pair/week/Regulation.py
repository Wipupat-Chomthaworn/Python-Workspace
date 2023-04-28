"""Regulation"""
def main():
    """Input and Calc"""
    var1 = int(input())
    var2 = float(input())
    var3 = input()
    print('%30s'%(str(var1)))
    print('%30s'%(str(var1).zfill(30)))
    print('%.2f'%(var2))
    print('%.12f'%(var2))
    print('%40s'%(str(var3)))
main()
