from accounts import Accounts
from passwords import Password


def create_account(first_name, last_name, user_name, password):
    accounts = Accounts('dennis', 'Kamau', 'DK-denno', '1234567890')
    return account


def save_account(accounts):
    accounts.save_account()


def delete_account(accounts):
    accounts.delete_account()


def find_accounts(user_name):
    return Accounts.find_by_user_name(user_name)


def isexist(username):
    return Accounts.account_exists(user_name)


def display_accounts():
    return Accounts.display_accounts()


def create_page(page, password):
    passwords = Password('facebook', '12345')
    return passwords


def save_page(passwords):
    passwords.save_page()


def delete_page(passwords):
    passwords.delete_page()


def display_pages():
    return Password.display_page()


def main():
    print('WELCOME TO PASSLOCK')
    print('Use the following numbers to pick their corresponding values')
    print(" 1) LOGIN \n 2) SIGN UP \n 3) ABOUT PASSLOCK \n")

    choice = int(input())
    if choice == 1:
        print('Enter username')
        username = input()
        print('Enter passoword')
        password = input()

        print(f'Welcome {username}, Use the following numbers to select their corresponding values')
        print(' 1) Save new password \n 2) Delete password \n 3) Display saved passwords ')

        log_choice = int(input())
        if log_choice == 1:
            print('New page')
            print('*'*100)

            print('Page name')
            page = input()

            print('password')
            password = input()

            #


if __name__ == '__main__':
    main()
