"""Classify"""
def issameyear(year, compare):
    """return year"""
    if year == compare:#if 64 == 64
        year = '--'
    return year
def main():
    """Classify"""
    list1 = []
    dict1 = {}
    compare = 0
    year = 0
    while True:
        var = str(input())
        if var == "END":
            break
        list1.append(int(str(var)[:4]))
        list1 = sorted(list1)

    for i in list1:
        dict1[i] = 0

    for i in list1:
        dict1[i] = dict1[i] + 1#dictให้เป็นชั้นปี

    for key, value in dict1.items():
        year = str(key)[0:2]#ex "64" from 64000000
        year = issameyear(year, compare)
        compare = str(key)[0:2]
        print(year, int(str(key)[2:4]), value)
main()
