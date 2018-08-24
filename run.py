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

    def display_accounts()
        return Accounts.display_accounts()

    def create_page(page, password):
        passwords = Password('facebook', '12345')
        return passwords

    def save_page(passwords):
        passwords.save_page()

    def delete_page(passwords):
        passwords.delete_page()

    def display_pages():
        return Password