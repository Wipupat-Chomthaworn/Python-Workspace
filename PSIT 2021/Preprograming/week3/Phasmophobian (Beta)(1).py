"""Phasmophobian (Beta)"""
def main():
    '''ab'''
    evil = (input()).lower()
    evil2 = (input()).lower()
    def two():
        '''ab'''
        if evil == 'ghost writing':
            print("I think Yurei and Revenant, so one of them is the answer!!!.")
        elif evil == 'spirit box':
            print("I think Wraith and Hantu, so one of them is the answer!!!.")
        elif evil == 'fingerprints':
            print("I think Revenant and Hantu, so one of them is the answer!!!.")
        elif evil == 'freezing temperature':
            print("I think Wraith and Banshee, so one of them is the answer!!!.")
        elif evil == 'emf level 5':
            print("I think Phantom and Banshee, so one of them is the answer!!!.")
        elif evil == 'ghost orb':
            print("I think Phantom and Yurei, so one of them is the answer!!!.")
    def twoplus():
        '''ab'''
        if evil2 == 'ghost writing':
            print("I think Yurei and Revenant, so one of them is the answer!!!.")
        elif evil2 == 'spirit box':
            print("I think Wraith and Hantu, so one of them is the answer!!!.")
        elif evil2 == 'fingerprints':
            print("I think Revenant and Hantu, so one of them is the answer!!!.")
        elif evil2 == 'freezing temperature':
            print("I think Wraith and Banshee, so one of them is the answer!!!.")
        elif evil2 == 'emf level 5':
            print("I think Phantom and Banshee, so one of them is the answer!!!.")
        elif evil2 == 'ghost orb':
            print("I think Phantom and Yurei, so one of them is the answer!!!.")
    def findg():
        '''ab'''
        if evil == ('spirit box') and evil2 == ('freezing temperature') or\
             evil2 == ('spirit box') and evil == ('freezing temperature'):
            allevil = ''
            allevil = 'Wraith'
            print("I think %s is the answer!!!."%(allevil))
        if evil == ('emf level 5') and evil2 == ('ghost orb') or \
            evil2 == ('emf level 5') and evil == ('ghost orb'):
            allevil = ''
            allevil = 'Phantom'
            print("I think %s is the answer!!!."%(allevil))
        if evil == ('ghost writing') and evil2 == ('ghost orb') or \
            evil2 == ('ghost writing') and evil == ('ghost orb'):
            allevil = ''
            allevil = 'Yurei'
            print("I think %s is the answer!!!."%(allevil))
        if evil == ('freezing temperature') and evil2 == ('emf level 5') or \
            evil2 == ('freezing temperature') and evil == ('emf level 5'):
            allevil = ''
            allevil = 'Banshee'
            print("I think %s is the answer!!!."%(allevil))
        if evil == ('ghost writing') and evil2 == ('fingerprints') or \
            evil2 == ('ghost writing') and evil == ('fingerprints'):
            allevil = ''
            allevil = 'Revenant'
            print("I think %s is the answer!!!."%(allevil))
        if evil == ('spirit box') and evil2 == ('fingerprints') or \
            evil2 == ('spirit box') and evil == ('fingerprints'):
            allevil = ''
            allevil = 'Hantu'
            print("I think %s is the answer!!!."%(allevil))
    if evil2 == 'no evidence' and evil != 'no evidence':
        two()
    elif evil == 'no evidence' and evil2 != 'no evidence':
        twoplus()
    elif evil == 'no evidence' and evil2 == 'no evidence':
        print('I think Wraith, Phantom, Yurei, Banshee, Revenant and\
 Hantu, so one of them is the answer!!!.')
    elif evil2 == 'no evidence' or evil2 == evil:
        two()
    else:
        findg()
