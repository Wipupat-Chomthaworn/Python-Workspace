"""What grade?"""
def main():
    '''ab'''
    human = int(float(input()))
    print("4.0"*(human >= 80)+\
        '3.5'*(75 <= human <= 79)+"3.0"*(70 <= human <= 74)+\
            "2.5"*(65 <= human <= 69)+"2.0"*(60 <= human <= 64)+\
                "1.5"*(55 <= human <= 59)+"1.0"*(50 <= human <= 54)+\
                    "0.0"*(human < 50))
main()
