from accounts import Accounts
from passwords import Password


def create_account(first_name, last_name, user_name, password):
    accounts = Accounts('dennis', 'Kamau', 'DK-denno', '1234567890')
    return account


def save_account(accounts):
    accounts.save_account()


def delete_account(accounts):
    accounts.delete_account()


fe


def find_accounts(user_name):
    return Accounts.find_by_user_name(page)


def isexist_accounts(user_name):
    return Accounts.account_exists(page)


def display_accounts():
    return Accounts.display_accounts()


def create_page(page, password):
    passwords = Password('facebook', '12345')
    return passwords


def save_page(passwords):
    passwords.save_page()


def find_page(pager):
    return Password.find_by_page(pager)


def isexist_page(pager):
    return Password.page_exists(pager)


def delete_page(passwords):
    passwords.delete_page()


def display_pages():
    return Password.display_page()


def main():
    print('WELCOME TO PASSLOCK')
    print('Use the following numbers to pick their corresponding values')
    while True:

        print(" 1) LOGIN \n 2) SIGN UP \n 3) ABOUT PASSLOCK \n")

        choice = int(input())
        if choice == 1:
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()

            print(f'Welcome {username}, Use the following numbers to select their corresponding values')
            print(
                ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords ')

            log_choice = int(input())
            if log_choice == 1:
                print('New page')
                print('*'*100)

                print('Page name')
                page = input()

                print('password')
                password = input()

                # created and saved page
                save_page(create_page(page, password))

            elif log_choice == 2:
                print("Enter the name of the page you want to delete")

                page = input()
                if isexist_page(page):
                    remove_page = (page)
                    del_page(remove_page)

                else:
                    print(f'I cant find {page}')

            elif log_choice = 3:
                if display_pages():
                    for pag in display_pages()
                    print(
                        f'{pag.page}:{pag.password}'
                    )

            else:
                break


if __name__ == '__main__':
    main()
