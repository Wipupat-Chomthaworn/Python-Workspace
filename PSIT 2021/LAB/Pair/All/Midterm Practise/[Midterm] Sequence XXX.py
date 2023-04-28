"""[Midterm] Sequencexxx"""
def main():
    """main"""
    varc = int(input())
    times = int(input())
    text = ''
    for i in range(varc):
        for j in range(varc):
            if i in (0, varc-1) or j in (0, varc-1) or i == j or j == varc-i-1:
                text += '*'
            else:
                text += ' '
        for _ in range(times):
            print(text, end=' ')
        text = ''
        print()
main()
# 01234
# *****0
# ** **1
# * * *2
# ** **3
# *****4
