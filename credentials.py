class Credentials:
    """
    Class to generate the instance of a User credentials
    """

    user_list= []

    def __init__(self, appname,appusername, appemail, apppassword):

            self.appname = appname
            self.appusername =appusername
            self.appemail = appemail
            self.apppassword = apppassword
