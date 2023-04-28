"""[Recommend] Books"""
import math
def main():
    """[Recommend] Books"""
    bookall = int(input())
    page = int(input())
    var_x = int(input())
    var_y = int(input())
    count = 0
    tally = 0
    this = 0
    iss = 0
    while True:
        today = math.ceil(((var_x+iss)/(var_y+iss))*page)
        if count == bookall or today >= page:
            break
        this += today
        tally += 1
        iss += 1
        if page-this <= 0:
            this = 0
            count += 1
        # print(today)
    print(tally+(bookall-count))
    # print(count)
    # print(tally)
main()