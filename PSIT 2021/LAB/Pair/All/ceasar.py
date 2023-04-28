"""realceasar"""
def caesar(shift, text):
    """aasdasd"""
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper() == True:
            result += chr((ord(char) + shift - 65)%26 + 65)
        elif char.islower() == True:
            result += chr((ord(char) + shift - 97)%26 + 97)
        else:
            result += char
    return result
def main():
    """main"""
    shift = int(input())
    text = input()

    print(caesar(shift, text))
main()
