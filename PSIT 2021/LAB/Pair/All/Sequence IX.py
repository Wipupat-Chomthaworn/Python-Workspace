"""Sequence IX"""
def main():
    """main func"""
    var = int(input())
    for i in range(1, var+1):
        for j in range(-1, var+1):
            ans = abs(var-(i +j))
            if abs(i)+abs(j) > var or i+j >= var+2:
                print("%02d"%(ans), end="  ")
            elif i+j <= var:
                print(' ', end=" ")
        print()
main()
# 1  2  3  4  5  6  7 
#          01   -1
#       01 02 01    0
#    01 02 03 02 01   1
# 01 02 03 04 03 02 01  2

# -3 -2 -1  0  1  2  3 
#          01   1
#       01 02 01    2
#    01 02 03 02 01   3
# 01 02 03 04 03 02 01  4