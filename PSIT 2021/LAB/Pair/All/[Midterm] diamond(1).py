"""dimond"""
def main():
    """main"""
    num = int(input())
    for i in range((-num//2)+1, (num//2)+1):
        for j in range((-num//2)+1, (num//2)+1):
            if abs(i) + abs(j) == (num//2) or abs(i) == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
main()
# 3210123 j
#    * 3
#   * *2
#  *   *1
# *******0 i
#  *   * 1
#   * * 2
#    * 3

# 101
#  * 1
# *** 0
#  * 1
