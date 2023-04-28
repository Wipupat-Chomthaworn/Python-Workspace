"""Multiplication Table V.1"""
def main():
    '''ab'''
    num = int(input())
    print('-----------------')
    for i in range(1, 13):
        mal = num*i
        print('%3d x %3d = %5d'%(num, i, mal))
    print('-----------------')
main()
