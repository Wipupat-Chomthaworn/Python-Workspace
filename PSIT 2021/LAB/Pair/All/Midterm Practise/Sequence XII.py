"""Sequence XII"""
def main():
    """ab"""
    var = int(input())
    for _ in range(-var+1, var):
        for j in range(-var, var):
            if abs(j)==2:
                print('03', end='')
            if j != 0:
                print('%02d'%abs(j), end=' ')
        print()
main()
#  2  1  0  1  2
# 03 02 01 02 03 2
# 02 03 02 03 02 1
# 01 02 03 02 01 0
# 02 03 02 03 02 1
# 03 02 01 02 03 2
