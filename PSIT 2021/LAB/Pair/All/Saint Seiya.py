"""Saint Seiya"""
def main(sec, punch):
    """Saint Seiya"""
    real = 0
    for i in range(2, sec+1, 2):
        if real < punch:
            if i%6 == 0:
                real += 1
            elif i%2 == 0:
                real += 165
        else:
            real += (sec+1-i)*12# 1 รอบ cash หายไป
            break
    print(real)
main(int(input()), int(input()))
