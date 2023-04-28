"""Plan ZXCZXC"""
def arrange():
    """arrange"""
    acdc = input()
    first = float(input())
    second = float(input())
    third = float(input())
    if first <= second and first <= third:
        small = first
    elif second <= first and second <= third:
        small = second
    else:
        small = third
    def arrange3():
        '''2'''
        if first < second and first > third:
            middle = first
            return middle
        elif first > second and first < third:
            middle = first
            return middle
        elif second < first and second > third:
            middle = second
            return middle
        elif second < third and second > first:
            middle = second
            return middle
        else:
            middle = third
            return middle
    middle = arrange3()
    if first >= second and first >= third:
        large = first
    elif second >= first and second >= third:
        large = second
    else:
        large = third
    if acdc == "Ascend":
        print('%.2f, %.2f, %.2f' %(small, middle, large))
    elif acdc == "Descend":
        print('%.2f, %.2f, %.2f' %(large, middle, small))
arrange()
