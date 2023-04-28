"""docstring"""
def main():
    """docstring"""
    allpot = float(input())
    first = float(input())
    rest = allpot - first
    if rest >= first:
        sec = first#จับเท่าหาที่ห่างสุด
        third = allpot - (first + sec)
    else:
        sec = rest
        third = 0
    if first -third > 2:
        print('Surprising')
    else:
        print('Not surprising')
main()
