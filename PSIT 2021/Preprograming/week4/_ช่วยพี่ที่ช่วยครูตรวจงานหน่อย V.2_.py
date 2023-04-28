'''ช่วยพี่ที่ช่วยครูตรวจงานหน่อย V.2'''
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
    for j in range(len(corr)):
        if corr[i].lower() + corr[j].lower() != stu[i].lower() + stu[j].lower():
            point -= 1
            finans += '(%s)'%(stu[i]+stu[j])
        elif corr[i].lower() != stu[i].lower():
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
