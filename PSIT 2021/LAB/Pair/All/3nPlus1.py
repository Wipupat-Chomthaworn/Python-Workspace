"""3nPlus1"""
def cal(num):
    """RRRR"""
    round_1 = 0
    want = num
    while True:
        if want == 1:
            break
        else:
            reuse = want
            if reuse % 2 == 0:
                want = 0
                want += reuse / 2
                round_1 += 1
            else:
                want = 0
                want += (reuse * 3) + 1
                round_1 += 1
    return round_1

def main():
    """DDDD"""
    round_re = []
    while True:
        num_1 = int(input())
        if num_1 == 0:
            break
        else:
            cal_1 = cal(num_1)
            round_re.append(cal_1+1)
    for i in range(len(round_re)):
        print(round_re[i])
main()
