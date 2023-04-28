'''BMI'''
def main():
    '''ab'''
    def bmifinder():
        '''ab'''
        name = input()
        weight = float(input())
        height = float(input())/100
        print("%s's  BMI = %.2f" %(name, (weight/(height**2))))
    for _ in range(5):
        bmifinder()
main()
