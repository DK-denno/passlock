class Password:
    def __init__(self, page, password):
        self.page = page
        self.password = password

    user_passwords = []

    def save_page(self):
        Password.user_passwords.append(self)
