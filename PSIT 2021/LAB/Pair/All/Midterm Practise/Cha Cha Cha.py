"""main"""
import math
def main():
    """main"""
    day = int(input())
    won = 8720
    ans = 0
    if day > 31:
        day = 31
    for _ in range(day):
        hou = math.ceil(float(input()))
        if hou > 24:
            hou = 24
        ans += hou*won
    print(ans)
main()
