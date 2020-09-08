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

#credential

def create_credential(appname,appusername, apppassword):
    '''
    Function to create a new credential
    '''
    new_cred= Credential(appname,appusername, apppassword)
    return new_cred

def save_cred(credential):
    '''
    Function to save the new user
    '''
    credential.save_cred()

def del_cred(credential):
    '''
    Function to delete a contact
    '''
    credential.delete_cred()

def display_credential():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.display_creds()    

def main():

    while True:

        print("Hello Welcome to the password locker. Do you have an existing account? Y/N? use ex to quit")

        account_status= input()

        if account_status == 'n':
            print("Please create an account to access to the password locker")

            print ("Username ....")
            u_name = input()

            print("Password...")
            p_word = input()

            save_user(create_user(u_name,p_word))
            print ('\n')
            print(f"{u_name}, you have been added to the system. You may now login")
            print ('\n')

        elif account_status =='y':
            print("Please enter your login details")

            print ("Username ....")
            u_name = input()

            print("Password...")
            p_word = input()

            if check_existing_user(u_name,p_word):
                    print("Details correct, you are now being logged in ...")
                    print ('\n')
            else:
                    print("User does not exist, or your password or Username might be wrong, try again ....")
                    print ('\n')

        elif account_status == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the correct codes. Watch for capitalization")

if __name__ == '__main__':

    main()
