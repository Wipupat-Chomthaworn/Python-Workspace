"""Hamming"""

def main():
    """main func"""
    var = input()
    var2 = input()
    count = 0
    for i in range(len(var)):
        if var[i] != var2[i]:
            count += 1
    print(count)

main()
