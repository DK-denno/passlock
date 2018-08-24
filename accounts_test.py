from accounts import Accounts
import unittest


class TestAccount(unittest.TestCase):
    def tearDown(self):
        Accounts.user_accounts = []

    def setUp(self):
        self.new_account = Accounts('dennis', 'kamau', 'Dk-denno', '4321')

    def test_init(self):
        self.assertEqual(self.new_account.first_name, 'dennis')
        self.assertEqual(self.new_account.last_name, 'kamau')
        self.assertEqual(self.new_account.user_name, 'Dk-denno')
        self.assertEqual(self.new_account.password, '4321')

    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(Accounts.user_accounts), 1)

    def test_save_multiple_accounts(self):
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        self.assertEqual(len(Accounts.user_accounts), 2)

    def test_del_account(self):
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Accounts.user_accounts), 1)

    def test_find_account_by_username(self):
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        found_account = Accounts.find_by_user_name('ijkl')
        self.assertEqual(found_account.user_name, test_account.user_name)

    def test_account_exists(self):
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        account_exists = Accounts.account_exists('ijkl')
        self.assertTrue(account_exists)

    def test_display_accounts(self):
        self.assertEqual(Accounts.display_accounts(),
                         Accounts.user_accounts)


if __name__ == '__main__':
    unittest.main()
