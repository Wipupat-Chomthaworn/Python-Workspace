"""Stepper II"""
def main():
    """ab"""
    var = int(input())
    var2 = int(input())
    if var <= var2:
        for i in range(var, var2+1):
            print(i)
    elif var >= var2:
        for j in range(var, var2-1, -1):
            print(j)
main()
