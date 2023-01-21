import random;
import string;

# Global Variables.
password_len = None;
letters = string.ascii_letters;
numbers = string.digits;
special_chars = string.punctuation;

# While loop to grab to users input for a password.
while type(password_len) != int:
    try:
        password_len = int(input('\033[1;37;40mEnter the length of the password: \033[1;32;40m'));
    except ValueError:
        print('\033[1;31;40mInvalid Entry. Please enter an numeric value.\n\033[1;37;40m')
        pass

# Function to generate a password.
def createPassword(length):
    global password
    password = '';
    for i in range(length):
        password += (random.choice(letters+numbers+special_chars));

# Print logs and function call.
createPassword(password_len);
print('Your password has been generated below: \n');
print('\033[1;36;40m' + password + '\033[1;37;40m\n');