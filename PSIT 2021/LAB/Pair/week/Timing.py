"""Timing"""
def main():
    '''hi'''
    seconds = int(input())
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    print(days, hours, minutes, seconds, sep=' ')
main()
