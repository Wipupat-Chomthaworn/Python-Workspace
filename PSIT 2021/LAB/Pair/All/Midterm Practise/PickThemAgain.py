"""main"""
def main():
    """main"""
    var = input().split()
    ans = []
    for i in var:
        if int(i)%5 == 0 or int(i)%3 == 0:
            ans.append(int(i))
    ans.reverse()
    if len(ans) == 0:
        print('Nope')
    else:
        for i in ans:
            print(i)
main()
