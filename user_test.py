import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Abuga1","password1")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.uname,"Abuga1")
        self.assertEqual(self.new_user.password,"password1")

    def test_save_user(self):
        '''
        test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
            '''
            check if we can save multiple objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Joshua2","20password20")
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user details.
        '''

        self.new_user.save_user()
        test_user = User("jimmiek","12334") # new user
        test_user.save_user()

        user_exists = User.user_exist("jimmiek", "12334")
        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()
