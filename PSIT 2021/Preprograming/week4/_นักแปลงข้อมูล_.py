'''นักแปลงข้อมูล'''
def main():
    '''ab'''
    cryp = input()
    corr = ''
    high = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = ' abcdefghijklmnopqrstuvwxyz'
    for i in cryp:
        if i.isalnum() or i.isalpha():
            if high.count(i) > 0:
                corr += chr((ord(i)-60)%26+65)
            elif low.count(i) > 0:
                corr += chr((ord(i)-97+5)%26+97)
            # corr += chr((ord(i)-60)%26+65)
            elif i.isalnum():
                corr += chr((ord(i)-48+5)%10+48)
        else:
            corr += i
    print(corr)
main()
