"""Area"""

def main():
    """main function"""
    count = 0
    for _ in range(int(input())):
        var = input()
        for i in var:
            if i != ' ':
                count += 1
    print(count)
main()
# 4
# #######
# ##   ##
# #$   %#
# #######