main()
# (('Wraith')*(evil == 'spirit box' and evil2 == 'freezing temperature')\
#                  +'Phantom'*(evil2 == 'ghost orb'and evil=='emf level 5'\
#                      +'Yurei'*(evil2 == 'ghost orb'and evil=='ghost writing'\
#                          +'Banshee'*(evil == 'freezing temperature'and evil2=='emf level 5'\
#                              +'Revenant'*(evil2 == 'fingerprints 'and evil=='ghost writing')\
#                                  +'Hantu'*(evil2 == 'fingerprints'and evil=='spirit box')))))
# elif evil2 == 'no evidence':
#             if evil.count('spirit box') >=1 or evil2.count('freezing temperature')>=1:
#                 allevil = 'Wraith'
#             elif evil2.count('ghost orb') >=1 or evil.count('emf level 5') >=1:
#                 allevil = 'Phantom'
#             elif evil2.count('ghost orb') >=1 or evil.count('ghost writing')>=1:
#                 allevil = 'Yurei'
#             elif evil.count('freezing temperature')>=1 or evil2.count('emf level 5')>=1:
#                 allevil = 'Banshee'
#             elif evil2.count('fingerprints') >=1 or evil.count('ghost writing')>=1:
#                 allevil = 'Revenant'
#             elif evil2.count('fingerprints') >=1 or evil.count('spirit box')>=1:
#                 allevil = 'Hantu'
#             if evil2 != 'no evidence':
#                 print("I think %s is the answer!!!."%(allevil))
#             elif evil2 == 'no evidence':
#                 print('I think %s and %s, so one of them is the answer!!!.'%(allevil, sol))

            # def findg():
            # if evil.count('spirit box') >=1 or evil2.count('freezing temperature')>=1:
            #     allevil = 'Wraith'
            #     allevil2 = 'Banshee'*bool(evil2.count('freezing temperature')>=1)
            # if evil.count('emf level 5')>=1 or evil2.count('ghost orb')>=1:
            #     allevil = 'Phantom'
            #     allevil2 = 'Banshee'*bool(evil2.count('emf level 5')>=1)
            # if evil.count('ghost writing')>=1 or evil2.count('ghost orb')>=1:
            #     allevil = 'Yurei'
            #     allevil2 = 'Phantom'*bool(evil2.count('ghost orb')>=1)
            # if evil.count('freezing temperature')>=1 or evil2.count('emf level 5')>=1:
            #     allevil = 'Banshee'
            #     allevil2 = 'Wraith'*bool(evil2.count('freezing temperature')>=1)
            # if evil.count('ghost writing')>=1 or evil2.count('fingerprints')>=1:
            #     allevil = 'Revenant'
            #     allevil2 = 'Yurei'*bool(evil2.count('ghost orb')>=1)
            # if  evil2.count('ghost orb')>=1: allevil2 = 'Yurei'
            # if evil.count('spirit box')>=1 or evil2.count('fingerprints')>=1:
            #     allevil = 'Hantu'
            # if allevil2.count('fingerprints')>=1:allevil2 = 'Revenant'
            # if evil2 != 'no evidence':
            #     print("I think %s is the answer!!!."%(allevil))
            # elif evil2 == 'no evidence':
            #     print('I think %s and %s, so one of them is the answer!!!.'%(allevil2, allevil))
'''"""Ghost"""
def out(cha):
    """Out function"""
    print("I think "+cha+" is the answer!!!.")
def out2(ghost1, ghost2):
    """Out2 function"""
    print("I think %s and %s, so one of them is the answer!!!."%(ghost1, ghost2))
def out3(num1, num2):
    """OUT3 function"""
    if num1 == "no evidence" and num2 == "no evidence":
        print("I think Wraith, Phantom, Yurei, Banshee, Revenant \
and Hantu, so one of them is the answer!!!.")
def main():
    """Function"""
    num1 = input().lower()
    num2 = input().lower()
    cha1 = "ghost writing"
    cha2 = "spirit box"
    cha3 = "fingerprints"
    cha4 = "freezing temperature"
    cha5 = "emf level 5"
    cha6 = "ghost orb"
    if (num1 == cha2 and num2 == cha4) or \
        num1 == cha4 and num2 == cha2:
        out("Wraith")
    elif (num1 == cha5 and num2 == cha6) or \
        (num1 == cha6 and num2 == cha5):
        out("Phantom")
    elif (num1 == cha1 and num2 == cha6) or \
        (num1 == cha6 and num2 == cha1):
        out("Yurei")
    elif (num1 == cha4 and num2 == cha5) or \
        (num1 == cha5 and num2 == cha4):
        out("Banshee")
    elif (num1 == cha1 and num2 == cha3) or \
        (num1 == cha3 and num2 == cha1):
        out("Revenant")
    elif (num1 == cha2 and num2 == cha3) or \
        (num1 == cha3 and num2 == cha2):
        out("Hantu")
    elif (num1 == cha1 and num2 == "no evidence") or \
        (num1 == "no evidence" and num2 == cha1) or \
        (num1 == cha1 and num2 == cha1):
        out2("Yurei", "Revenant")
    elif (num1 == cha2 and num2 == "no evidence") or \
        (num1 == "no evidence" and num2 == cha2) or \
        (num1 == cha2 and num2 == cha2):
        out2("Wraith", "Hantu")
    elif (num1 == cha3 and num2 == "no evidence") or \
        (num1 == "no evidence" and num2 == cha3) or \
        (num1 == cha3 and num2 == cha3):
        out2("Revenant", "Hantu")
    elif (num1 == cha4 and num2 == "no evidence") or \
        (num1 == "no evidence" and num2 == cha4) or \
        (num1 == cha4 and num2 == cha4):
        out2("Wraith", "Banshee")
    elif (num1 == cha5 and num2 == "no evidence") or \
        (num1 == "no evidence" and num2 == cha5) or \
        (num1 == cha5 and num2 == cha5):
        out2("Phantom", "Banshee")
    elif (num1 == cha6 and num2 == "no evidence") or \
        (num1 == "no evidence" and num2 == cha6) or \
        (num1 == cha6 and num2 == cha6):
        out2("Phantom", "Yurei")
    out3(num1, num2)
main()'''
