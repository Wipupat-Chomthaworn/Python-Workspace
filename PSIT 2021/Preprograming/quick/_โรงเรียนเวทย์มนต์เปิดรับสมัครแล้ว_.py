'''โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว'''
def main():
    '''ab'''
    nam = input()
    age = int(input())
    fem = input()
    hight = int(input())
    ans = ''
    fem2 = ''
    def jun():
        if age <= 15 and age >= 13:
            if fem.lower() == 'male':
                if hight >= 160:
                    ans = 'study in junior high school.'
                else:
                    ans = 'not join this school.'
            elif fem.lower() == 'female':
                if hight >= 155:
                    ans = 'study in junior high school.'
                else:
                    ans = 'not join this school.'
            else:
                ans = 'not join this school.'
        return ans
    def senior():
        if age >= 16 and age <= 18:
            if fem.lower() == 'male':
                if hight >= 170:
                    ans = 'senior high school.'
                else:
                    ans = 'not join this school.'
            elif fem.lower() == 'female':
                if hight >= 165:
                    ans = 'senior high school.'
                else:
                    ans = 'not join this school.'
            else:
                ans = 'not join this school.'
        return ans
    if age <= 15 and age >= 13:
        ans = jun()
    elif age >= 16 and age <= 18:
        ans = senior()
    if fem.lower() == 'male':
        fem2 = 'Mr.'
    elif fem.lower() == 'female':
        fem2 = "Miss"
    else:
        ans = 'not join this school.'
    print('%s %s Age: %d Height: %.2f'%(fem2, nam, age, hight))
    print('You can %s'%ans)
main()
