class User():
    def __init__(self, id=None, name=None):
        self._id =  id
        self._name = name
        self._users = []

    def id(self):
        return self._id

    def id(self, value):
        self._id = value

    def name(self):
        return self._name

    def name(self, value):
        self._name = value

    def users(self):
        return self._users.copy()

class Admin(User):
    def __init__(self, id, name, access):
        super().__init__(id, name)
        self._access = access

    def access(self):
        return self._access

    def add_user(self, id, name):
        new_user = {'id': id,'name': name}
        if any(user['id'] == id for user in self._users):
            print(f"Внимание: пользователь с id '{id}' уже есть")
            return
        self.users.append(new_user)
        print(f"{name} - добавление успешно")

    def remove_user(self, id):
        for i, user in enumerate(self._users):
            if user['id'] == id:
                self._users.pop(i)
                print(f"Пользователь с id {id} - удаление успешно")
                return
        print(f"Пользователь с id {id} - не существует")

