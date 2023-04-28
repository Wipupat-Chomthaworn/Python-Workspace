"""ป้ายไฟ"""
def main():
    """anotherquest"""
    num = input().upper()
    num2 = (len(num) + 4) * '-'
    print('|%s|'%(num2))
    print('|  %s  |'%(num))
    print('|%s|'%(num2))
main()
