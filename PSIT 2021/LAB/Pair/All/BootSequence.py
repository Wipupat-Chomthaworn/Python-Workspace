"""BootSequence"""
def main():
    """ab"""
    var = int(input())
    var2 = []
    for i in range(1, var+1):
        var2.append(i)
        var3 = str(var2)
    print(var3.replace('[', '').replace(']', '').replace(', ', '_'))
main()
