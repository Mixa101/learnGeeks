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