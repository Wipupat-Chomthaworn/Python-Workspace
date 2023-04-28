"""Shark"""
def main():
    """main"""
    var = input().upper()
    shallow = ["BULL SHARK"]
    twic = ["CHAIN CATSHARK", "GREAT WHITE SHARK", \
        "GUMMY SHARK", "BLUE SHARK", "MAKO SHARK"]
    midn = ["FRILLED SHARK", "GOBLIN SHARK", "SIXGILL SHARK", \
        "GREENLAND SHARK", "COOKIECUTTER SHARK"]
    abby = ["MEGAMOUTH SHARK"]
    if var in shallow:
        print("THE SHALLOW ZONE")
    elif var in twic:
        print("THE TWILIGHT ZONE")
    elif var in midn:
        print("THE MIDNIGHT ZONE")
    elif var in abby:
        print("THE ABYSSAL ZONE")
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
main()
