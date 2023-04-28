"""Harshad"""
def main():
    """Harshaddd"""
    keep = 0
    for _ in range(10):
        var = abs(int(input()))
        for i in str(var):
            keep += abs(float(i))
        if keep == 0:
            print('No')
        elif int(int(var)%keep) == 0:
            print('Yes')
        else:
            print('No')
        keep = 0
main()
