"""
Kim Zhang
A01374508
"""

import json
import random
from pathlib import Path


def die_of_rooms(level):
    """
    Generates a random room based on the level.

    This function generate a random room type. The type of room generated depends on the level of the character. The
    higher the level is, the higher the chance of encountering 'Totem' or 'runes' will be.

    :param level: a positive integer representing for the level of the character.
    :precondition: level must be a positive integer between 1 and 3, inclusive.
    :postcondition: generate a room type between "Totem", "runes" and "empty room" based on the level.
    :return: A string representing the type of room generated.
    """
    room = random.randint(1, 8)
    if room <= level:
        return "Totem"
    elif room > 8 - level:
        return "runes"
    else:
        return "empty room"


def make_board(level):
    """
    Generates a 5x5 game board with various room types based on the level.

    This function creates a dictionary representing a game board, where each key is a coordinate tuple (row, column),
    and value is a string of room type. The starting room (0,0) is always 'empty room'.

    :param level: a positive integer representing the level of the character.
    :precondition: level must be a positive integer between 1 and 3, inclusive.
    :postcondition: generate a dictionary where each key is a coordinate and each value is a room type.
    :return: A dictionary representing a 5x5 game board.
    """
    board_template = {(row, column): die_of_rooms(level) for row in range(5) for column in range(5)}
    board_template[(0, 0)] = "empty room"
    return board_template


def make_character():
    """
    Make a character that has coordinate and HP.

    :precondition: must not pass any parameter
    :postcondition: make a dictionary representing a character with x and y coordinates, current HP, Sanity,
    Experience, Darkness and Level
    :return: a dictionary with 7 key-value pairs, representing the initialized character

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Sanity': 10, 'Experience': 0, 'Darkness': 4, 'Level': 1}
    """
    character_template = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Sanity": 10, "Experience": 0,
                          "Darkness": 4, "Level": 1}
    return character_template


def describe_current_location(board, character):
    """
    Shows character's current location and its description.

    :param board: a dictionary which each key is a coordinate and each value is a room type
    :param character: a dictionary representing a character
    :precondition: must pass two dictionaries
    :postcondition: shows the current coordinate location of character and the location's description
    :return: a string representing the description of the current location's room type
    """
    coordinate_x = character["X-coordinate"]
    coordinate_y = character["Y-coordinate"]
    location = (coordinate_x, coordinate_y)
    red_location = "\033[91m{}\033[0m".format(location)
    print(f"Your current location is: {red_location} it is: {board[location]}")
    return board[location]


def activate_totem(character):
    """
    Attempts to activate a totem with player's input.

    This function ask the player for input command 'at' to activate a totem. If the command is correct, the function
    then randomly determines if the totem is activated successfully based on the character's 'Darkness' attribute.
    Then the character's status is updated based on the result.

    :param character: A dictionary representing a character, containing 'Current HP', 'Darkness', and other attributes.
    :precondition: character must be a dictionary with 'Current HP' and 'Darkness' as keys.
    :postcondition: Updates the character's HP and experience based on if the totem activation is success.
    :return: An updated dictionary representing for the character after encountering the Totem.
    """
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
    """
    Attempts to read runes with player's input.

    This function allows a player to try reading runes. It asks the player to enter a command 'rr'. If the command is
    correct, the function then uses a random chance which related to the character's Darkness to decide if the player
    successfully reads the runes. If successful, the character loses sanity but gains experience.

    :param character: A dictionary representing the character, with 'Sanity', 'Darkness', and other attributes.
    :precondition: character should be a dictionary with 'Sanity' and 'Darkness' as keys.
    :postcondition: Changes the character's sanity and experience based on whether the runes are read successfully.
    :return: An updated dictionary representing for the character after encountering the rune.
    """
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
    """
    Checks if the character can level up.

    This function looks at the character's level and experience. If the level is less than 3 and experience is 10
    or more, the character can level up. The function returns True or False based on whether level up.

    :param character: A dictionary representing the character, with 'Level', 'Experience', and other attributes.
    :precondition: character should be a dictionary with 'Level' and 'Experience' as keys.
    :return: True if the character can level up, False if not.

    >>> check_level_up({"Level": 2, "Experience": 10})
    True
    >>> check_level_up({"Level": 1, "Experience": 9})
    False
    """
    if character['Level'] < 3 and character["Experience"] >= 10:
        return True
    else:
        return False


