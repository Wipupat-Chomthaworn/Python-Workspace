"""print II"""

def main():
    """printing II"""
    inp = input()
    inp2 = input()#แปลงข้อความ1เป็นข้อความ2
    print(inp)
    for i in range(max(len(inp), len(inp2))):
        print(inp2[:i+1]+inp[i+1:])
main()
