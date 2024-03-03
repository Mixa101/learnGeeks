class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def get_name_hero(self):
        return self.name
    def multiplication_hp(self):
        self.health_points = self.health_points * 2
        print(f'succesful multiplication health point\'s to {self.health_points}')
    
    def __str__(self) -> str:
        return f'nickname : {self.nickname}\nsuperpower : {self.superpower}\nHP : {self.health_points}'

zoro = SuperHero('Zoro', 'king of hell', 'three sword style', 50, 'where i am, give me bear')
print(zoro)
print(zoro.get_name_hero())
zoro.multiplication_hp()

class earth_hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = True, lazer_eyes = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
        self.lazer_eyes = lazer_eyes
    def multiplication_hp(self):
        self.health_points = self.health_points ** 2
        self.fly = True
    
    def say_phrase(self):
        print('True in the True_phrase')
    # здесь я не понял может вы хотели чтобы мы вывели catchphrase и ошиблись и изза этого сделаю обе
    def say_catchphrase(self):
        print(f'True in the {self.catchphrase}')

class cosmic_hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = True, immortality = True):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
        self.immortality = immortality
    def multiplication_hp(self):
        if self.immortality == True:
            print('I\'m already immortal!!!')
            self.health_points = 1
        else:
            self.health_points = self.health_points ** 2
        self.fly = True
    def say_phrase(self):
        print('True in the True_phrase')

    def say_catchphrase(self):
        print(f'True in the {self.catchphrase}')

class villain(earth_hero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=True, lazer_eyes=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly, lazer_eyes)
    
    def gen_x(self):
        pass
    def crit(self):
        self.damage = self.damage ** 2
        print(f'Damage up to {self.damage}')

IronMan = earth_hero('Stark', 'IronMan', 'Mind', 100, 'We have a Hulk', 30)
IronMan.get_name_hero()
IronMan.multiplication_hp()
IronMan.say_phrase()
IronMan.say_catchphrase()
###
Thor = cosmic_hero('Thor', 'Thunder God', 'Lightning', 100, 'Give me the Thanos', 50)

Thor.say_catchphrase()
Thor.say_phrase()

Thanos = villain('Thanos', 'Mad Titan', 'infinity stones', 100, 'Couldn\'t accept defeat', 60)
Thanos.crit()
### я не понял как что надо делать с CRIT 