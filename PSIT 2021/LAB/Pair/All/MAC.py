"""MAC(Midter,"""
def mac():
    """MAC"""
    txt = input()
    if not (len(txt) == 17 or len(txt) == 14):
        return print("ERROR")
    charater = "ABCDEFabcdef1234567890.:-"
    for i in txt:
        if i not in charater:
            return print("ERROR")


        #check simbol
    if not (txt.count("-") == 5 or txt.count(":") == 5 or txt.count(".") == 2):
        return print("ERROR")
        #isvalid

    if txt[2] == "-" and txt[5] == "-" and \
        txt[8] == "-" and txt[11] == "-" and txt[14] == "-":
        print("VALID 1")
    elif txt[2] == ":" and txt[5] == ":" and \
        txt[8] == ":" and txt[11] == ":" and txt[14] == ":":
        print("VALID 2")
    elif txt[4] == "." and txt[9] == "." and \
        txt[:4].isalnum() and txt[5:9].isalnum() and\
             txt[10:].isalnum():
        print("VALID 3")
    else:
        print("ERROR")
mac()
