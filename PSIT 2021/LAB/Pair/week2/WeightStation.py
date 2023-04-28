'''WeightStation'''
def main():
    '''ab'''
    avg = float(input())
    wl1 = float(input())#wheel
    wl2 = float(input())
    wl3 = float(input())
    wl4 = (avg*4)-(wl1+wl2+wl3)
    allwl = (wl1+wl2+wl3+wl4)
    if allwl > 15000:#over15tons
        print('Overweight')
    elif abs(avg-wl1) > (avg/2):
        print('Unbalance')
    elif abs(avg-wl2) > (avg/2):
        print('Unbalance')
    elif abs(avg-wl3) > (avg/2):
        print('Unbalance')
    elif abs(avg-wl4) > (avg/2):
        print('Unbalance')
    else:
        print('Pass %.2f'%(wl4))
main()
