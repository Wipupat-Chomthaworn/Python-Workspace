"""dimond"""
def main():
    """main"""
    var = int(input())
    for i in range(-var//2, 0):
        for j in range(-var//2, (var//2)+1):
            if abs(i)+abs(j) == 3 or i == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print('*'*var)

main()
# 3210123
#    * 3
#   * *2
#  *   *1
# *******0
#  *   *
#   * *
#    *