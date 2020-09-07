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
