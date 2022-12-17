user = ''
name = 'admin'


def input_user():
    global user
    global name
    user = input('Представьтесь пожалуйста: ')
    if user == name:
        print(f'Добро пожаловать, {user}')
    else:
        print('Пользователь не распознан.\nВведите имя повторно: ')
        input_user()


def user_print():
    print()


def main():
    input_user()
    user_print()
    print(f'Текущий пользователь, {user}')
    print(__name__)


# if __name__ == '__main__':
#     main()
main()