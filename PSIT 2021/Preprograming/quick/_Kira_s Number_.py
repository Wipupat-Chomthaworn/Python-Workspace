'''Kira's Number'''
def main():
    '''ab'''
    per = input()
    var = 0
    var2 = 0
    ans = ''
    for i in per:
        var += int(i)
    var2 = var**3
    var3 = int(per)//1000000000000000
    if len(str(var2+var3)) < 5:
        ans = str(int(var3+var2))
        print('%s'%ans.zfill(5))
    elif len(str(var2+var3)) > 5:
        ans = str(int(var3+var2))
        ans = ans[0:5]
        print((ans))
main()
