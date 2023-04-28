"""Inverter"""
def main():
    """main"""
    var = input()
    ans = (var.replace('1', 'x')).replace('0', 'y')
    ans = (ans.replace('x', '0')).replace('y', '1')
    if int(var) < 0:
        var = abs(int(var))
    print(abs(int(ans)))
main()
