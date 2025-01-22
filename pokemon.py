import requests 
pokemon_number = input("What is the Pokemon's ID? ") 
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number) 
response = requests.get(url)
pokemon = response.json() 
moves = pokemon['moves'] 
for move in moves: 
    print(move['move']['name'])