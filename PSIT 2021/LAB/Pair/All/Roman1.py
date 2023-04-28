"""Aaa"""
def main():
    """Cal"""
    roman_1 = input()
    ro_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_1)):
        if i > 0 and ro_value[roman_1[i]] > ro_value[roman_1[i - 1]]:
            result += ro_value[roman_1[i]] - (2 * ro_value[roman_1[i - 1]])
        else:
            result += ro_value[roman_1[i]]
    print(result)
main()
