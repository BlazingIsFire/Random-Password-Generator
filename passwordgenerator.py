import random;
import string;

password_len = None;
letters = string.ascii_letters;
numbers = string.digits;
special_chars = string.punctuation;

while type(password_len) != int:
    try:
        password_len = int(input('\033[1;37;40mEnter the length of the password: \033[1;32;40m'));
    except ValueError:
        print('\033[1;31;40mInvalid Entry. Please enter an numeric value.\n\033[1;37;40m')
        pass

def createPassword(length):
    global password
    password = '';
    for i in range(length):
        password += (random.choice(letters+numbers+special_chars));

createPassword(password_len);
print('Your password has been generated below: \n');
print('\033[1;36;40m' + password + '\033[1;37;40m');