def get_user_choice():
    """
    Asks the player to pick a direction.

    This function shows four directions: North, South, West, and East. The player picks a direction by typing a number
    (1 to 4, inclusive). If the player types something else, the function asks again. It keeps asking until the player
    picks correctly.

    :precondition: should pass 0 arguments to the function.
    :postcondition: verify if player's choice is valid (a positive integer in 1 to 4, inclusive), and get the valid
    choice of direction
    :return: the integer the player picks that matches a direction.
    """
    direction_system = {1: "North", 2: "South", 3: "West", 4: "East"}
    red_system = "\033[91m{}\033[0m".format(direction_system)
    print("_" * 10)
    print("{}".format(red_system))
    while True:
        try:
            choice = int(input("Please choose your direction, please only input numbers from 1 to 4:\n"))
        except ValueError:
            print("{}".format("Invalid input. Please enter a number."))
        else:
            if choice in [1, 2, 3, 4]:
                print("You choose to move: {}".format(direction_system[choice]))
                print("_" * 10)
                return choice
            else:
                print("{}".format("Input must be a number from 1 to 4. Try again."))


def validate_move(character, direction):
    """
    Check if the character can move along the direction on the board.

    This function checks whether a character can move in a given direction based on their current coordinates.
    Directions are represented by integers: 1 for North, 2 for South, 3 for West, and 4 for East.

    :param character: A dictionary representing a character with 'X-coordinate', 'Y-coordinate', and other attributes.
    :param direction: An integer (1, 2, 3, 4) representing the direction of the incoming movement.
    :precondition: character must have 'X-coordinate' and 'Y-coordinate' keys with integer values from 0 to 4,
    inclusive.
    :precondition: direction must be an integer in [1, 2, 3, 4].
    :postcondition: Evaluates if the movement in the specified direction is possible within a 5x5 grid.
    :return: True if the character can move in the specified direction, False otherwise.

    >>> validate_move({"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,"Darkness": 4, "Level": 1}, 1)
    True
    >>> validate_move({"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,"Darkness": 4, "Level": 1}, 1)
    False
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
    """
    Moves the character to a direction.

    This function changes the character's position. Directions are numbers: 1 for North, 2 for South, 3 for West,
    4 for East. The function updates the character's 'X-coordinate' or 'Y-coordinate' based on the direction.

    :param character: A dictionary with the character's 'X-coordinate' and 'Y-coordinate' and other details.
    :param direction: An integer (1, 2, 3, 4) that shows which direction to move.
    :precondition: character must be a dictionary with 'X-coordinate' and 'Y-coordinate' and other keys.
    :precondition: direction must be a number from 1 to 4, inclusive.
    :postcondition: Updates the character's position based on the direction.

    >>> my_character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,"Darkness": 4, "Level": 1}
    >>> move_character(my_character, 1)
    >>> my_character
    {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 10, 'Sanity': 10, 'Experience': 0, 'Darkness': 4, 'Level': 1}
    """
    if direction == 1:
        character["X-coordinate"] -= 1
    elif direction == 2:
        character["X-coordinate"] += 1
    elif direction == 3:
        character["Y-coordinate"] -= 1
    elif direction == 4:
        character["Y-coordinate"] += 1


def mad_or_prophet(level):
    """
    Decides if player meet a Madness, a Prophet or Nobody.

    This function randomly decides who player meets based on character's level. If level is high, the character is more
    likely to meet a prophet. If not, the character might meet a mad person or nobody. Then It tells player some
    background text about whom the character meets.

    :param level: An integer from 1 to 3 (inclusive) representing character's level.
    :precondition: level must be a positive integer from 1 to 3, inclusive.
    :postcondition: prints a text description about the person you meet.
    :return: A string 'Madness', 'Prophet', or 'Nobody' representing who the player meets.
    """
    meet_mad_or_prophet = random.randint(1, 8)
    if meet_mad_or_prophet <= level:
        mad_text = ("When you turn the corner, you come face-to-face with wild, haunted eyes. "
                    "A figure, shrouded in tattered clothes, shambles towards you, muttering incoherently. "
                    "Their gaze is frenzied, and an unsettling chill runs down your spine. "
                    "It's clear that this poor soul has succumbed to madness, their mind fractured by horrors unknown. "
                    "With a sudden, startling energy, they lunge at you, driven by an unfathomable madness.")
        print("{}".format(mad_text))
        return "Madness"
    elif meet_mad_or_prophet > 8 - level:
        prophet_text = ("As you navigate the misty streets, you encounter a solitary figure. "
                        "Cloaked in a robe adorned with arcane symbols, they stand eerily still. "
                        "Their eyes, filled with an otherworldly knowledge, fix upon you. "
                        "'Seeker of truths,' they intone in a voice that seems to echo from a forgotten age, "
                        "'heed my words and be enlightened.' "
                        "The air around them vibrates with a strange energy, "
                        "and you sense that this prophet may unlock secrets that will guide your journey.")
        print("{}".format(prophet_text))
        return "Prophet"
    else:
        nobody_text = ("The streets are eerily empty. "
                       "Fog swirls around, casting shifting shadows, yet reveals no other soul. "
                       "An unsettling quiet pervades, as if the town itself holds its breath, "
                       "concealing secrets best left undiscovered.")
        print("{}".format(nobody_text))
        return "Nobody"


def check_if_goal_attained(character):
    """
    Check if character has reached the bottom right hand corner.

    :param character: a dictionary representing a character with x-coordinate, y-coordinate and other attributes.
    :precondition: character keys must have: "X-coordinate", "Y-coordinate".
    :postcondition: check if it is True that the character has reached the bottom right corner (4, 4) after a move
    :return: True if the character has reached the bottom right corner after a last move, False if it hasn't
    """
    current_location = (character["X-coordinate"], character["Y-coordinate"])
    goal_location = (4, 4)
    return current_location == goal_location


def check_win(character):
    """
    Decides if the character wins or loses a fight against Madness.

    This function lets a character fight Madness. The player must enter a command ('fm') to start the fight.
    Then it uses a random chance, based on the character's 'Darkness' level, to decide if the character wins.
    If the character wins, they gain experience. Either way, the character loses some health and sanity.

    :precondition: The character must have 'Current HP', 'Sanity', and 'Darkness' as keys in its dictionary.
    :postcondition: Updates the character's 'Current HP', 'Sanity', and 'Experience' based on the fight's result.
    :return: None. This function updates the character's attributes but does not return anything.
    """
    red_fm = "\033[91m" + "fm" + "\033[0m"
    validation_fight = input(f"input {red_fm} to fight with the Madness: \n")
    while validation_fight != "fm":
        validation_fight = input(f"input {red_fm} to fight with the Madness: \n")
    chance_win = character['Darkness']
    chance = random.randint(1, chance_win)
    if chance >= 3:
        print("{}".format("You won"))
        character["Experience"] += 2
    else:
        print("{}".format("You lose"))
    character["Current HP"] -= 2
    character["Sanity"] -= 1
    return


def check_learn(character, level):
    """
    Decides if the character learns from the Prophet.

    :precondition: The character must have 'Experience' and 'Sanity' as keys in its dictionary.
    :precondition: level must be a positive integer.
    :postcondition: Updates the character's 'Experience' and 'Sanity' based on whether they learn from the Prophet.
    """
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
        print("{}".format(text_learn_runes))
        print("{}".format("runes learnt"))
        character["Experience"] += 2
        character["Sanity"] += 1
    else:
        print("{}".format("runes not learnt"))
        text_not_learnt = ("As you approach, the prophet's form distorts unnaturally, "
                           "their words dissolving into an incomprehensible babble, "
                           "leaving you bewildered and no wiser than before.")
        print("{}".format(text_not_learnt))
    return


def decide_text():
    """
    Prints a random text for game background.
    """
    text_generator = random.randint(1, 6)
    text_base = {1: "I hear the whispers of the stars, speaking of eternal darkness and the endless void.",
                 2: "Time is melting before my eyes, reality and dreams entwined, indistinguishable.",
                 4: "All is in vain, we are but insignificant specks in this cosmos.",
                 5: "I am unsure what is real anymore, or if my mind has been corrupted by the darkness.",
                 6: "Other worlds are calling me, I hear the summons from unknown realms.",
                 3: "Akhamna, Igwatius... these runes echo in my mind, I cannot stop them"}
    print("{}".format(text_base[text_generator]))
    return


def is_alive_and_sane(character):
    """
    Check if the character is alive and sane.

    :param character: A dictionary representing a character with attributes like 'Current HP' and 'Sanity'.
    :precondition: character must be a dictionary containing "Current HP" and "Sanity" as keys.
    :postcondition: Checks if the character's 'Current HP' is > 0 and 'Sanity' is > 0.
    :return: True if the character is both alive and sane, False otherwise.
    """
    if character["Current HP"] <= 0:
        print("{}".format("You are dead of low HP"))
        return False
    elif character["Sanity"] <= 0:
        print("{}".format("You are mad"))
        print("{}".format("IT IS CALLING MY NAME, the ancient one from the abyss, I cannot resist his voice."))
        print("{}".format("All hail Cthulhu"*5))
        return False
    else:
        return True


def boss_fight(character):
    """
    Simulates a boss fight.

    :param character: a dictionary representing the player's character
    :precondition: character must be a dictionary with keys: "Current HP", "Sanity", "Darkness", 'Level', "Experience"
    :postcondition: tells if player wins the fight
    :return: True if the player wins the fight, False if lose the fight
    """
    print("{}".format("The sea roars, and from its depths emerges the 'Lord of the Abyss', a creature of unspeakable "
                      "horror."))
    print("{}".format("Your HP, Sanity and Darkness ability have restored"))
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
    for index, command in enumerate(commands):
        print(f"{command} : {commands_descriptions[command]}")
    success_count = 0
    for count in range(3):
        command = input(f"Enter command {commands} to challenge the abyss: ")
        while command not in commands:
            command = input(f"Invalid command! Enter command {commands} to challenge the abyss: ")
        success_chance = character['Level'] + character['Darkness'] + character['Experience']
        if random.randint(1, 25) <= success_chance:
            print("{}".format("Your courage shines, striking a blow against the abyssal horror!"))
            success_count += 1
        else:
            print("{}".format("Your attack falters. The 'Lord of the Abyss' retaliates with a wave of dark energy!"))
            character["Current HP"] -= 2
            character["Sanity"] -= 1
        if character["Current HP"] <= 0:
            print("{}".format("Engulfed by darkness, your journey ends in the jaws of the abyss."))
            return False
        if character["Sanity"] <= 0:
            print("{}".format("Overwhelmed by the abyss, your mind succumbs to madness."))
            return False
    return success_count >= 2


def load_data(filename='game.json'):
    """
    Loads game data from a file.

    :param filename: The name of the file to load data from, default value is 'game.json'.
    :postcondition: loads data from the file if it exists.
    :return: A dictionary which is the data from the file, or an empty dictionary if the file does not exist.
    """
    path = Path(filename)
    if path.is_file():
        with path.open('r') as file_object:
            return json.load(file_object)
    else:
        return {}


def save_data(data, filename='game.json'):
    """
    Saves game data to a file.

    :param data: the game data to be saved.
    :param filename: The name of the file to save data to, default value is 'game.json'.
    :precondition: data must be a valid dictionary
    :postcondition: writes the given data to the specified file 'game.json' in JSON.
    """
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)


def get_user_data(data, username):
    """
    Gets a user's data with the given username.

    :param data: a dictionary representing for the game data.
    :param username: a string representing for a username
    :precondition: data must be a dictionary
    :precondition: username must be a string
    :postcondition: get the user data from the game data if the user exists.
    :return: If can find the user's data, return the user's data, otherwise, return None.
    """
    return data.get(username, None)


def create_new_user(data, username):
    """
    Creates a new user and save it in the game data.

    :param data: a dictionary representing for the game data.
    :param username: a string representing for a username
    :precondition: data must be a dictionary
    :precondition: username must be a string
    :postcondition: a new user added to the game data and saves the updated data.
    """
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
        print("{}".format("New user detected. Creating a new account..."))
        character = make_character()
        user_data = {'character': character, 'level': 1}
        game_data[username] = user_data
        save_data(game_data)
    character = user_data['character']
    while True:
        print("=" * 20)
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
                    print("{}".format("You can't go in that direction. Try another direction."))
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
                        print("{}".format("With a final, valiant effort, you vanquish the 'Lord of the Abyss'. You "
                                          "survived."))
                    else:
                        print("{}".format("Overwhelmed by the ancient terror, your fate is sealed."))
                    print("{}".format("Game Over"))
                    print("=" * 20)
                    return
                else:
                    if_level_up[0] = True
            if not is_alive_and_sane(character):
                print("{}".format('Game Over'))
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
    game_data = load_data()
    username = input("Please enter your username: ")
    game(username, game_data)


if __name__ == "__main__":
    main()
