"""print"""

def main():
    """printing"""
    inp = input()
    for i in range(len(inp)):
        print(inp[:i+1])
main()
