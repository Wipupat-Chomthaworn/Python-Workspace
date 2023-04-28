'''The world!!!'''
def main():
    '''ab'''
    allenemy = 0
    urx = int(input())
    ury = int(input())
    enemy = int(input())
    for _ in range(enemy):
        enemyx = int(input())
        enemyy = int(input())
        a_to_me = (((urx-enemyx)**2)+(ury-enemyy)**2)**0.5
        if a_to_me <= 500:
            allenemy += 1
        # b_to_me = (((urx-b_x)**2)+(ury-b_y)**2)**0.5
    if allenemy == 1:
        print("You got 1 enemy in your area.")
    elif allenemy > 1:
        print('You got %d enemies in your area.'%(allenemy))
    else:
        print("Muda Muda Muda.")
main()
