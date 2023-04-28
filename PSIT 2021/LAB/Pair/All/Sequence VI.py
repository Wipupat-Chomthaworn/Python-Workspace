"""Sequence VI"""
def main():
    """ab"""
    var = int(input())
    ans = []
    for i in range(1, var+1):
        ans.append(i)
        ans2 = str(ans).replace(',', '')
        ans3 = ans2.replace(']', '')
        finans = ans3.replace('[', '')
        print(finans)
main()
