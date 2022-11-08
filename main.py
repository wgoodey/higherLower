from game_data import data
import art
import random
import os


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def get_new(data_list, history_list):
    """Returns a randomly selected entity from the data_list and inserts it into the history_list."""
    while True:
        new = random.choice(data_list)
        if new not in history_list:
            history_list.append(new)
            break
    return new


def get_guess(a, b):
    """Prompts user for input of 'A' or 'B' and returns the selected item."""
    while True:
        response = input("Who has more followers? Type \'A\' or \'B\': ").upper()
        if len(response) > 0:
            response = response[0]
        if response == "A" or response == "B":
            break
        else:
            print("Please select \'A\' or \'B\'.")
    return a if response == "A" else b


def get_answer(first, second):
    """Returns the entity with the higher follower_count."""
    return first if first['follower_count'] > second['follower_count'] else second


def print_options(a, b):
    """Prints the name, description, and country of origin of th two options with vs art inbetween."""
    print(f"Name: {a['name']}")
    print(f"Description: {a['description']}")
    print(f"Country: {a['country']}")
    print(art.vs)
    print(f"Name: {b['name']}")
    print(f"Description: {b['description']}")
    print(f"Country: {b['country']}\n")


def reload():
    """Asks the user if they want to reload the game."""
    response = input("Do you want to play again? Type \'Y\' to reload: ").upper()
    if len(response) > 1:
        response = response[0]
    return True if response == "Y" else False


def game():
    """Provides the user two options and asks them to pick the one with the most followers. It repeats until an
    incorrect answer is given. Returns True or False depending on if the user wants to play again."""
    history = []
    score = 0
    # randomly select 2 keys from the game_data.py and assign them to a and b, adding them to a history dictionary
    a = get_new(data, history)
    b = get_new(data, history)
    while True:
        print_options(a, b)
        # compare which has more followers
        answer = get_answer(a, b)
        # get user's guess which has more followers
        guess = get_guess(a, b)
        # if user is correct, assign b to a and select new random choice for b
        # if user is incorrect, game is over. display score
        print(f"\n{a['name']}: {a['follower_count']} Million\n{b['name']}: {b['follower_count']} Million")
        if answer == guess:
            print(f"\nYou got it!\nHere's the next one:\n")
            score += 1
            a = b
            b = get_new(data, history)
        else:
            print("\nSorry, You lost.")
            print(f"Your score was {score}.")
            break

    # ask if user wants to play again
    return reload()


print(art.logo)
play_again = True

while play_again:
    play_again = game()
    clear_screen()
