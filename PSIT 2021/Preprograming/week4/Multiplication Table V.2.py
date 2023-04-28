"""Multiplication Table V.2"""
def main():
    '''ab'''
    print('-------------')
    for j in range(2, 13):
        num = j
        for i in range(1, 13):
            mal = j*i
            print('%2d x %2d = %3d'%(num, i, mal))
        print('-------------')
main()
