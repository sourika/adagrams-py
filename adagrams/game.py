from random import randint

LETTER_POOL_DISTRIBUTION = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2,
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2,
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1,
    'Y': 2, 'Z': 1
}

SCORES = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10
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
    total_score = 0
    for letter in word.upper():
        total_score += SCORES.get(letter, 0)
    
    word_length = len(word)
    if word_length >= 7 and word_length <= 10:
        total_score += 8    
    return total_score

def get_highest_word_score(word_list):
    score_dict = {}
    for word in word_list:
        score = score_word(word)
        score_dict[word] = score

    max_score = -1
    for score in score_dict.values():
        if score > max_score:
            max_score = score

    max_score_list_contenders = []
    for word, score in score_dict.items():
        if score == max_score:
            max_score_list_contenders.append(word)

    if len(max_score_list_contenders) == 1:
        return max_score_list_contenders[0], max_score

    for word in max_score_list_contenders:
        if len(word) == 10:
            return word, max_score  

    winner = max_score_list_contenders[0]
    min_len = len(winner)

    for i in range(1, len(max_score_list_contenders)):
        if len(max_score_list_contenders[i]) < min_len:
            min_len = len(max_score_list_contenders[i])
            winner = max_score_list_contenders[i]

    return winner, max_score