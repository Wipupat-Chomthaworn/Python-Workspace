"""Just a normal average day V.1"""
def main():
    '''ab'''
    max1 = (float(input()))
    max2 = (float(input()))
    max3 = (float(input()))
    max4 = (float(input()))
    max5 = (float(input()))
    max6 = (float(input()))
    allmax = max(max1, max2, max3, max4, max5, max6)
    allmax2 = min(max1, max2, max3, max4, max5, max6)
    allmax3 = max1 + max2 + max3 + max4 + max5 + max6
    allmax4 = (allmax3/6)
    print('max : %.2f'%(allmax))
    print('min : %.2f'%(allmax2))
    print('sum : %.2f'%(allmax3))
    print('avg : %.4f'%(allmax4))
main()
