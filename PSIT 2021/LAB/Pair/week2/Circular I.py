'''Circular I'''
def main():
    '''ab'''
    my_x = float(input())
    my_y = float(input())
    red = float(input())
    mosx = float(input())
    mosy = float(input())
    dis = (((mosx - my_x)**2)+((mosy - my_y)**2))**0.5
    if dis <= red:
        print('Yes')
    else:
        print('No')
main()
