class User:
    def __init__(self, id=None, name=None):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Admin(User):
    def __init__(self, id, name, access):
        super().__init__(id, name)
        self._access = access
        self._users = []  # список пользователей теперь хранится только в Admin

    @property
    def access(self):
        return self._access

    def add_user(self, id, name):
        new_user = {'id': id, 'name': name}
        if any(user['id'] == id for user in self._users):
            print(f"Внимание: пользователь с id '{id}' уже есть")
            return
        self._users.append(new_user)
        print(f"{name} - добавление успешно")

    def remove_user(self, id):
        for i, user in enumerate(self._users):
            if user['id'] == id:
                self._users.pop(i)
                print(f"Пользователь с id {id} - удаление успешно")
                return
        print(f"Пользователь с id {id} - не существует")

    def users(self):
        return self._users.copy()

