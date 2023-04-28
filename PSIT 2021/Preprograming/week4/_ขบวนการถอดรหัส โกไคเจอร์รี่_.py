'''ขบวนการถอดรหัส โกไคเจอร์รี่'''
def main():
    '''ab'''
    num = int(input())
    keep = ''
    code = ''
    num2 = 0
    for _ in range(num):
        for _ in range(num):
            code = input()
            keep += code
            num2 += 1
    for i in range(len(keep)):
        if i == (keep[i]):
            print('true')
            if i %2 == 0 and i == (keep[i]):
                print('true3')
        else:
            keep = 0
        print(keep)
        # if i.isalnum() or i.isalpha():
        #     if high.count(i) > 0:
        #         corr += chr((ord(i)-60)%26+65)
        #     elif low.count(i) > 0:
        #         corr += chr((ord(i)-97+5)%26+97)
        #     # corr += chr((ord(i)-60)%26+65)
        #     elif i.isalnum():
        #         corr += chr((ord(i)-48+5)%10+48)
        # else:
        #     corr += i
main()
