"""Sequence VIII"""
def main():
    """ab"""
    var = int(input())
    for i in range(1, var+1):
        for j in range(1, var+1):
            ans = abs(i +j -var)
            if i +j == var+1 or i+j > var:
                print("%02d"%(ans), end=" ")
            else:
                print(' ', end="  ")
        print()
main()
# 1  2  3
#       01  1
#    01 02  2
# 01 02 03  3
