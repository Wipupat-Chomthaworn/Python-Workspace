"""asdasdw"""
def gcd(first, second):
    """Create the gcd of two positive integers."""
    while second != 0:
        first, second = second, first%second
    return first
def is_coprime(first, second):
    """co_primer"""
    if gcd(first, second) == 1:
        return "YES"
    return "NO"
def main():
    """aaaa"""
    first = int(input())
    second = int(input())
    print(is_coprime(first, second))
    print(gcd(first, second))
main()
