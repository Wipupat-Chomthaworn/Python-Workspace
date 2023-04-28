"""[Midterm] Books"""
def main():
    '''main'''
    kprice = 0
    ksize = 0
    for i in range(int(input())):
        price, size = float(input()), float(input())
        avg = size/price
        if i == 0:
            high = avg
            kprice = price
            ksize = size
        if avg > high:
            high = avg
            kprice = price
            ksize = size
        elif avg == high:
            if kprice > price:
                kprice = price
                ksize = size
    print('%.2f %.2f'%(kprice, ksize))
main()
