'''Timing II'''
def main():
    '''ab'''
    seconds = int(input())
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    if len(str(days)) <= 4:
        print("%4s:%02d:%02d:%02d"%(str(days).zfill(4), hours, minutes, seconds))
    else:
        print('ERR_:__:__:__')
main()
