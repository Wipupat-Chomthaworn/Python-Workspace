"""Digit v3"""
def main():
    """main"""
    var = input().split(" ")
    ans = 0
    keep = 0
    dict1 = {
        "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,\
            "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,\
                "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30,\
                    "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, \
                        "hundred":100, 'thousand':1000, 'one thousand':1000, 'one hundred':100}
    for i in var:
        if i == "hundred":
            keep *= 100
            ans += keep
            keep = 0
            if ans == 0:
                ans = 100
        elif i == "thousand":
            keep *= 1000
            ans += keep
            keep = 0
            if ans == 0:
                ans = 1000
        else:
            keep += dict1[i]
    ans += keep
    print(ans)
main()
