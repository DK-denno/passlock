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
        self.test_password = Password('instagram','4321')
        self.test_password.save_page()
        self







if __name__ == '__main__':
    unittest.main()
