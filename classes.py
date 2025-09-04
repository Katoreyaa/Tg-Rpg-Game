import random

class Entity:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, target):
        effective_damage = max(0, self.damage - target.armor)
        target.health -= effective_damage

class Enemy(Entity):

    def difficulty_level(self, difficulty):
        self.difficulty_level = difficulty
        
class Player(Entity):
    def __init__(self,health, damage, armor):
        super().__init__(health, damage, armor)
        self.level = 0
        self.experience = 0
    
    def level_up(self):
        self.level += 1
        self.health += 10
        self.damage += 5
        self.armor += 2

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()
        self.experience = self.experience % 100


def Create_Enemy():
    difficulty = random.choice(["easy","medium","hard"])

    if difficulty == "easy":
        return Enemy(
            random.randint(50, 100),
            random.randint(5, 10),
            random.randint(2,5)
        )
    if difficulty == "medium":
        return Enemy(
            random.randint(100, 150),
            random.randint(10, 15),
            random.randint(5, 10)
        )
    if difficulty == "hard":
        return Enemy(
            random.randint(150, 200),
            random.randint(15, 20),
            random.randint(10,20)
        )
    

        

    
    
    
def main():
    gigachad = Create_Enemy()   


if __name__ == ("__main__"):
    main()
