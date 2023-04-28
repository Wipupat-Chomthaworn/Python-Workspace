'''Letter Row'''
def main():
    '''ab'''
    num = int(input())
    keep = ''
    for _ in range(num):
        code = input()
        for j in code:
            if j.isalpha():
                keep += j
    print(keep)
main()
