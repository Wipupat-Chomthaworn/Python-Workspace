"""bonusheart"""
def main():
    """anotherquest"""
    myheart_1 = int(input())
    heart = '<3'
    bonush = int(input())
    slap_1 = 10 - (myheart_1 + bonush)
    allh = (myheart_1 + bonush)*heart
    allslap = '_'* slap_1
    print('My Heart %d Heart |%s%s|'%(myheart_1, allh, allslap))
    print('My Bonus %d Heart'%(bonush))
main()
