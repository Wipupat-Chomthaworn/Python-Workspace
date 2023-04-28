"""BrickBridge"""
def main():
    """BrickBridge"""
    smallbrick = int(input())
    bigbrick = int(input())
    goal = int(input())
    result = 0
    while goal != result:
        result = result + 5
        bigbrick = bigbrick - 1
        if bigbrick < 0:
            if smallbrick+result-5 == goal:
                print(smallbrick)
                break
            else:
                print(-1)
                break
        elif goal - result < 5:
            goal = goal % 5
            if smallbrick >= goal:
                print(goal)
                break
            else:
                print(-1)
                break
        elif smallbrick+bigbrick*5 == goal:
            print(smallbrick)
            break
main()
# 15
# 2
# 30
# 15
# and smallbrick + result < goal
# 10
# 2
# 20
# -1
