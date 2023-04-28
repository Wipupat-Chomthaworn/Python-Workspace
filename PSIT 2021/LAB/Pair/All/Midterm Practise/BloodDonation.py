"""BloodDonation"""

def main():
    """main"""
    age = int(input())
    weight = int(input())
    many = int(input())
    ans = False
    per = False
    if age == 17:
        per = input()
        ans = (weight >= 45) and per == "True"
    elif  many < 1 and age > 55:
        if age >= 60 and age <= 70:
            per = input()
        ans = False
    elif 17 < age < 60:
        ans = (weight >= 45)
    elif age >= 60 and age <= 70:
        per = input()
        ans = (weight >= 45) and per == "True"
    if ans:
        print('Yes')
    else:
        print('No')
main()
