from passwords import Password
import unittest


class TestPasswords(unittest.TestCase):
    def setUp(self):
        self.new_password = Password('facebook', '12345')

    def test_init(self):
        self.assertEqual(self.new_password.page, 'facebook')
        self.assertEqual(self.new_password.password, '12345')

    def test_save_page(self):
        self.new_password.save_page()
        self.assertEqual(len(Password.user_passwords), 1)

    def test_save_multiple(self):
        self.new_password.save_page()
        test_password = Password('instagram', '4321')
        test_password.save_page()
        self.assertEqual(len(Password.user_passwords), 2)


if __name__ == '__main__':
    unittest.main()
