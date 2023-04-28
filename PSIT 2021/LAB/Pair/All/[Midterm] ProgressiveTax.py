"""main"""
def main():
    """main"""
    income = int(input())
    # print(type(near))
    # print(near, near2)
    tax = 0
    # a1 = income > 150000

    if income > 4000000:
        tax += (income-4000000)*35/100
        income -= income-4000000
    if income > 2000000 and income <= 4000000:
        tax += (income-2000000)*30/100
        income -= income-2000000
    if income > 1000000 and income <= 2000000:
        tax += (income-1000000)*25/100
        income -= income-1000000
    if income > 750000 and income <= 1000000:
        tax += (income-750000)*20/100
        income -= income-750000
    if income > 500000 and income <= 750000:
        tax += (income-500000)*15/100
        income -= income-500000
    if income > 300000 and income <= 500000:
        tax += (income-300000)*10/100
        income -= income-300000
    if income > 150000 and income <= 300000:
        tax += (income-150000)*5/100
        income -= income-150000
    print(int(tax))
main()
