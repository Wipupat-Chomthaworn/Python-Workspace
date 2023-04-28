'''วิถีหมอลำ'''
def main():
    '''ab'''
    point = 0
    bonus = 0
    num = int(input())
    for _ in range(num):
        game = int(input())
        player = int(input())
        if game == player:
            bonus += 1
            point += bonus
        else:
            bonus = 0
            point -= 1
    print("%d Point"%(point))
main()
