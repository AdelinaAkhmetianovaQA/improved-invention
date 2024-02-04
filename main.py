import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                         json = {
                             "name": "Here",
                             "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/009.png&size=200"},
                         headers = {'Content-Type': 'application/json', 'trainer_token' : '999874506bf6450cfbfc081d0328b224'})
print(response.text)

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
                         json = {
                             "pokemon_id": "29655",
                             "name": "Where",
                             "photo": "https://dolnikov.ru/pokemons/albums/008.png"},
                         headers = {'Content-Type': 'application/json', 'trainer_token' : '999874506bf6450cfbfc081d0328b224'})
print(response.text)

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                         json = {
                             "pokemon_id": "29655",
                            },
                         headers = {'Content-Type': 'application/json', 'trainer_token' : '999874506bf6450cfbfc081d0328b224'})
print(response.text)