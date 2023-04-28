"""SaveComputeRepeat"""
def main():
    '''hi'''
    start_here = 492137954293754252786
    milliseconds = start_here
    seconds = milliseconds // 1000
    milliseconds = milliseconds % 1000
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    print(days, hours, minutes, seconds, milliseconds, sep=' ')
main()
