import requests
from pprint import pprint

class SuperHero:
    def __init__(self, name):
        self.name = name

    def Get_SuperHero_Intelligence(self):
        url = "https://superheroapi.com/api/2619421814940190/search/"
        params = {}
        headers = {}
        response = requests.get(url + self.name, params=params, headers=headers, timeout=5)
        dict_ = response.json()
        for line in dict_['results']:
            return int(line['powerstats']['intelligence'])

if __name__ == '__main__':
    super_heroes = ['Hulk', 'Captain America', 'Thanos']
    super_heroes_intelligence = {}
    for super_hero in super_heroes:
        super_heroes_intelligence[super_hero] = SuperHero(super_hero).Get_SuperHero_Intelligence()
    print(f'Самый умный супергерой - {max(super_heroes_intelligence, key=super_heroes_intelligence.get)}')


