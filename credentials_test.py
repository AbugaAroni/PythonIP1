import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Credential("Facebook","AbugaAroni","password")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_cred.appname,"Facebook")
        self.assertEqual(self.new_cred.appusername,"AbugaAroni")
        self.assertEqual(self.new_cred.apppassword,"password")

    def test_save_cred(self):
        '''
        test case to test if the cred object is saved into the cred list
        '''
        self.new_cred.save_cred()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_cred(self):
        '''
        check if we can save multiple objects to our cred_list
        '''
        self.new_cred.save_cred()
        test_cred = Credential("Twitter","John75","20password20")
        test_cred.save_cred()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_cred(self):
        '''
        test if we can remove a credential from our credential list
        '''
        self.new_cred.save_cred()
        test_cred = Credential("Slack","username","1224password") # new credential
        test_cred.save_cred()

        self.new_cred.delete_cred()# Deleting a cred object
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_cred_by_appname(self):
        '''
        test to check if we can find a credential by the appname and get display information
        '''

        self.new_cred.save_cred()
        test_cred= Credential("Youtube","usernameyt","1224paseresword") # new credential
        test_cred.save_cred()

        found_cred = Credential.find_by_appname("Youtube")

        self.assertEqual(found_cred.appname,test_cred.appname)

    def test_display_all_cred(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_creds(),Credential.credential_list)

    def test_passwordgenerator(self):
        '''
        method that test the password generator
        '''

        self.new_cred.save_cred()
        test_cred= Credential("Newgrounds","usyt","") # new credential
        test_cred.save_cred()

        new_password = Credential.generatePassword(8)
        test_cred.apppassword = new_password

        self.assertEqual(test_cred.apppassword,new_password)

    def test_cred_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential information.
        '''

        self.new_cred.save_cred()
        test_cred = Credential("Google","amceweyt","12cewgaeusircord") # new user
        test_cred.save_cred()

        cred_exists = Credential.cred_exist("Google")
        self.assertTrue(cred_exists)

if __name__ == '__main__':
    unittest.main()
