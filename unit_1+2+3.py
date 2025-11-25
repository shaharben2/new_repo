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

guess = input("Guess a letter: ")
print(guess.lower())

word = input("Please enter a word: ")
game = "_" * len(word)

print(" ".join(game))