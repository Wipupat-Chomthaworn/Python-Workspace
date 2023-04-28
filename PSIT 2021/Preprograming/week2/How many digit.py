"""How many digit?"""
def main():
    '''ab'''
    maxp = input()
    max0 = maxp.count('1')
    max1 = maxp.count('2')
    max2 = maxp.count('3')
    max3 = maxp.count('4')
    max4 = maxp.count('5')
    max5 = maxp.count('6')
    max6 = maxp.count('7')
    max7 = maxp.count('8')
    max8 = maxp.count('9')
    max9 = maxp.count('0')
    ans = max0+max1+max2+max3+max4+max5+max6+max7+max8+max9
    print(ans)
main()
