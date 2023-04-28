"""Left Arrow"""
def main():
    """"""
    vark = int(input())
    varn = int(input())
    keep = 0
    for i in range(((varn-1)//2)+1):
        keep +=0
        for j in range(1, vark+1):
            if j == i+1 or j>vark:
                print('*', end='')
            else:
                print(' ', end='')
        print()
main()