"""main"""
def main():
    """main"""
    var = int(input())
    this = {}
    # num = 0
    # avg = 0
    # som = 0
    # keep = ''
    for i in range(var):
        var1 = input()
        this[var1[0:9]] = var1[9:]
        print(this.get([var1[0:9]]))
        # if i == 0:
        #     keep = var1[9:]
        # num += 1
        # som += var1[9:]
        # avg = som / num

main()
