"""
Kim Zhang
A01374508
"""
import random

def die_of_rooms(level):
    room = random.randint(1,8)
    if room <= level:
        return "gate"
    elif room > 8 - level:
        return "runes"
    else:
        return "empty room"

def make_board(level):
    """
    Make a coordinate board.

    :param rows: an integer greater than or equal to 2
    :param columns: an integer greater than or equal to 2
    :precondition: must pass two parameters representing rows and columns
    :precondition: rows and columns must be integer greater than or equal to 2
    :postcondition: make a board consists of coordinate-description pairs
    :return: a dictionary with key-value pairs representing coordinate-description
    """
    board_template = {(row, column): die_of_rooms(level) for row in range(5) for column in range(5)}
    board_template[(0, 0)] = "empty room"
    return board_template


def make_character():
    """
    Make a character that has coordinate and HP.

    :precondition: must not pass any parameter
    :postcondition: make a dictionary representing a character with x and y coordinates and current HP
    :return: a dictionary with 6 key-value pairs

    >>> player = make_character()
    >>> player
    {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Sanity": 10, "Experience": 0, "Level": 1}
    """

    character_template = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Sanity": 10, "Experience": 0,
                          "Level": 1}
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
    print("Your current location is:", location, "it is:", board[location])
    return board[location]


def open_door(character):
    character["Current HP"] -= 1
    open_door_result = random.randint(1, 4)
    if open_door_result > 1:
        print("Door opened")
        character["Experience"] += 1
    else:
        print("Door is still closed. Try harder or try another direction")
    return character


def read_runes(character):
    read_runes_result = random.randint(1, 4)
    if read_runes_result > 1:
        print("Runes read. You hear the whispers of the stars, speaking of eternal darkness and the endless void.")
        character["Sanity"] -= 1
        character["Experience"] += 2
    else:
        print("You can't read the runes. 'Weird place.' You thought.")
    return character

def check_level_up(character):
    if character["Experience"] >= 10:
        character["Level"] += 1
        print("One day has passed")
        return True
    else:
        return False


def get_user_choice():
    """
    Obtain the user's choice for direction.

    :postcondition: Display and store the user's choice for character's moving direction
    :return: an integer from 1 to 4 (include both) representing the direction
    """
    direction_system = {1: "Up", 2: "Down", 3: "Left", 4: "Right"}
    print("_"*10)
    print(direction_system)
    choice = input("Please choose your direction, please only input numbers from 1 to 4:\n")
    while not choice.isnumeric():
        choice = input("Try again, please only input numbers from 1 to 4:\n")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Try again, please only input numbers from 1 to 4:\n")
    choice = int(choice)
    print("You choose to move:", direction_system[choice])
    print("_" * 10)
    return choice


def validate_move(board, character, direction):
    """
    Check if the character can move along the direction on the board.

    :param board: a dictionary with key-value pairs representing coordinate-description
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
    """
    Update the character's coordinate by making it move along the specified direction

    :param character: a dictionary representing a character with x-coordinate, y-coordinate and HP
    :param direction: an integer representing the direction that the character wants to move forward
    :precondition: character keys must be: "X-coordinate", "Y-coordinate", "Current HP"
    :precondition: direction must be in [1,2,3,4]
    :postcondition: update the character position by updating the values of "X-coordinate" and "Y-coordinate"
    :return: a dictionary representing the character's most updated coordinates and current HP
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
    meet_mad_or_prophet = random.randint(1, 8)
    if meet_mad_or_prophet <= level:
        print("When you turn the corner, you come face-to-face with wild, haunted eyes. A figure, shrouded in tattered clothes, shambles towards you, muttering incoherently. Their gaze is frenzied, and an unsettling chill runs down your spine. It's clear that this poor soul has succumbed to madness, their mind fractured by horrors unknown. With a sudden, startling energy, they lunge at you, driven by an unfathomable madness.")
        return "Madness"
    elif meet_mad_or_prophet > 8 - level:
        print("As you navigate the misty streets, you encounter a solitary figure. Cloaked in a robe adorned with arcane symbols, they stand eerily still. Their eyes, filled with an otherworldly knowledge, fix upon you. 'Seeker of truths,' they intone in a voice that seems to echo from a forgotten age, 'heed my words and be enlightened.' The air around them vibrates with a strange energy, and you sense that this prophet may unlock secrets that will guide your journey.")
        return "Prophet"
    else:
        print("The streets are eerily empty. Fog swirls around, casting shifting shadows, yet reveals no other soul. An unsettling quiet pervades, as if the town itself holds its breath, concealing secrets best left undiscovered.")
        return "Nobody"

