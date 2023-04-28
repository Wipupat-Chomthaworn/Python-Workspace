"""Future Message"""
def main():
    """ab"""
    var = input()
    if var.isnumeric():
        print("Number")
    elif var.isupper():
        print("Uppercase")
    elif var.islower():
        print("Lowercase")
    elif var.istitle():
        print("Title")
    elif var.isspace():
        print("Space")
    else:
        print("Other")
main()
