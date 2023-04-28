"""Inflation"""
def main():
    '''main'''
    var = float(input())
    years = int(input())
    var = int(var*100)
    for _ in range(years):
        var += var*381//10000
    print("%d.%02d" %(var//100, var%100))
main()
