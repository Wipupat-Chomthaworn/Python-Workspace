'''The Screen'''
def main():
    '''ab'''
    kung = int(input())
    hight = int(input())
    where = int(input())
    leve = int(input())
    mass = input()
    print('-'*kung)
    for i in range(1, hight-1):
        if i == leve:
            if where == 1:
                print('|%s'%(' '*(kung-len(mass)-2)), end='%s'%(mass))
            elif where == -1:
                print('|%s'%(mass), end='%s'%(' '*(kung-len(mass)-2)))
            print('|')
        else:
            print('|'+' '*(kung-2)+'|', end='\n')
    print('-'*kung)
main()
