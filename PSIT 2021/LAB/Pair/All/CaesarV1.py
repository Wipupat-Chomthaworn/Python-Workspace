"""CaesarV1"""
def main():
    """CaesarV1"""
    num = int(input())
    text = input()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + num - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + num - 97) % 26 + 97)
        else:
            result += char
    print(result)
main()
