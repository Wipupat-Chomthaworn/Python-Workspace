# """main"""
# import json
# def main():
#     """main"""
#     data = json.loads(input())
#     fil = float(input())
#     lkey = list(data.keys())
#     lval = list(data.values())
#     ans = {}
#     for i in lval:
#         if float(i) >= fil:
#             ans[lkey[lval.index(i)]] = i
#     anskey = sorted(list(ans.keys()))
#     if len(anskey) == 0:
#         print('Nope')
#     else:
#         for i in anskey:
#             print("%s\t%.2f" %(i, ans[i]))
# main()
"""Filter"""
import json
def main():
    """Filter"""
    data = json.loads(input())
    list1 = []
    fil = float(input())

    for key in data:
        if data[key] >= fil:
            list1.append('%s %.2f' %(key, float(data[key])))
        else:
            pass
    list1.sort()
    if len(list1) == 0:
        print("Nope")
    else:
        for i in list1:
            print("%s\t%.2f" %(i[0:8], float(i[9::])))
main()
