"""main"""
import json
def main():
    """main"""
    var = json.loads(input())
    ans = []
    for i in var:
        if i %2 == 0:
            ans.append(i)
            print(i)
    if len(ans) == 0:
        print('Nope')
main()
