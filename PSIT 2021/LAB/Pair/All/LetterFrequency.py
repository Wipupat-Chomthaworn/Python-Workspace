"""LetterFrequency"""

def main():
    """LetterFrequency"""
    st1, few = str(input()), ["", 0]
    for code in range(ord('a'), ord('z') + 1):
        if st1.count(chr(code)) > int(few[1]):
            few = [chr(code), st1.count(chr(code))]
    print(few[0])
main()
