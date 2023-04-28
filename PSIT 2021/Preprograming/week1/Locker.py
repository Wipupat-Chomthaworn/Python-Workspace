"""locker"""
def main():
    '''def'''
    all_1 = int(input())
    used = int(input())
    var_3 = all_1 - used
    print('X' * used + 'O' * var_3 + " (available: %s)" %(var_3))
main()
