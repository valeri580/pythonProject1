from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        pass


class Sword(Weapon):
    def attack(self, target):
        print(f"Боец наносит удар мечом.")


class Bow(Weapon):
    def attack(self, target):
        print(f"Боец наносит удар из лука.")


class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{ self.name} выбирает {weapon.__class__.__name__}.")

    def attack(self, target):
        if self.weapon:
            self.weapon.attack(target)
        else:
            print(f"{self.name} бьёт кулаком по {target.name}.")


class Monster():
    def __init__(self, monster_name):
        self.monster_name = monster_name


    def status(self):
        print(f"{self.monster_name} побежден!")


fighter = Fighter("Иван")
monster = Monster("Дракон")

fighter.change_weapon(Sword())
fighter.attack(monster)
monster.status()


