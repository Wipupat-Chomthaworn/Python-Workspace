""""PSIT"""
import re
def mani():
    """PSIT"""
    num = input()
    strings = re.sub('[^A-Za-z]+', ' ', num)
    strings = strings.split()
    for i in range(len(strings)):
        if len(strings[i]) > 6:
            print(strings[i], end=" ")
        else:
            pass

mani()
