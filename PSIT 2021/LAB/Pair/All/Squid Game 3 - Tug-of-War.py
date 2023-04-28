"""main"""
def main():
    """main"""
    ans1 = 0
    ans2 = 0
    for _ in range(10):
        hou = round(float(input()))
        ans1 += hou
    for _ in range(10):
        hou = round(float(input()))
        ans2 += hou
    if ans1 > ans2:
        print('B')
    elif ans1 < ans2:
        print('A')
    elif ans1 == ans2:
        print('AB')
main()
