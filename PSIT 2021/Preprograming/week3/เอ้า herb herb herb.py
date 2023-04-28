"""เอ้า herb herb herb"""
def main():
    '''ab'''
    mon1 = int(input())
    mon2 = int(input())
    mon3 = int(input())
    mon4 = int(input())
    mon5 = int(input())
    mon6 = int(input())
    mon7 = int(input())
    mon8 = int(input())
    mon9 = int(input())
    mon10 = int(input())
    ans = 0
    if mon1 <= 100:
        ans += mon1
    if mon2 <= 100:
        ans += mon2
    if mon3 <= 100:
        ans += mon3
    if mon4 <= 100:
        ans += mon4
    if mon5 <= 100:
        ans += mon5
    if mon6 <= 100:
        ans += mon6
    if mon7 <= 100:
        ans += mon7
    if mon8 <= 100:
        ans += mon8
    if mon9 <= 100:
        ans += mon9
    if mon10 <= 100:
        ans += mon10
    if ans == 420:
        print('herb')
    else:
        print(ans)
main()
