"""Future Message"""
import math
def truncate(num, demical):
    """2 demical"""
    return math.floor(num * 10 ** demical) / 10 ** demical
def main():
    """ab"""
    var = int(input())
    keep = 0
    score = 0
    def grade(num):
        '''grade'''
        if 95 <= num <= 100:
            gra = 4
        elif 90 <= num < 95:
            gra = 3.5
        elif 85 <= num < 90:
            gra = 3
        elif 80 <= num < 85:
            gra = 2.5
        elif 75 <= num < 80:
            gra = 2
        elif 70 <= num < 75:
            gra = 1.5
        elif 65 <= num < 70:
            gra = 1
        elif 60 <= num < 65:
            gra = 0.5
        elif 0 <= num < 60:
            gra = 0
        return gra
    for _ in range(1, var+1):
        score = grade(float(input()))
        keep += score
    avg = keep / var
    if avg == int(avg):
        print("%.2f" %avg)
    else:
        print("%.2f" %truncate(avg, 2))
main()
