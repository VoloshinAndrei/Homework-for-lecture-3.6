# Домашнее задание к лекции 3.6 «Классы и их применение в Python»
# Необходимо реализовать классы животных на ферме:

# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
#
# Условия:
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

class domestic_animals:
    weight = 10  # kg
    height = 50  # cm
    favorite_food = None

    def eat(self, value):
        self.weight += value


class cows(domestic_animals):
    weight = 100  # kg
    height = 100  # cm

    def give_milk(self):
        print("You have cow's milk")
        self.weight -= 0.5


class goats(domestic_animals):
    weight = 50  # kg

    def give_milk(self):
        print("You have goat's milk")
        self.weight -= 0.3


class sheep(domestic_animals):
    weight = 50  # kg

    def give_wool(self):
        print("You have sheep's wool")
        self.weight -= 10


class pigs(domestic_animals):
    weight = 70  # kg
    height = 30  # cm

    def kill_pig(self):
        print("You have pig's meat")
        self.weight = 0


class ducks(domestic_animals):
    height = 30  # cm

    def kill_duck(self):
        print("You have duck's meat and feathers")
        self.weight = 0


class chickens(domestic_animals):
    weight = 7
    height = 20  # cm

    def kill_chicken(self):
        print("You have chicken's meat and you can cook some chicken nuggets!")
        self.weight = 0

    def make_egg(self):
        print("You have chicken's egg")
        self.weight -= 0.1


class geese(domestic_animals):
    weight = 15
    height = 20  # cm

    def save_Rome(self):
        print("The geese have saved Rome!!!")

    def give_feathers(self):
        print("You got some feathers and you can make a pen!")


x1 = cows()
print(x1.weight)
x1.give_milk()
print(x1.weight)

y1 = geese()
y1.save_Rome()

