"""main"""
def check(var, list1):
    """check"""
    for j in var:
        if not isinstance(j, list):
            list1.append(j)
        else:
            check(j, list1)
import json
def main():
    """main"""
    list1 = []
    var = json.loads(input())
    check(var, list1)
    list1.sort(reverse=True)
    print(list1)
main()
# """main"""
# import json
# list1 = []
# def check(var, list1):
#     """check"""
#     for j in var:
#         if not isinstance(j, list):
#             list1.append(j)
#         else:
#             check(j, list1)
#     list1.sort(reverse=True)
#     return list1
# print(check(json.loads(input()), list1))
