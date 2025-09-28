"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
# version_1
# def main():
#
#     score = float(input("Enter score: "))
#     check_result(score)
#
#
# def check_result(score):
#     if score < 0 or score > 100:
#         print("Enter a valid score")
#     elif score >= 90:
#         print("excellent")
#     elif score >= 50:
#         print("pass")
#     else:
#         print("bad")
#
# main()


def main():
    score = float(input("Enter score: "))
    print(check_result(score))


def check_result(score):
    if score < 0 or score > 100:
        return "Enter a valid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


main()

