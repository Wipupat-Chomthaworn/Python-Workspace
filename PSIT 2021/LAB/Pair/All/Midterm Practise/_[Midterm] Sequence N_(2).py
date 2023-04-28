'''[Midterm] Sequence N'''
def main():
    """main function"""
    var = int(input())
    for i in range(var):
        for j in range(var):
            if i == j or j == 0 or j == var-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
main()
# *    *
# **   *
# * *  *
# *  * *
# *   **
# *    *
