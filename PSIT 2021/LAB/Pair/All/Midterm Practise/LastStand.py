"""main"""
import json
def main():
    """main"""
    list1 = json.loads(input())
    for i in list1:
        print(str(i)[-1])
main()
