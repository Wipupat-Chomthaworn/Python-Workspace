'''PointInCircle'''
def main():
    '''ab'''
    var_x = float(input())
    var_y = float(input())
    red = float(input())
    ptx = float(input())
    pty = float(input())
    dis = (((ptx - var_x)**2)+((pty - var_y)**2))**0.5
    if dis <= red:
        print('True')
    else:
        print('False')
main()
