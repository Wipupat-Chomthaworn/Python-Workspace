"""Just M3X it V.4"""
def find(var, var1):
    '''ab'''
    ans = var*(var > var1) + var1*(var <= var1)
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
    ans = find(ans, float(input()))
    ans = find(ans, float(input()))
    print('%.2f'%ans)
main()
