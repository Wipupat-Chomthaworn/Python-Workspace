'''Stairs V.2'''
def main():
    '''ab'''
    num = int(input())
    for i in range(1,num+1):
        for j in range(1,i):
            for k in range(j:i:-1):
                print(j, end='')
                print(k, end='')
                
            # for k in range(num,1):
            #     print(j+k, end='')
        print()
        # for j in range(i, num, 1):
        #     print('%d+\n'%(i))

main()
