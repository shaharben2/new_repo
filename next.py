import functools
import string

def check_input(username, password):
    is_username_ok = True
    is_password_ok = True
    must_letters = {"Upper" : 0, "Lower": 0, "Digit" : 0, "Punc" : 0}
    for char in username:
        if not (char.isalpha() or char.isdigit() or char == "_"):
            is_username_ok = False
            raise UsernameContainsIllegalCharacter(char, username.find(char))
            

    if len(username) < 3:
        is_username_ok = False
        raise UsernameTooShort()

    if len(username) > 16:
        is_username_ok = False
        raise UsernameTooLong()
    
    if len(password) < 8:
        is_password_ok = False
        raise PasswordTooShort()
    
    if len(password) > 40:
        is_password_ok = False
        raise PasswordTooLong()
    
    for char in password:
        if char.isupper():
            must_letters["Upper"] += 1
        elif char.islower():
            must_letters["Lower"] += 1
        elif char.isdigit():
            must_letters["Digit"] += 1
        elif char in string.punctuation:
            must_letters["Punc"] += 1
    
    for key in must_letters:
        if must_letters[key] == 0:
            is_password_ok = False
            if key == "Upper":
                raise UpperCase()
            elif key == "Lower":
                raise LowerCase()
            elif key == "Digit":
                raise Digit()
            elif key == "Punc":
                raise Special()

    if is_username_ok and is_password_ok:
        print("OK")

    return "OK"

    

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, idx):
        self._char = char
        self._idx = idx

    def __str__(self):
        print('The username contains an illegal character \"%s\" at index %d' % (self._char, self._idx))

class UsernameTooShort(Exception):
    def __str__(self):
        print("The username is too short")

class UsernameTooLong(Exception):
    def __str__(self):
        print("The username is too long")

class PasswordMissingCharacter(Exception):
    def __str__(self):
        print("The password is missing a character")

class PasswordTooShort(Exception):
    def __str__(self):
        print("The password is too short")

class PasswordTooLong(Exception):
    def __str__(self):
        print("The password is too long")

class UpperCase(PasswordMissingCharacter):
    def __str__(self):
        print("The password is missing a character (Uppercase)")

class LowerCase(PasswordMissingCharacter):
    def __str__(self):
        print("The password is missing a character (Lowercase)")

class Digit(PasswordMissingCharacter):
    def __str__(self):
        print("The password is missing a character (Digit)")

class Special(PasswordMissingCharacter):
    def __str__(self):
        print("The password is missing a character (Special)")


def main():
    is_ok = ""
    while is_ok != "OK":
        username = input("enter username: ")
        password = input("enter password: ")
        try:
            is_ok = check_input(username, password)
        except Exception as e:
            e.__str__() 

    # check_input("0123456789ABCDEFG", "2")
    # check_input("A_a1.", "12345678")
    # check_input("A_1", "2")
    # check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    # check_input("A_1", "abcdefghijklmnop")
    # check_input("A_1", "ABCDEFGHIJLKMNOP")
    # check_input("A_1", "ABCDEFGhijklmnop")
    # check_input("A_1", "4BCD3F6h1jk1mn0p")
    # check_input("A_1", "4BCD3F6.1jk1mn0p")
    

if __name__ == '__main__':
    main()