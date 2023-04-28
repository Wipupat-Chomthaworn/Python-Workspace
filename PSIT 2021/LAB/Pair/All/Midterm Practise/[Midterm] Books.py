"""[Midterm] Books"""
def main():
    '''main'''
    import math
    book = int(input())
    page = int(input())
    varx = int(input())
    vary = int(input())
    keep = 0
    rou = 0
    count = 0
    aaa = 0
    while True:
        today = math.ceil(((varx+rou)/(vary+rou))*page)
        if count == book or today >= page:
            break
        keep += today
        aaa += 1
        rou += 1
        if page-keep <= 0:
            keep = 0
            count += 1
        # print(today)
    print(aaa+(book-count))
main()
    # day1 = math.ceil((varx/vary)*page)
    # day2 = math.ceil(((varx+1)/(vary+1))*page)
    # day3 = math.ceil((x+2)/(y+2)*page)
