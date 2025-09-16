from random import randint

LETTER_POOL_DISTRIBUTION = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2,
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2,
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1,
    'Y': 2, 'Z': 1
}

LETTER_POOL_LIST = []
for letter, quantity in LETTER_POOL_DISTRIBUTION.items():
    for _ in range (quantity):
        LETTER_POOL_LIST.append(letter) 


def draw_letters():
    copy_list = list(LETTER_POOL_LIST)
    hand = []       
    hand_length = 10
        
    for _ in range(hand_length):
        current_len = len(copy_list)
        random_index = randint(0, current_len - 1)
        letter = copy_list.pop(random_index)
        hand.append(letter)
    
    return hand    


def uses_available_letters(word, letter_bank):
    count_letters = {}

    for letter in letter_bank:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

    for letter in word.upper():
        if letter in count_letters and count_letters[letter] > 0:
            count_letters[letter] -= 1
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass