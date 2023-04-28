'''Pyramid'''
def main():
    '''ab'''
    num = int(input())
    for i in range(-(num-1), num):
        for j in range(-(num-1), num):
            if abs(i) + abs(j) < num:
                print('*', end='')
            else:
                print(' ', end='')
        print()
main()
