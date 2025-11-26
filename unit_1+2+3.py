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


def check_valid_input(letter_guessed, old_letters_guessed):
    is_valid = False
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        is_valid = True

    return is_valid


word = input("Please enter a word: ")
game = "_" * len(word)
print(" ".join(game))




def main():
     
if __name__ == '__main__':
    main()