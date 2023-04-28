"""Inverter"""
def main():
    """main"""
    var = input()
    ans = (var.replace('1', 'x')).replace('0', 'y')
    ans = (ans.replace('x', '0')).replace('y', '1')
    if int(ans) == 0:
        print(ans[:ans.find('1')+1])
    else:
        print(int(ans))
main()
