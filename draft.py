"""
Kim Zhang
A01374508
"""
import json
import random
from pathlib import Path


def die_of_rooms(level):
    room = random.randint(1, 8)
    if room <= level:
        return "Totem"
    elif room > 8 - level:
        return "runes"
    else:
        return "empty room"


def make_board(level):
    board_template = {(row, column): die_of_rooms(level) for row in range(5) for column in range(5)}
    board_template[(0, 0)] = "empty room"
    return board_template


def make_character():
    """
    Make a character that has coordinate and HP.

    :precondition: must not pass any parameter
    :postcondition: make a dictionary representing a character with x and y coordinates and current HP
    :return: a dictionary with 6 key-value pairs
    {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Sanity": 10, "Experience": 0, "Level": 1}
    """

    character_template = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Sanity": 10, "Experience": 0,
                          "Darkness": 4, "Level": 1}
    return character_template


def describe_current_location(board, character):
    """
    Shows character's current location and its description.

    :param board: a dictionary representing board of locations, keys are in (x,y) form, values are descriptions
    :param character: a dictionary representing a character, items are x coordinate; y coordinate; and current HP
    :precondition: must pass two dictionaries
    :postcondition: shows the current coordinate location of character and the location's description
    """
    coordinate_x = character["X-coordinate"]
    coordinate_y = character["Y-coordinate"]
    location = (coordinate_x, coordinate_y)
    red_location = "\033[91m{}\033[0m".format(location)
    print(f"Your current location is: {red_location} it is: {board[location]}")
    return board[location]


def activate_totem(character):
    red_at = "\033[91m" + "at" + "\033[0m"
    text_activate = "Totem activated"
    text_not_activate = "Totem not activated. Try harder or try another direction"
    validation_activate = input(f"input {red_at} to activate the Totem: \n")
    while validation_activate != "at":
        validation_activate = input(f"input {red_at} to activate the Totem: \n")
    character["Current HP"] -= 1
    activate_totem_result = random.randint(1, character['Darkness'])
    if activate_totem_result > 1:
        print(f"{text_activate}")
        character["Experience"] += 1
    else:
        print(f"{text_not_activate}")
    return character


def read_runes(character):
    red_rr = "\033[91m" + "rr" + "\033[0m"
    text_read = "Runes read. You hear the whispers of the stars, speaking of eternal darkness and the endless void."
    text_not_read = "You can't read the runes. 'Weird place.' You thought."
    validation_read = input(f"input {red_rr} to read runes: \n")
    while validation_read != "rr":
        validation_read = input(f"input {red_rr} to read runes: \n")
    read_runes_result = random.randint(1, character['Darkness'])
    if read_runes_result > 1:
        print("{}".format(text_read))
        character["Sanity"] -= 1
        character["Experience"] += 2
    else:
        print("{}".format(text_not_read))
    return character


def check_level_up(character):
    if character['Level'] < 3 and character["Experience"] >= 10:
        return True
    else:
        return False


