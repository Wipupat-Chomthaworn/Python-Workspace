"""คอยเซ็นเตอร์"""
def main():
    '''ab'''
    price = int(input())
    minit = int(input())
    sec = int(input())
    if sec > 30:
        minit += 1
    if price == 0:
        print('free')
    elif minit <= 2:
        print('free')
    elif minit <= 15 and minit > 2:
        allp = price*15
        print('%d'%(allp))
    else:
        allp = price*minit
        print('%d'%(allp))
main()
