"""main"""
def che(var):
    """cen"""
    if var[0:3] == "B.E":
        ans = str(int(var[4:])-543)
    else:
        ans = (var[4:])
    if int(ans[2:]) > 0:
        print(int(ans[0:2])+1)
    else:
        print(ans[0:2])
def main():
    """main"""
    num = int(input())
    for _ in range(num):
        var = input()
        che(var)
main()
