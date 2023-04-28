"""DataSpike"""
def find(var, var1):
    '''ab'''
    if var > var1:
        ans = var
    elif var <= var1:
        ans = var1
    return ans
def main():
    '''main'''
    ans = find(float(input()), float(input()))
    ans = find(ans, float(input()))
    ans = find(ans, float(input()))
    ans = find(ans, float(input()))
    ans = find(ans, float(input()))
    ans = find(ans, float(input()))
    ans = find(ans, float(input()))
    print('%d'%(ans))
main()
