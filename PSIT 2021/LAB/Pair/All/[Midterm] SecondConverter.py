"""Timing"""
def main():
    '''hi'''
    seconds = int(input())
    mini = int(input())
    hou = int(input())
    day = int(input())
    aseconds = seconds % mini
    aminutes = seconds // mini#a = ans
    aseconds %= mini
    ahours = aminutes // hou
    aminutes %= hou
    # adays = ahours // day
    ahours %= day
    # print(aseconds, aminutes, ahours, adays)
    # if adays > 0:
    #     for i in adays:
    #     ahours = adays
    print("%d:%d:%d"%(ahours, aminutes, aseconds))
main()
