# """WPM"""
# def adut(wpm):
#     """made for adult"""
#     # print(26 <= wpm <= 35)
#     if wpm < 26:
#         print('Very Slow')
#     elif 26 <= wpm <= 35:
#         print('Slow/Beginner')
#     elif 36 <= wpm <= 45:
#         print('Intermidate/Average')
#     elif 46 <= wpm <= 65:
#         print('Fast/Advanced')
#     elif 66 <= wpm <= 80:
#         print('Very Fast')
#     elif wpm > 80:
#         print('Insane')
#     else:
#         print("Very Slow")
# def main():
#     """main"""
#     age = input()
#     wpm = int(input())
#     if age == 'Kids':
#         if wpm < 11:
#             print('Very Slow')
#         elif 11 <= wpm <= 20:
#             print('Slow')
#         elif 21 <= wpm <= 30:
#             print('Average')
#         elif 31 <= wpm <= 40:
#             print('Fast')
#         elif wpm > 40:
#             print('Very Fast')
#     else:
#         adut(wpm)
# main()
"""WPM"""
def adut(wpm):
    """made for adult"""
    if wpm < 26:
        print('Very Slow')
    elif 26 <= wpm <= 35:
        print('Slow/Beginner')
    elif 36 <= wpm <= 45:
        print('Intermediate/Average')
    elif 46 <= wpm <= 65:
        print('Fast/Advanced')
    elif 66 <= wpm <= 80:
        print('Very Fast')
    elif wpm > 80:
        print('Insane')
def main():
    """main function"""
    age = input()
    wpm = int(input())
    if age == 'Kids':
        if wpm < 11:
            print('Very Slow')
        elif 11 <= wpm <= 20:
            print('Slow')
        elif 21 <= wpm <= 30:
            print('Average')
        elif 31 <= wpm <= 40:
            print('Fast')
        elif wpm > 40:
            print('Very Fast')
    if age == 'Adults':
        adut(wpm)
main()
