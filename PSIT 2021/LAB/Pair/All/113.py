"""113"""
def main():
    """main"""
    var = input()
    while True:
        if var.count("113") < 1:
            break
        var = var.replace("113", "")
    print(var)
main()
