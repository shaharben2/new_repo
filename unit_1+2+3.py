HANGMAN_ASCII_ART = """welcome to the game Hangman\n   
  _    _                                         
 | |  | |                                        	
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/\n"""
MAX_TRIES = 6

print (HANGMAN_ASCII_ART, MAX_TRIES)

print("""x-------x""")
					 
print("""    
    x-------x
    |
    |
    |
    |
    |""")
					 
print("""
    x-------x
    |       |
    |       0
    |
    |
    |""")
					 
print("""
    x-------x
    |       |
    |       0
    |       |
    |
    |""")
					 
print("""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |""")
					 
print("""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""")
	
print("""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |""")

def is_valid_input(letter_guessed):
    """this function checks if the input letter of the user is valid
    :param letter_guessed: the input letter from the user
    :type letter_guessed: string
    :return: True if the input is valid or False if not
    :rtype: bool"""
    is_valid = True
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        is_valid = False
    
    return is_valid

word = input("Please enter a word: ")
game = "_" * len(word)
print(" ".join(game))