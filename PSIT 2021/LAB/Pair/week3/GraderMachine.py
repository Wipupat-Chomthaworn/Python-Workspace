'''GraderMachine'''
def main():
    """ab"""
    var = int(input())
    var_2 = int(input())
    keep = 0
    print('pass :', end=' ')
    if var <= var_2:
        for i in range(var, var_2+1):
            if i %2 == 0:
                print(i, end=' ')
                keep += i
    elif var >= var_2:
        for j in range(var, var_2-1, -1):
            if j %2 == 0:
                print(j, end=' ')
                keep += j
    print()
    print('Sum : %d'%keep)
main()
