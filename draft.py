
def game():
# make_character()
#  ONLY ASK FOR LEVEL INPUT WHEN FIRST START!!!!!
# make a 5x5 board make_board(level)
# character goal =  not achieved
# tell if character live and sane with is_alive_and_sane(character) (T/F)
# if T:
# check GOAL_ATTAINED(character) (T/F) if T: END GAME
# if T:
# describe_current_location
# check if current is EMPTY OR DOOR OR RUNES
# if current location is "door": OPEN_DOOR
# if current location is "runes": READ_RUNES
# check if level up (T/F): if T: back to make_board(level+1). else go to show system
# if EMPTY:
# print to show the system of direction
# GET_CHOICE() ask for user's choice
# validate if user can move towards the chosen direction with VALIDATE_MOVE(character, choice)
# if cant, repeat until user can
# character moves into the new room with MOVE_CHARACTER(character, choice)
# tell if meet Madness; Prophets; or nothing with MAD_OR_PROPHET(level) <INFLUENCED BY LEVEL>
# if meet Madness/Propehts: tell if win the fight with CHECK_WIN(character) or tell if win the fight with
# CHECK_LEARN(character)
# check if level up
# if T, back to make_board; if F, back to "live and sane check"

def main():
    pass


if __name__ == '__main__':
    main()
