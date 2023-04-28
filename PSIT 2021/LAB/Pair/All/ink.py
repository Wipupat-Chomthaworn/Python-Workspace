"""Ink"""

import math
def is_tum(speed, var):
    """Let find"""
    dis = ((0-int(var[0]))**2 + (0-int(var[1]))**2)**0.5
    count = 0
    pii = 3.1416
    speed2 = 0
    while True:
        speed2 += speed
        red = abs((speed2/pii)**0.5)
        if int(var[0]) == 0 and int(var[1]) == 0:
            return count
        count += 1
        if red >= dis:
            return count
        red += red
        # print(red, dis, count, speed2)

def main():
    """main"""
    sam = input().split()
    speed = int(sam[0])
    # location = {}
    for _ in range(int(sam[1])):
        var = input().split()
        # location[int(var[0])] = int(var[0])
        ans = is_tum(speed, var)
        print(math.ceil(ans))
main()
