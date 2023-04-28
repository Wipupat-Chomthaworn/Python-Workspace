"""Composite Function"""
def main():
    """anotherquest"""
    num = float(input())
    def ffunction(num1):
        """anotherquest"""
        ans = (15+num1-(num1**3))/(((num1**2)/3)+11)
        return ans

    def gfunction(num2):
        """anotherquest"""
        ans1 = (num2**3) + (4*num2) -1
        return ans1
    fog = ffunction(gfunction(num))
    gof = gfunction(ffunction(num))
    print('%.4f'%(fog))
    print('%.4f'%(gof))
main()
