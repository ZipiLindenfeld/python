import os
import math
import re
from email import utils

# class SmartArray:
#     def __init__(self, usernames):
#         n = len(usernames)
#         self.accessible_usernames = usernames[:math.ceil(n * 0.1)]
#
#     def get_accessible_usernames(self):
#         return self.accessible_usernames
from validate_email import validate_email


class Task8:
    # def __init__(self):
    #     self.data=

    def read_file(filename):
        if not os.path.exists(filename):
            if not os.path.exists("subdirectory"):
                os.makedirs(f"subdirectory/{filename}")

    def read_usernames_gen(filename):
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()

    def read_usernames(filename):
        with open(filename, 'r') as file:
            users = file.read().splitlines()
            return users

    # def read_90_users_names(filename):
    #     with open(filename, 'r') as file:
    #         usernames = file.read().splitlines()
    #         return SmartArray(usernames)

    def read_email_addresses(filename):
        with open(filename, 'r') as file:
            email_addresses = file.read().splitlines()
            return email_addresses

    def validate_email_addresses(email_addresses):
        valid_email_addresses = []

        for email_address in email_addresses:
            email_address = utils.parseaddr(email_address)[1]
            if validate_email(email_address):
                valid_email_addresses.append(email_address)
        return valid_email_addresses

    def get_even_usernames(usernames):
        even_usernames = []
        for i, username in enumerate(usernames):
            if i % 2 == 1:
                even_usernames.append(username)
        return even_usernames

    def get_gmail_addresses(email_addresses):
        gmail_addresses = []
        for email_address in email_addresses:
            if re.search(r'@gmail\.com$', email_address, re.IGNORECASE):
                gmail_addresses.append(email_address)
        return gmail_addresses

    def check_match_name(emails, names):
        for email, name in zip(emails, names):
            email_without_domain = re.sub('@.*', ' ', email)
            if name in email_without_domain:
                print(f"{name} is in the {email}")

    def input_name_check_if_in_the_list(users_names):
        user_name = input("enter your name")
        for name in users_names:
            if user_name.lower() == name.lower():
                print("true")
        print("false")
        asci = [ord(char) for char in user_name]
        print(asci)
        print(user_name.lower().count('a'))
        # return user_name.lower() in [name.lower() for name in users_names]

    def check_letters(usersnames):
        return all(user[0].isupper() for user in usersnames)

    def sum_i_have(usersnames):
        print(len(usersnames) / 8 * 200 + len(usersnames) % 8 * 50)

    # 1
    file_content = read_file("UsersName.txt")
    # 2
    usersnames = read_usernames('UsersName.txt')
    for username in read_usernames_gen('UsersName.txt'):
        print(username)
    # 3
    # usernames_array = read_usernames('usernames.txt')
    # accessible_usernames = usernames_array.get_accessible_usernames()
    # print(accessible_usernames)
    # 4
    for user in get_even_usernames(read_usernames('UsersName.txt')):
        print(user)
    # 5
    email_addresses = read_email_addresses('UsersEmail.txt')
    valid_email_addresses = validate_email_addresses(email_addresses)
    for email_address in valid_email_addresses:
        print(email_address)
    # 6
    gmail_addresses = get_gmail_addresses(valid_email_addresses)
    for email_address in gmail_addresses:
        print(email_address)
    # 7
    usersnames = read_usernames('UsersName.txt')
    # check_match_name(email_addresses, usersnames)
    # 8
    # input_name_check_if_in_the_list(usersnames)
    # 9
    # print(check_letters(usersnames))
    sum_i_have(usersnames)
