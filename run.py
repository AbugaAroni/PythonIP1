#!/usr/bin/env python3.6
from user import User
from credentials import Credentials


def create_user(uname,password):
    '''
    Function to create a new user
    '''
    new_user= User(uname,password)
    return new_user

def save_user(user):
    '''
    Function to save the new user
    '''
    user.save_user()

def check_existing_user(ulname,pword):
    '''
    Function that check if a user exists with that password and returns a Boolean
    '''
    return User.user_exist(ulname,pword)

def main():
        print("Hello Welcome to the password locker. Do you have an existing account? Y/N?")
    account_status= input()

    while True:

        if account_status = 'N':
            print("Please create an account to access to the password locker")

            print ("Username ....")
            u_name = input()

            print("Password...")
            p_word = input()

            save_user(create_user(u_name,p_word))
            print ('\n')
            print(f"{u_name}, you have been added to the system")
            print ('\n')

        elif account_status='Y':
            print("Please enter your login details")

            print ("Username ....")
            u_name = input()

            print("Password...")
            p_word = input()

            if check_existing_user(u_name,p_word):
                    print("Details correct, you are now being logged in ...")
            else:
                    print("User does not exist. Your password or Username might be wrong, try again")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()
