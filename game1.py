class Hero:
    def __init__(self, name, health=100, attack_power=30):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра 'Битва героев' начинается!")
        print(f"{self.player.name} vs {self.computer.name}")
        print("-----------------------------")

        current_attacker, current_defender = self.player, self.computer

        while self.player.is_alive() and self.computer.is_alive():
            # Показываем текущее состояние
            print(f"{self.player.name}: {self.player.health} HP")
            print(f"{self.computer.name}: {self.computer.health} HP")
            print()

            # Ход текущего атакующего
            damage = current_attacker.attack(current_defender)
            print(f"{current_attacker.name} атакует {current_defender.name} и наносит {damage} урона!")

            # Меняем атакующего и защищающегося
            current_attacker, current_defender = current_defender, current_attacker

            # Небольшая пауза для удобства чтения
            input("Нажмите Enter для продолжения...")
            print("-----------------------------")

        # Определяем победителя
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")

        print("Игра завершена.")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()