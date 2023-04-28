'''เกมทายใจ'''
def main():
    '''ab'''
    num = int(input())
    many = int(input())
    for i in range(many):
        game = int(input())
        if game == num:
            print('Yes! It is %d.'%(num))
            break
        else:
            if many-1 == i:
                print("No more chances. You lose.")
main()
# """เกมทายใจ"""
 
# def main():
#     """fdocstr"""
#     num = int(input())
#     chance = int(input())
#     for _ in range(chance):
#         guess = int(input())
#         if guess == num:
#             break
#     if guess == num:
#         print('Yes! It is %d.' %num)
#     else:
#         print('No more chances. You lose.')
# main()
