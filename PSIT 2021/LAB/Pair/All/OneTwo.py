"""main"""
def check(sn1, sn2):
    """check"""
    ans = sn2 + sn1
    return ans, sn2

def main():
    """main"""
    sn1 = '1'
    sn2 = '2'
    for _ in range(int(input())):
        sn1, sn2 = check(sn1, sn2)
    print(sn1)
main()
