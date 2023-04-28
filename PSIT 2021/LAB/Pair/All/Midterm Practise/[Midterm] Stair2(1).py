"""main"""
import math
def main():
    """main"""
    foot = int(input())
    many = int(input())
    keep = 0
    for i in range(many):
        stair = int(input())
        keep += stair
    # print(keep)
    ans = keep / foot
    if ans != math.floor(ans):
        print("NO")
    else:
        print(ans)
main()
