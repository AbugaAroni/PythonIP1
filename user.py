class User:
    """
    Class to generate the instance of a User
    """

    user_list= []

    def __init__(self, uname, password):

            self.uname =uname
            self.password = password

    def save_user(self):

        '''
        method that saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def user_exist(cls,ulname,pword):
        '''
        Method that checks if a user exists from the user list.
        Args:
            ulname: username to search if it exists
            pword: password to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.uname == ulname and user.password == pword:
                    return True
