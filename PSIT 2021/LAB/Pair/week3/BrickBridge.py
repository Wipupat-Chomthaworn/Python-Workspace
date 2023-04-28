"""BrickBridge"""
def main():
    """docstring"""
    small = int(input())
    large = int(input())
    goal = int(input())

    large_need = goal // 5
    remain = goal % 5

    if large >= large_need:
        if remain == 0:
            return 0
        if small >= remain:
            return remain
        return -1
    remain = goal - large*5
    if small >= remain:
        return remain
    return -1

print(main())
