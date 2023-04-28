"""Future Message"""
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
    avg = str(keep/var)
    if len(avg) <= 4:
        print('%0-3s'%avg[0:4], end='')
        print(0)
    else:
        print('%0-3s'%avg[0:4])
main()
