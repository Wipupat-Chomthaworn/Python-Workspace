"""Kanomwhan Bakery"""
def main():
    '''ab'''
    human = int(input())
    price = abs(float(input()))
    discount = int(input())
    withdis = human*price
    pro1 = (withdis-(withdis*discount/100))
    pro2 = 0
    if human < 3:
        print('Promotion 1 %.3f Baht '%(withdis))
    if human >= 4:
        pro2 = (human//4)*3*price+((human%4)*price)
        if pro1 <= pro2:
            print('Promotion 1 %.3f Baht '%(pro1))
        else:
            print('Promotion 2 %.3f Baht '%(pro2))
    if human == 3:
        print('Promotion 1 %.3f Baht '%(pro1))
    print('Purchase successfully !')
    print('Have a good meal with "Kanomwhan"')
main()
