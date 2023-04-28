"""Sequence II"""
def main():
    """main func"""
    var = int(input())
    for i in range(var):
        for _ in range(var):
            i += var
            print(i-var, end=" ")
        print()
main()
