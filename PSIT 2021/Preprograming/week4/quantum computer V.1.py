"""quantum computer V.1"""
def main():
    '''ab'''
    num1 = int(input())
    ans = 0
    for _ in range(num1):
        key = input()
        if key == 'INC':
            ans += 1
        elif key == 'DEC':
            ans -= 1
        elif key == 'DUBL':
            ans = ans*2
        elif key == 'HALF':
            ans = ans/2
    print('%.2f'%(ans))
main()
