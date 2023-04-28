"""main"""
def main():
    """main"""
    var = input()
    var2 = input()
    var3 = input()
    finger = int(input())
    potato = var2[:finger].count(')')
    result = var2.replace(')', " ", potato).count(')')
    # print(many)
    # print("")
    print(potato)
    if result <= 0:
        print('None.')
    else:
        print('There are still some left.')
    print(var)
    print(var2.replace(')', " ", potato))
    print(var3)
main()
# """in"""
# def main():
#     """placeholder"""
#     can1, content, can2 = input(), input(), input()
#     ability = int(input())
#     new_content = content[ability:len(content)+1].rjust(len(can1)+1, ' ')
#     gotten = abs(new_content.count(')') - content.count(')'))
#     print(gotten)
#     if content.count(')') - gotten <= 0:
#         print('None.')
#     else:
#         print('There are still some left.')
#     print(can1)
#     print(new_content)
#     print(can2)
# main()
