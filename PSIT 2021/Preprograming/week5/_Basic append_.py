'''Basic append'''
def main():
    '''ab'''
    num = int(input())
    mylist = []
    for _ in range(num):
        mylist.append(input())
    for i in mylist:
        print(i, end=' ')
        # for j in range(i, num, 1):
        #     print('%d+\n'%(i))
main()
