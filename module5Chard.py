# Модуль 5 . Доп. задание.
# ========================


class Video:
    def __init__(self, title, duration, time_now,adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        if adult_mode>= adult_mode:
            self.adult_mode = True
class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users['']
        self.videos = videos['']
        self.current_user = current_user
    def log_in(nickname, password):
        print()


def __add__(nickname):
    pass


def register(self, nickname, password, age):
        if not isinstance( nickname, str):
            User. __add__([' nickname'])
        else:
            print("Пользователь {username} уже существует")
class Databasa:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password
        # gprint(username)
class User:
    """
    Класс пользователя,содержащий атрибуты: логин, пароль,возраст.
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
    # def __hash__(self):
    #     return ((self.nickname, self.password,self.age))
    #     print(self)

if __name__ == '__main__':
    databasa=Databasa()
    while True:
        choice = input("Привет. Выберите действие: \n1-Вход\n2-Регистрация\n")
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in databasa.data:
                if password==databasa.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else:
                    print("Не верный пароль.")
            else:
                print('Пользователь не найден.')

        if choice == 2:
            user=User(input('Введите логин: '), password:= input('Введите пароль: '),
                  password2:=input('Повторите пароль: '))
            if password != password2:
                print("Пароли не совпадают, попрубуйте еще раз.")
                continue
            databasa.add_user(user.username, user.password)
        print(databasa.data)
#ur = UrTube()
# print(result('Лучший язык программирования 2024 года', 200,20))
#v1 = User('Лучший язык программирования 2024 года', 200,200,20)
# v2 = result('Для чего девушкам парень программист?', 10, adult_mode=True)
# #v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
#ur.add(v1, v2)

