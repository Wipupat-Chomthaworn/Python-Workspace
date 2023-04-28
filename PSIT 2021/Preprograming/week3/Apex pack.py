"""Apex pack"""
def main():
    '''ab'''
    lvl = int(input())
    if lvl == 1 or lvl < 1:
        box = 0
        print('%d Packs opened'%(box))
        print('%d Packs more'%(500-box))
    elif lvl >= 2 and lvl <= 20:
        box = lvl*1-1
        print('%d Packs opened'%(box))
        print('%d Packs more'%(500-box))
    elif lvl > 20 and lvl <= 300:
        box = ((lvl-20)//2)+19
        print('%d Packs opened'%(box))
        print('%d Packs more'%(500-box))
    elif lvl > 300 and lvl <= 500:
        box = ((lvl-300)*1//5)+159
        print('%d Packs opened'%(box))
        print('%d Packs more'%(500-box))
    elif lvl > 500:
        box = 199
        print('%d Packs opened'%(box))
        print('%d Packs more'%(500-box))
main()
 