"""เป่ายิงฉุบฉบับชาวสงขลา"""
def main():
    '''ab'''
    gam = (input()).lower()
    gam2 = (input()).lower()
    print('Numphung'*(gam == 'bird' and gam2 == 'stone')+\
        ('Sui'*(gam == 'stone' and gam2 == 'bird')+\
            ('Numphung'*(gam == 'stone' and gam2 == 'water')+\
                ('Sui'*(gam == 'water' and gam2 == 'stone')+\
                    ('Numphung'*(gam == 'water' and gam2 == 'bird')+\
                        ('Sui'*(gam == 'bird' and gam2 == 'water')+\
                            ('Draw'*(gam == gam2))))))))
main()
#ค้อน=stone waterกระดาษ bird กรรไกร
