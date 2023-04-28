'''BMIAgain'''
def main():
    '''ab'''
    weight = int(input())
    height = (int(input())/100)**2
    bmi = weight/height
    if bmi >= 30:
        print('Obese')
    elif 25 <= bmi < 30:
        print('Overweight')
    elif 18.5 <= bmi < 25:
        print('Normal')
    elif bmi < 18.5:
        print('Underweight')
main()
