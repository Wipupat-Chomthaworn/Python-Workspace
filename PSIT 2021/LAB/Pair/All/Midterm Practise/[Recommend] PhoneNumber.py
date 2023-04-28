"""[Recommend] PhoneNumber"""
def main():
    '''main'''
    num = input()
    inter = input()

    if len(num) == 9:
        if inter == "International":
            print('+66 %s %s' %(num[1:5], num[5:]))
        else:
            print('0 %s %s' %(num[1:5], num[5:]))
    else:
        if inter == "International":
            print('+66%s %s %s' %(num[1], num[2:6], num[6:]))
        else:
            print('0%s %s %s' %(num[1], num[2:6], num[6:]))
main()
