"""How many in this ads?"""
def main():
    '''ab'''
    owen = input()
    upp = 0
    low = 0
    num = 0
    for i in range(len(owen)):
        if ord(owen[i]) >= 97 and ord(owen[i]) <= 122:
            upp += 1
        elif (ord(owen[i]) >= 65 and
              ord(owen[i]) <= 90):
            low += 1
        if owen[i].isdigit():
            num += 1
    print('%d number(s)'%(num))
    print('%d uppercase letter(s)'%(low))
    print('%s lowercase letter(s)'%(upp))
main()
