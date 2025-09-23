
def main():
    get_password()


def get_password():
    password = input("Enter your password: ")
    while len(password) < 6:
        print("Invalid password")
        password = input("Enter your password:")
    print_astrisks(password)


def print_astrisks(password):
    print("*" * len(password))


main()
