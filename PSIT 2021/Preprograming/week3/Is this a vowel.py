"""Is this a vowel?"""
def main():
    '''ab'''
    sol = (input()).upper()
    if sol in ('A', 'E', 'I', 'O', 'U'):
        print('%s is vowel.'%(sol))
    else:
        print('%s is consonant.'%(sol))
main()

# """Is this a vowel?"""
# def main():
#     """Is this a vowel?"""
#     word = input()
#     big_word = word.upper()
#     fix_word = ord(big_word)
#     if fix_word == 65:
#         print("%s is vowel."%big_word)
#     elif fix_word == 69:
#         print("%s is vowel."%big_word)
#     elif fix_word == 73:
#         print("%s is vowel."%big_word)
#     elif fix_word == 79:
#         print("%s is vowel."%big_word)
#     elif fix_word == 85:
#         print("%s is vowel."%big_word)
#     else:
#         print("%s is consonant."%big_word)
# main()

# """Is this a vowel?"""
# def main():
#     """อินพุตตัวใหญ่เท่านั้น"""
#     txt = input().upper()
#     txt2 = "AEIOU"
#     txt3 = "BCDFGHJKLMNPQRSTVWXYZ"
#     if txt2.find(txt) >= 0:
#         print("% s is vowel." %txt)
#     elif txt3.find(txt) >= 0:
#         print("%s is consonant." %txt)
# main()

# """กลับมาได้มั้ยฉันยอมได้ทุกอย่าง"""
# def main():
#     """ขอเพียงแค่พอได้มีทางให้กลับมารักกันนน"""
#     num = input()
#     num1 = num.replace("E", "A").replace("I", "A").replace("O", "A").replace("U", "A")
#     if num1 == "A":
#         print(num+" is vowel.")
#     else:
#         print(num+" is consonant.")
# main()