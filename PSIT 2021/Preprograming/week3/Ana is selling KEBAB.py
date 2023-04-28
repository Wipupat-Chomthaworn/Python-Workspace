"""Ana is selling KEBAB"""
def main():
    '''ab'''
    price = int(input())
    num = int(input())
    feedb = (input())
    keb = price*num
    ste1 = 'This kebab is very good'
    ste2 = "This is not good not bad"
    ste3 = "This is not kebab"
    if feedb == ste1:
        print('%.2f'%(keb*70/100))
    elif feedb == ste2:
        print('%.2f'%(keb*95/100))
    elif feedb == ste3:
        print('%.2f'%(keb*116/100))
    elif feedb not in (ste1, ste2, ste3):
        print('%.2f'%0.00)
main()
