'''ช่วยพี่ที่ช่วยครูตรวจงานหน่อย V.1'''
def main():
    '''ab'''
    corr = input()
    stu = input()
    point = 10
    finans = ''
    for i in range(len(corr)):
        if corr[i].lower() != stu[i].lower():
            point -= 1
            finans += '(%s)'%stu[i]
        else:
            finans += '%s'%stu[i]
    print(finans)
    if point <= 0:
        print('0/10 (%d)'%(point-10))
    else:
        print('%d/10 (-%d)'%(point, 10-point))
main()
