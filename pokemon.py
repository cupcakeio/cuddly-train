import random
import requests
import concurrent.futures


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'moves': [{'name': move['move']['name'], 'url': move['move']['url']} for move in pokemon['moves']],
        'no_of_moves': len(pokemon['moves']),
    }


def get_move_details(move_url):
    response = requests.get(move_url)
    move_data = response.json()

    return {
        'name': move_data['name'],
        'power': move_data['power'],  
        'accuracy': move_data['accuracy'],
        'type': move_data['type']['name'],
    }


def get_random_moves(pokemon, num_moves=3):
    available_moves = pokemon['moves']
    if len(available_moves) < num_moves:
        num_moves = len(available_moves)
    selected_moves = random.sample(pokemon['moves'], num_moves)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        detailed_moves = list(executor.map(get_move_details, [move['url'] for move in pokemon['moves']]))
    valid_moves = [move for move in detailed_moves if move['power'] is not None]
    if len(valid_moves) < num_moves:
        print(f"Warning: Only {len(valid_moves)} valid moves available. Returning fewer moves.")
        num_moves = len(valid_moves)
    return random.sample(valid_moves, num_moves)



def run(you, opponent):
    my_pokemon = random_pokemon()

    my_pokemon_random_moves = get_random_moves(my_pokemon, 3)  
    moves_display = ', '.join(
        [f"{move['name']} (Power: {move['power']})" for move in my_pokemon_random_moves]
    )

    if not my_pokemon_random_moves:
        print(f"{my_pokemon['name']} has no valid moves! Skipping turn...")
        return you, opponent

    print(f"You were given {my_pokemon['name']} with {my_pokemon['no_of_moves']} moves!")
    stat_choice = input(f"Your three generated move choices are: \n{moves_display}. \nWhich one would you like to choose? ")

    
    chosen_move = next((move for move in my_pokemon_random_moves if move['name'] == stat_choice), None)
    if not chosen_move:
        print("Invalid move choice!")
        return you, opponent

    print(f"You chose {chosen_move['name']} with Power: {chosen_move['power']}.")

   
    opponent_pokemon = random_pokemon()
    opponent_pokemon_random_moves = get_random_moves(opponent_pokemon, 3)  

    if not opponent_pokemon_random_moves:
        print(f"{opponent_pokemon['name']} has no valid moves! You win this round!")
        return you + 1, opponent
    
    opponent_move = random.choice(opponent_pokemon_random_moves)  

    print(f"The opponent chose {opponent_pokemon['name']} and used {opponent_move['name']} (Power: {opponent_move['power']}).")

    
    if chosen_move['power'] > opponent_move['power']:
        print("You Win!")
        you = you + 1
    elif chosen_move['power'] < opponent_move['power']:
        print("You Lose!")
        opponent = opponent + 1
    else:
        print("It's a Draw!")

    return you, opponent

def game():
    you = 0
    opponent = 0
    
    while you < 3 and opponent < 3:
        you, opponent = run(you, opponent)
        print(f"Score - You: {you}, Opponent: {opponent}")

    if you == 3:
        print("\nCongratulations! You won the game!")
    else:
        print("\nSorry! You lost the game!")

    play_again = input("Play again? (y/n)").strip().lower()

    return play_again

def bestOfThree():
    play_again = "y"
    while play_again == "y":
        play_again = game()
    
    print("Thanks for playing!")
    
    
print("Welcome to Pokemon Top Trumps Best of Three.\nChoose a move to use against your opponent and first to three wins!")
bestOfThree()

