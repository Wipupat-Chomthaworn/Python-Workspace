"""Nearer"""
def main():
    '''main'''
    alice = int(input())
    bob = int(input())
    ice = int(input())
    disa = abs(alice-ice)
    disb = abs(bob-ice)
    if disa > disb:
        print('Bob %d'%disb)
    elif disa < disb:
        print('Alice %d'%disa)
    else:
        print('Sundaes %d'%disa)
main()
