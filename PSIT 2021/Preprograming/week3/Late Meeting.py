"""Late Meeting"""
def main():
    '''ab'''
    hour = int(input())
    minit = int(input())
    sec = int(input())
    am_pm = (input())
    fminit = int(input())
    fsec = int(input())
    allsec = (sec+fsec)%60
    allminit = (minit +fminit+((sec+fsec)//60))%60
    alhour = (hour + (minit +fminit+((sec+fsec)//60))//60)
    
    # if alhour >= 12 and alhour < 24:
    #     alhour = alhour%12
    #     if am_pm == 'pm':
    #         am_pm = 'am'
    #     elif am_pm == 'am':
    #         am_pm = 'pm'
    # if alhour >= 24:
    #     alhour = alhour%24
    # if price == 0:
    #     print('%2d:%2d:%2d %s'(alhour, allminit, allsec, am_pm))
    # elif minit <= 2:
    #     print('free')
    # elif minit <= 15 and minit > 2:
    #     allp = price*15
    #     print('%d'%(allp))
    # else:
    #     allp = price*minit
    #     print('%d'%(allp))

    if am_pm == 'am' and hour == 12:
        hour = 0
        allsec = (sec+fsec)%60
        allminit = (minit +fminit+((sec+fsec)//60))%60
        alhour = (hour + (minit +fminit+((sec+fsec)//60))//60)
    elif am_pm == 'pm' and hour != 12:
        hour += 12
        allsec = (sec+fsec)%60
        allminit = (minit +fminit+((sec+fsec)//60))%60
        alhour = (hour + (minit +fminit+((sec+fsec)//60))//60)
        if alhour > 12:
            am_pm = 'pm'
        else:
            am_pm = 'am'
        alhour = (hour + (minit +fminit+((sec+fsec)//60))//60)%12
    

    print('%02d:%02d:%02d %s'%(alhour, allminit, allsec, am_pm))
main()
