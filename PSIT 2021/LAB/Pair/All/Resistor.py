"""main"""
def main():
    """main"""
    dct = {'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4, 'Green': 5,\
         'Blue': 6, 'Purple': 7, "Grey": 8, 'White': 9}
    dct2 = {'Black': 1, 'Brown': 10, 'Red': 100, 'Orange': 1000,\
         'Yellow': 10000, 'Green': 100000,\
         'Blue': 1000000, 'Purple': 10000000,\
              "Gold": 0.1, 'Silver': 0.01}
    per = {'Brown': 1, 'Red': 2, 'Green': 0.5,\
         'Blue': 0.25, 'Purple': 0.1, "Grey": 0.05\
             , "Gold": 5, 'Silver': 10}
    ans = ''
    low = 0
    upp = 0
    che = 'p'
    for i in range(4):
        var = input()
        if i == 0 or i == 1:
            if var not in dct:
                if che != 'e':
                    print('Error')
                che = "e"
                continue
            ans += str(dct[var])
        elif i == 2:
            if var not in dct2:
                che = "e"
                if che != 'e':
                    print('Error')
                continue
            ans = int(ans) * dct2[var]
        elif i == 3:
            if var not in per:
                che = "e"
                if che != 'e':
                    print('Error')
                continue
            low = int(ans) - (int(ans)*per[var])/100
            upp = int(ans) + (int(ans)*per[var])/100
        # print(ans)
    if che != 'e':
        print("%.4f"%low)
        print("%.4f"%upp)

main()
