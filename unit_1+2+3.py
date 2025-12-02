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

HANGMAN_PHOTOS = {0 : """x-------x""", 1 : """    
    x-------x
    |
    |
    |
    |
    |""", 2 : """
    x-------x
    |       |
    |       0
    |
    |
    |""", 3 : """
    x-------x
    |       |
    |       0
    |       |
    |
    |""", 4 : """
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |""", 5 : """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |""", 6 : """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |"""}

print (HANGMAN_ASCII_ART, MAX_TRIES)

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

def check_valid_input(letter_guessed, old_letters_guessed):
    is_valid = False
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        is_valid = True

    return is_valid

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    is_valid = check_valid_input(letter_guessed, old_letters_guessed)
    if is_valid:
        old_letters_guessed.append(letter_guessed)
    else:
        print("X")
        print(sorted(old_letters_guessed))

    print(is_valid)


word = input("Please enter a word: ")
game = "_" * len(word)
print(" ".join(game))


def show_hidden_word(secret_word, old_letters_guessed):
    gussed_by_now = ""
    for num in range(len(secret_word)):
        if secret_word[num] not in old_letters_guessed:
            gussed_by_now += "_"
        else:
            gussed_by_now += secret_word[num]

    return " ".join(gussed_by_now)


def check_win(secret_word, old_letters_guessed):
    has_won = True
    for num in range(len(secret_word)):
        if secret_word[num] not in old_letters_guessed:
            has_won = False

    return has_won


def choose_word(file_path, index):
    file = open(file_path, "r")
    file_read = file.read()
    file.close()
    names_list = file_read.split(" ")
    num_unique_words = len(list(set(names_list)))
    real_idx = (index - 1) % len(names_list)
    return (num_unique_words, names_list[real_idx])

def main():



if __name__ == '__main__':
    main()


    