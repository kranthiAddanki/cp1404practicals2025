MENU = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"

def main():

    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(print_result(score))
        elif choice == "S":
            print(print_astrisks(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Thanks")


def get_valid_score():
    score = int(input("Enter score: "))
    return score


def print_result(score):
    if score < 0 or score > 100:
        return "Enter a valid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


def print_astrisks(score):
    return "*" * score

main()
