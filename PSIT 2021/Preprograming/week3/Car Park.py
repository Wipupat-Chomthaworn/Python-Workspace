"""Car Park"""
def main():
    '''ab'''
    dain = int(input())
    timin = int(input())
    dayut = int(input())
    timut = int(input())
    alday = dayut-dain
    altime = timut-timin
    if altime > 12:
        alday += 1
    if timin >= 23 and timut <= 23 or altime > 12:
        alday += 1
        altime = timin-23 +timut
        print('%d day %d hour'%(alday, altime))
        print('%d baht'%(alday*))
    elif altime <= 2:
        alday = lvl*1-1
        print('%d day %d hour'%(alday, altime))
        print('0 baht')
    elif lvl > 20 and lvl <= 300:
        alday = ((lvl-20)//2)+19
        print('%d day %d hour'%(alday,))
        print('%d baht'%(500-alday))
    elif lvl > 300 and lvl <= 500:
        alday = ((lvl-300)*1//5)+159
        print('%d day %d hour'%(alday,))
        print('%d baht'%(500-alday))
    elif lvl > 500:
        alday = 199
        print('%d day %d hour'%(alday,))
        print('%d baht'%(500-alday))
    elif alday < 0:
        print('error')
main()
 