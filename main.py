from random import choice

digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
ally = digits + uppercase + lowercase + punctuation

chars = ''

while True:
    print('1. Показать действующие пароли')
    print('2. Создать новый пароль')
    print('3. Изменить действующий пароль')
    cmd = input('Выберете желаемую операцию: ')

    if cmd == '1':
        file = open('passwd.txt', 'r')
        print(file.read())
        file.close()
        break
    elif cmd == '2':
        pwd_length = int(input('Введите желаемую длину пароля: '))
        pwd_auto = input('Сгенерировать пароль автоматически? (y, n): ')

        if pwd_auto == 'y':
            chars += ally
        else:
            pwd_digits = input('Включить цифры (y, n): ')
            pwd_uppercase = input('Включить uppercase (y, n): ')
            pwd_lowercase = input('Включить lowercase (y, n): ')
            pwd_punctuation = input('Включить спец. символы (y, n): ')
            if pwd_digits == 'y':
                chars += digits
            if pwd_uppercase == 'y':
                chars += uppercase
            if pwd_lowercase == 'y':
                chars += lowercase
            if pwd_punctuation == 'y':
                chars += punctuation

        password = ''

        for i in range(pwd_length):
            password += choice(chars)

        print('\n', password, '\n', sep='')

        pwd_new = input('Желаете сохранить данный пароль? (y, n): ')
        if pwd_new == 'y':
            pwd_social = input('Укажите соц. сеть: ')
            file = open('passwd.txt', 'a')
            file.write('\n')
            file.write(pwd_social)
            file.write(': ')
            file.write(password)
            file.close()



        break