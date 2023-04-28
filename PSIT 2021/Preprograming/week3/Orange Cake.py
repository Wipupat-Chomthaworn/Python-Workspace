"""Orange Cake"""
def main():
    '''ab'''
    mon = int(input())
    price = int(input())
    cake = mon // price
    monle = mon % price
    if cake >= 1:
        print('Orange Cake: %d'%(cake))
        print('Money left: %d'%(monle))
    elif cake <= 1:
        print('Not enough money;(')
        print('Money left: %d'%(monle))
main()
