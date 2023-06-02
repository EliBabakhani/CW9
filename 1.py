import re
password = input('Enter password: ')


def is_password_valid(passwrod: str):
    result = re.match(
        r"?=.(?=.{8,})(?=.\d)(?=.[a-z])(?=.[A-Z])$", password)
    if result:
        return True
    else:
        return False

is_password_valid(password)