"""Kerati, Master of Noodle V.1"""
def main():
    """ab"""
    ban = (input()).lower()
    fav = (input()).lower()
    num = int(input())
    # ban1 = ('chotipat', 'mawai', 'nisjung', 'yummayro')
    favp = fav.lower().count('pork')
    chot = 280*num
    maw = (280 - 280*15/100)*num
    nis = (280 + ((280/8)**(1/2))*3)*num
    yum = (280 - (280%100/16))*num
    def findpork(ans):
        '''findpork'''
        if favp == 0:
            ans += ans*10/100
            return ans
        else:
            return ans
    if ban == 'chotipat':
        print('%d'%findpork(chot))
    elif ban == 'mawai':
        print('%d'%findpork(maw))
    elif ban == 'nisjung':
        print('%d'%findpork(nis))
    elif ban == 'yummayro':
        print('%d'%findpork(yum))
    else:
        print('No Data !!')
main()
