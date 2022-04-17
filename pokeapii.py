import requests

def get_pokemon_info(name):
    print("getting poke info- ", end='')
    poke_url = 'https://pokeapi.co/api/v2/pokemon/' 
    response = requests.get(poke_url)

    if response.status_code == 200:
        print('pokeinfo')
        return response.json()
    else:
        print('fail to get info',response.status_code)
        return None