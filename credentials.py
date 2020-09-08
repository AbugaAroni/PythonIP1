class Credential:
    """
    Class to generate the instance of a User credentials
    """

    credential_list= []

    def __init__(self, appname,appusername, apppassword):

            self.appname = appname
            self.appusername = appusername
            self.apppassword = apppassword

    def save_cred(self):

        '''
        method that saves user objects into user_list
        '''

        Credential.credential_list.append(self)

    def delete_cred(self):

        '''
        this method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_appname(cls,appname):
        '''
        Method that takes in the appname and returns a credential that matches that number.

        Args:
            appname: App name to search for
        Returns :
            Credential that matches the info.
        '''

        for credential in cls.credential_list:
            if credential.appname == appname:
                return credential
