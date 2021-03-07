import secrets
import string
import time


def custom_pass(chars):
    chars += string.digits if flag_nums.lower() == 'y' else ''
    chars += string.ascii_lowercase if flag_lowers.lower() == 'y' else ''
    chars += string.ascii_uppercase if flag_uppers.lower() == 'y' else ''
    chars += string.punctuation if flag_symbols.lower() == 'y' else ''
    chars += complex if flag_complex.lower() == 'y' else ''
    print('Password can`t be empty lol XD') if chars == '' else print('\n' + generate_password(len, chars) + '\n')
    return chars

def all_in(chars):
    chars += string.digits
    chars += string.ascii_lowercase
    chars += string.ascii_uppercase
    chars += string.punctuation
    chars += complex
    print('Password can`t be empty lol XD') if chars == '' else print('\n' + generate_password(len, chars) + '\n')
    return chars

def generate_password(len, chars):
    passwords = []
    password = ''
    for circle in range(num):
        for symbol in range(len):
            password += secrets.choice(chars)
        passwords.append(password)
        password = ''
    return '\n'.join(passwords)

complex = 'il1Lo0O'
chars = ''

while True:
    try:
        choice = input('Type "y" if you want to customize your password or just press Enter to create '
                       'strong password right now'
                       )
        if choice == 'y':
            num = int(input('How many passwords?\n '))
            len = int(input('Password length?\n '))
            flag_nums = input('Include numbers? (y n)\n')
            flag_lowers = input('Include lowercase letters? (y n)\n ')
            flag_uppers = input('Include uppercase letters? (y n)\n ')
            flag_symbols = input('Include special symbols? (y n)\n ')
            flag_complex = input('Include confusing letters, like "il1Lo0O"? (y n)\n')
            custom_pass(chars)
        else:
            len = int(input('Password length?\n '))
            num = int(input('How many passwords?\n'))

            generate_password(len, all_in(chars))
    except ValueError:
        print('This one should be a number. Try again\n')
        continue


    exit = input('Run again? Type "n" to exit\n')
    if exit.lower() == 'n':
        break
    else:
        continue
print('See ya!')
time.sleep(2)