'''[Midterm] FourDirections'''
def main():
    """main function"""
    var = input()
    upp = ['  *  ', ' *** ', '* * *', '  *  ', '  *  ']
    down = ['  *  ', '  *  ', '* * *', ' *** ', '  *  ']
    left = ['  *  ', ' *   ', '*****', ' *   ', '  *  ']
    right = ['  *  ', '   * ', '*****', '   * ', '  *  ']
    for i in range(5):
        for alpha in var:
            if alpha == 'U':
                print(upp[i], end=' ')
            elif alpha == 'D':
                print(down[i], end=' ')
            elif alpha == 'L':
                print(left[i], end=' ')
            elif alpha == 'R':
                print(right[i], end=' ')
        print()
main()
