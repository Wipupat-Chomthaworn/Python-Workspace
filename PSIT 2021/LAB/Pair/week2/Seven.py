"""Seven"""
def main():
    '''main'''
    ans = int(input())
    if ans > 10000000:
        ans = ans%100
    elif ans == 1000000:
        ans = ans%10
    if ans%4 == 1:
        ans2 = 7
    elif ans%4 == 2:
        ans2 = 9
    elif ans%4 == 3:
        ans2 = 3
    elif ans%4 == 0:
        ans2 = 1
    print('%d'%(ans2))
main()
