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
    while True:
        if keep >= page:
            break
        read = math.ceil(((varx+rou)/(vary+rou))*page)
        keep+=read
        rou +=1
        print(read)
main()
    # day1 = math.ceil((varx/vary)*page)
    # day2 = math.ceil(((varx+1)/(vary+1))*page)
    # day3 = math.ceil((x+2)/(y+2)*page)