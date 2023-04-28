"""[Midterm] Sequencexxx"""
def seqx(varc):
    """seqx"""
    for i in range(varc):
        for j in range(varc):
            if i in (0, varc-1) or j in (0, varc-1) or i == j or j == varc-i-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def main():
    """main"""
    varc = int(input())
    times = int(input())
    for _ in range(times):
        for i in range(varc):
            for j in range(varc):
                if i in (0, varc-1) or j in (0, varc-1) or i == j or j == varc-i-1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
main()
# 01234
# *****0
# ** **1
# * * *2
# ** **3
# *****4
