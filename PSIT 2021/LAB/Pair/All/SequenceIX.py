"""Sequence IX"""
def main():
    """"""
    var = int(input())
    for i in range(1, var+1):
        for j in range(-var, var):
            if abs(i)==abs(j) or i>j:
                print('%02d'%(abs(i)-abs(j)+1), end=' ')
            else:
                print(' ', end=' ')
        print()
main()
# 3  2  1  0  1  2  3
#          01   1
#       01 02 01    2
#    01 02 03 02 01 3
# 01 02 03 04 03 02 01  4