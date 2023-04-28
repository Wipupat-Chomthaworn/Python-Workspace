"""Final Battle"""
def main():
    """ab"""
    ben = int(input())
    gwen = int(input())
    gper = gwen*int(input())/100
    gogo = int(input())
    if gper+gogo == ben:
        print('The world is save but we lost our hero.')
    elif gper+gogo > ben:
        print('The world is save!')
    else:
        print('Ben 99 is going to ruin the world.')
main()