def check_if_goal_attained(character):
    """
    Check if character has reached the bottom right hand corner.

    :param board: a dictionary with key-value pairs representing coordinate-description
    :param character: a dictionary representing a character with x-coordinate, y-coordinate and HP
    :precondition: board's keys must be coordinates in the form of (x , y)
    :precondition: character keys must be: "X-coordinate", "Y-coordinate", "Current HP"
    :postcondition: check if it is True that the character has reached the bottom right corner after last move
    :return: True if the character has reached the bottom right corner after the last move, False if it hasn't
    """
    current_location = (character["X-coordinate"], character["Y-coordinate"])
    goal_location = (4, 4)
    return current_location == goal_location

def check_win(character):
    chance = random.randint(1, 2)
    if chance == 1:
        print("You won")
        character["Experience"] += 2
    else:
        print("You lose")
    character["Current HP"] -= 2
    character["Sanity"] -= 1
    return

def check_learn(character, level):
    border = 2*level
    chance = random.randint(1, border)
    if chance == 1:
        print("The prophet, though tainted by otherworldly forces, imparts cryptic wisdom that resonates within you, enhancing your understanding and strengthening your resolve.")
        character["Experience"] += 2
        character["Sanity"] += 1
    else:
        print("As you approach, the prophet's form distorts unnaturally, their words dissolving into an incomprehensible babble, leaving you bewildered and no wiser than before.")
    return


def decide_text():
    text_generator = random.randint(1, 7)
    text_base = {1: "I hear the whispers of the stars, speaking of eternal darkness and the endless void.",
                 2: "Time is melting before my eyes, reality and dreams entwined, indistinguishable.",
                 3: "It's calling me, the ancient one from the abyss, I cannot resist its voice.",
                 4: "All is in vain, we are but insignificant specks in this cosmos.",
                 5: "I am unsure what is real anymore, or if my mind has been corrupted by the darkness.",
                 6: "Other worlds are calling me, I hear the summons from unknown realms.",
                 7: "Akhamna, Igwatius... these runes echo in my mind, I cannot stop them"}
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
        print("You are dead")
        return False
    elif character["Sanity"] <= 0:
        print("IT IS CALLING MY NAME, the ancient one from the abyss, I cannot resist his voice.")
        print("All hail Cthulhu"*5)
        return False
    else:
        return True


def game():
    """
    Run the game.
    """
    print("=" * 20)
    if_level_up = False
    while if_level_up == False:

    character = make_character(1)
    board = make_board()
    achieved_goal = False
    while is_alive_and_sane(character) and not achieved_goal:
        # Tell the user where they are
        current_room = describe_current_location(board, character)
        if current_room != "empty room":
            if current_room == "door":
                open_door(character)
            elif current_room == "runes":
                read_runes(character)
            if_level_up = check_level_up(character)

        else:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)
            achieved_goal = check_if_goal_attained(character)
            if achieved_goal:
                print("Congratulations! You made it!")
                print("Game Over")
                print("=" * 20)
        else:
            print("You can't go in that direction")
        if not is_alive(character):
            print("You are dead")
            print("Game Over")
            print("=" * 20)


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
