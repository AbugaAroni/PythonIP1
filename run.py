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
def passwordGenerate():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.generatePassword(8)

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

                    while True:
                            print("Use these short codes to navigate the app : cc - create a new credential, dc - display credentials,  de -delete a contact, ex -exit the application")

                            short_code = input().lower()

                            if short_code == 'cc':
                                    print("New Credentials")
                                    print("-"*10)

                                    print ("Input the application you want to create a credential for ....")
                                    app_name = input()

                                    print("Input the username you wish to use ...")
                                    u_name = input()

                                    print("Would you like to create your own password or have one generated for you? y/n")
                                    password_generate= input()

                                    newPassword = ''
                                    if password_generate == 'n':

                                        print ('\n')
                                        print("Input the password you wish to use ...")
                                        newPassword = input()
                                        print ('\n')


                                    else password_generate =='y':

                                        print ('\n')
                                        newPassword = passwordGenerate();
                                        print ('\n')
                                        print(f"Your generated password {newPassword}")

                                    save_cred(create_cred(app_name,u_name,newPassword)) # create and save new contact.
                                    print ('\n')
                                    print(f"New Credentials for {app_name} have been created")
                                    print ('\n')

                            elif short_code == 'dc':

                                    if display_contacts():
                                            print("Here is a list of all your contacts")
                                            print('\n')

                                            for contact in display_contacts():
                                                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                            print('\n')
                                    else:
                                            print('\n')
                                            print("You dont seem to have any contacts saved yet")
                                            print('\n')

                            elif short_code == 'de':

                                    print("Enter the number for the contact you want to delete")
                                    search_number = input()
                                    if check_existing_contacts(search_number):
                                        print ('\n')
                                        search_contact = find_contact(search_number)
                                        del_contact(search_contact)
                                        print(f"Contact Deleted")
                                        print ('\n')
                                    else:
                                        print("That contact you want to delete does not exist")
                            elif account_status == "ex":
                                    print("Bye .......")
                                    break
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
