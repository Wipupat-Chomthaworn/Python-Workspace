"""Basic while"""
def main():
    '''ab'''
    dain = 0
    num = 0
    while True:
        num = num + dain
        dain = int(input())
        if dain < 0:
            print(num)
            break
main()