def get_user_choice():
    direction_system = {1: "North", 2: "South", 3: "West", 4: "East"}
    red_system = "\033[91m{}\033[0m".format(direction_system)
    print("_" * 10)
    print(red_system)
    while True:
        try:
            choice = int(input("Please choose your direction, please only input numbers from 1 to 4:\n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            if choice in [1, 2, 3, 4]:
                print("You choose to move: {}".format(direction_system[choice]))
                print("_" * 10)
                return choice
            else:
                print("Input must be a number from 1 to 4. Try again.")


def validate_move(character, direction):
    """
    Check if the character can move along the direction on the board.

    :param character: a dictionary representing a character with x-coordinate, y-coordinate and HP
    :param direction: an integer representing the direction that the character wants to move forward
    :precondition: board's keys must be coordinates in the form of (x , y)
    :precondition: character keys must be: "X-coordinate", "Y-coordinate", "Current HP"
    :precondition: direction must be in [1,2,3,4]
    :postcondition: must check if it is True or False that the character can move along the chosen direction
    :return: True if the character can move towards specified direction, False if it can't
    """
    current_row = character["X-coordinate"]
    current_column = character["Y-coordinate"]
    if direction == 1:
        return current_row - 1 >= 0
    elif direction == 2:
        return current_row + 1 <= 4
    elif direction == 3:
        return current_column - 1 >= 0
    elif direction == 4:
        return current_column + 1 <= 4


def move_character(character, direction):
    if direction == 1:
        character["X-coordinate"] -= 1
    elif direction == 2:
        character["X-coordinate"] += 1
    elif direction == 3:
        character["Y-coordinate"] -= 1
    elif direction == 4:
        character["Y-coordinate"] += 1


def mad_or_prophet(level):
    meet_mad_or_prophet = random.randint(1, 8)
    if meet_mad_or_prophet <= level:
        mad_text = ("When you turn the corner, you come face-to-face with wild, haunted eyes. "
                    "A figure, shrouded in tattered clothes, shambles towards you, muttering incoherently. "
                    "Their gaze is frenzied, and an unsettling chill runs down your spine. "
                    "It's clear that this poor soul has succumbed to madness, their mind fractured by horrors unknown. "
                    "With a sudden, startling energy, they lunge at you, driven by an unfathomable madness.")
        print(mad_text)
        return "Madness"
    elif meet_mad_or_prophet > 8 - level:
        prophet_text = ("As you navigate the misty streets, you encounter a solitary figure. "
                        "Cloaked in a robe adorned with arcane symbols, they stand eerily still. "
                        "Their eyes, filled with an otherworldly knowledge, fix upon you. "
                        "'Seeker of truths,' they intone in a voice that seems to echo from a forgotten age, "
                        "'heed my words and be enlightened.' "
                        "The air around them vibrates with a strange energy, "
                        "and you sense that this prophet may unlock secrets that will guide your journey.")
        print(prophet_text)
        return "Prophet"
    else:
        nobody_text = ("The streets are eerily empty. "
                       "Fog swirls around, casting shifting shadows, yet reveals no other soul. "
                       "An unsettling quiet pervades, as if the town itself holds its breath, "
                       "concealing secrets best left undiscovered.")
        print(nobody_text)
        return "Nobody"


def check_if_goal_attained(character):
    """
    Check if character has reached the bottom right hand corner.

    :param character: a dictionary representing a character with x-coordinate, y-coordinate and HP
    :precondition: character keys must be: "X-coordinate", "Y-coordinate", "Current HP"
    :postcondition: check if it is True that the character has reached the bottom right corner after last move
    :return: True if the character has reached the bottom right corner after the last move, False if it hasn't
    """
    current_location = (character["X-coordinate"], character["Y-coordinate"])
    goal_location = (4, 4)
    return current_location == goal_location


def check_win(character):
    red_fm = "\033[91m" + "fm" + "\033[0m"
    validation_fight = input(f"input {red_fm} to fight with the Madness: \n")
    while validation_fight != "fm":
        validation_fight = input(f"input {red_fm} to fight with the Madness: \n")
    chance_win = character['Darkness']
    chance = random.randint(1, chance_win)
    if chance >= 3:
        print("You won")
        character["Experience"] += 2
    else:
        print("You lose")
    character["Current HP"] -= 2
    character["Sanity"] -= 1
    return


def check_learn(character, level):
    red_lp = "\033[91m" + "lp" + "\033[0m"
    validation_learn = input(f"input {red_lp} to learn from the Prophet: \n")
    while validation_learn != "lp":
        validation_learn = input(f"input {red_lp} to learn from the Prophet: \n")
    border = 2*level
    chance = random.randint(1, border)
    if chance == 1:
        text_learn_runes = ("The prophet, though tainted by otherworldly forces, "
                            "imparts cryptic wisdom that resonates within you, "
                            "enhancing your understanding and strengthening your resolve.")
        print(text_learn_runes)
        print("runes learnt")
        character["Experience"] += 2
        character["Sanity"] += 1
    else:
        print("runes not learnt")
        text_not_learnt = ("As you approach, the prophet's form distorts unnaturally, "
                           "their words dissolving into an incomprehensible babble, "
                           "leaving you bewildered and no wiser than before.")
        print(text_not_learnt)
    return


def decide_text():
    text_generator = random.randint(1, 6)
    text_base = {1: "I hear the whispers of the stars, speaking of eternal darkness and the endless void.",
                 2: "Time is melting before my eyes, reality and dreams entwined, indistinguishable.",
                 4: "All is in vain, we are but insignificant specks in this cosmos.",
                 5: "I am unsure what is real anymore, or if my mind has been corrupted by the darkness.",
                 6: "Other worlds are calling me, I hear the summons from unknown realms.",
                 3: "Akhamna, Igwatius... these runes echo in my mind, I cannot stop them"}
    print(text_base[text_generator])
    return


def is_alive_and_sane(character):
    """
    Check if the character is alive based on character's HP.

    :param character: a dictionary representing a character, have 3 items for x-coordinate, y-coordinate and HP
    :precondition: character must be a dictionary containing keys: "X-coordinate", "Y-coordinate", "Current HP"
    :postcondition: check if the character is alive by checking if value of "Current HP" is greater than 0
    :return: True if the character is alive, False if character dead
    """
    if character["Current HP"] <= 0:
        print("You are dead of low HP")
        return False
    elif character["Sanity"] <= 0:
        print("You are mad")
        print("IT IS CALLING MY NAME, the ancient one from the abyss, I cannot resist his voice.")
        print("All hail Cthulhu"*5)
        return False
    else:
        return True


def boss_fight(character):
    """
    Simulates a boss fight.

    :param character: a dictionary representing the player's character
    :return: True if the player wins the fight, False if lose the fight
    """
    print("The sea roars, and from its depths emerges the 'Lord of the Abyss', a creature of unspeakable horror.")
    print("Your HP, Sanity and Darkness ability have restored")
    character["Current HP"] = 13
    character["Sanity"] = 13
    character["Darkness"] = 7
    commands_descriptions = {
        "ac": "Ancient Chant - Breaks the defenses.",
        "eb": "Eldritch Blast - Unleashes powerful energy against the Eye.",
        "ms": "Mystic Shield - Temporarily boosts defense.",
        "ag": "Abyssal Gaze - Stares into the abyss, seizing an attack opportunity."
    }
    commands = ["ac", "eb", "ms", "ag"]
    for command in commands:
        print(f"{command} : {commands_descriptions[command]}")
    success_count = 0
    for count in range(3):  # Let's say there are 3 rounds in the boss fight
        command = input(f"Enter command {commands} to challenge the abyss: ")
        while command not in commands:
            command = input(f"Invalid command! Enter command {commands} to challenge the abyss: ")
        success_chance = character['Level'] + character['Darkness'] + character['Experience']
        if random.randint(1, 25) <= success_chance:
            print("Your courage shines, striking a blow against the abyssal horror!")
            success_count += 1
        else:
            print("Your attack falters. The 'Lord of the Abyss' retaliates with a wave of dark energy!")
            character["Current HP"] -= 2
            character["Sanity"] -= 1
        if character["Current HP"] <= 0:
            print("Engulfed by darkness, your journey ends in the jaws of the abyss.")
            return False
        if character["Sanity"] <= 0:
            print("Overwhelmed by the abyss, your mind succumbs to madness.")
            return False
    return success_count >= 2


def load_data(filename='game.json'):
    path = Path(filename)
    if path.is_file():
        with path.open('r') as file_object:
            return json.load(file_object)
    else:
        return {}


def save_data(data, filename='game.json'):
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)


def get_user_data(data, username):
    return data.get(username, None)


def create_new_user(data, username):
    data[username] = {'character': make_character(), 'level': 1}
    save_data(data)


def game(username, game_data):
    """
    Run the game.
    """
    user_data = get_user_data(game_data, username)
    if user_data:
        choice = input("Input 'ng' to start new game, or 'ct' to continue from last save: ")
        if choice == 'ng':
            character = make_character()
            user_data = {'character': character, 'level': 1}
    else:
        print("New user detected. Creating a new account...")
        character = make_character()
        user_data = {'character': character, 'level': 1}
        game_data[username] = user_data
        save_data(game_data)
    character = user_data['character']
    # level = user_data['level']
    while True:
        print("=" * 20)
        # level = character['Level']
        level = user_data['level']
        print(f"Day {level}")
        title_text = {1: "the Past Shadow", 2: "Mouth of Madness", 3: "Call of Cthulu"}
        print(f"{title_text[level]}")
        if_level_up = [False]
        board = make_board(character['Level'])
        while if_level_up[0] is False:
            achieved_goal = False
            while is_alive_and_sane(character) and not achieved_goal:
                current_room = describe_current_location(board, character)
                if current_room == "empty room":
                    direction = get_user_choice()
                else:
                    if current_room == "Totem":
                        activate_totem(character)
                    else:
                        read_runes(character)
                    direction = get_user_choice()
                if_level_up[0] = check_level_up(character)
                valid_move = validate_move(character, direction)
                while valid_move is False:
                    print("You can't go in that direction. Try another direction.")
                    direction = get_user_choice()
                    valid_move = validate_move(character, direction)
                move_character(character, direction)
                current_coordinate = (character["X-coordinate"], character["Y-coordinate"])
                if current_coordinate != (4, 4):
                    game_data[username] = {'character': character, 'level': character['Level']}
                    save_data(game_data)
                stranger = mad_or_prophet(character['Level'])
                if stranger == "Madness":
                    check_win(character)
                elif stranger == "Prophet":
                    check_learn(character, character['Level'])
                achieved_goal = check_if_goal_attained(character)
                if_level_up[0] = check_level_up(character)
                decide_text()
            if achieved_goal:
                if character['Level'] == 3:
                    if boss_fight(character):
                        print("With a final, valiant effort, you vanquish the 'Lord of the Abyss'. You survived.")
                    else:
                        print("Overwhelmed by the ancient terror, your fate is sealed.")
                    print("Game Over")
                    print("=" * 20)
                    return
                else:
                    if_level_up[0] = True
            if not is_alive_and_sane(character):
                print('Game Over')
                print("=" * 20)
                return
        if if_level_up[0] is True:
            current_level = character['Level'] + 1
            user_data['level'] = current_level
            character = make_character()
            character['Level'] = current_level
            character['Current HP'] += current_level
            character['Sanity'] += current_level
            character['Darkness'] += current_level
            game_data[username] = {'character': character, 'level': character['Level']}
            save_data(game_data)


def main():
    """
    Drives the program.
    """
    # game()
    game_data = load_data()
    username = input("Please enter your username: ")
    game(username, game_data)


if __name__ == "__main__":
    main()
