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
