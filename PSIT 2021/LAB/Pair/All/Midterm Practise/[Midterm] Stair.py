"""main"""
def main():
    """main"""
    foot_stride = int(input())
    steps = int(input())
    big_step = 0
    step_count = 0
    too_big = False
    for _ in range(steps):
        each = int(input())
        if big_step + each > foot_stride:
            if each > foot_stride:
                too_big = True
                break

            else:
                step_count += 1
                big_step = each

        else:
            big_step += each
    if big_step <= foot_stride:
        step_count += 1

    if too_big == True:
        print('NO')
    else:
        print(step_count)
main()
