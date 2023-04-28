"""OG is waiting for you"""
def main():
    """ab"""
    age = int(input())
    if age >= 17 and age <= 23:
        if age < 20:
            per = (input()).upper()
            exp = int(input())
            abod = (input()).upper()
            if per == 'Y' and exp >= 12 and abod == 'Y':
                print('You can be in OG!')
            else:
                print('May be next time.')
        else:
            exp = int(input())
            abod = (input()).upper()
            if exp >= 12 and abod == 'Y':
                print('You can be in OG!')
            else:
                print('May be next time.')
    else:
        print('May be next time.')
main()
