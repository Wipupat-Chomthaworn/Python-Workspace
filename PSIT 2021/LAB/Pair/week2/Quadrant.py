'''Quadrant'''
def main():
    '''ab'''
    x_value = float(input())
    y_value = float(input())
    if x_value > 0 and y_value > 0:
        print('Q1')
    elif x_value < 0 and y_value > 0:
        print('Q2')
    elif x_value < 0 and y_value < 0:
        print('Q3')
    elif x_value > 0 and y_value < 0:
        print('Q4')
    elif x_value == 0 and y_value == 0:
        print('O')
    elif x_value == 0 and y_value != 0:
        print('Y')
    elif x_value != 0 and y_value == 0:
        print('X')
main()
