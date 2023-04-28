"""What is it then?"""
def main():
    """ab"""
    txt = input()
    txt2 = "1234567890"
    txt3 = "AEIOUBCDFGHJKLMNPQRSTVWXYZabcdefghijklmnopqrstuvwxyz"
    if txt2.find(txt) >= 0:
        print("'%s' is numeric." %txt)
    elif txt3.find(txt) >= 0:
        print("'%s' is an alphabet."%txt)
    else:
        print("'%s' is not both an alphabet and numeric."%txt)
main()
