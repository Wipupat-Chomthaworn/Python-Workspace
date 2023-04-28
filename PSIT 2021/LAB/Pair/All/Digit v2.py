# """Digit v2"""
# def main():
#     """main"""
#     var = input().split(" ")
#     ans = 0
#     dict1 = {
#         "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
#         "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
#         "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30,
#         "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, \
#         "hundred":100, 'thousand':1000}
#     for i in var:
#         if i == "hundred":
#             ans *= 100
#             if ans == 0:
#                 ans = 100
#         elif i == "thousand":
#             ans *= 1000
#             if ans == 0:
#                 ans = 1000
#         else:
#             ans += dict1[i]
#         # print(ans)

#     print(len(str(ans)))
# main()
"""Test"""

def main():
    """main func"""
    var = input().split()
    units = {
        "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
        "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
        "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30,
        "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, \
        "hundred":100, 'thousand':1000}

    num = 0
    for i in var:
        num += int(units["%s" % (i)])
    print(len(str(num)))

main()
