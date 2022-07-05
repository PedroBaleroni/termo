from words import word_array, word_dict
from unidecode import unidecode

def word_points (word,pool):
    points = 0
    
    for answer_word in pool:
        for letter in word:
            if unidecode(letter) in unidecode(answer_word):
                points += 1
        for i in range(5):
            if unidecode(answer_word[i]) == unidecode(word[i]):
                points += 2
    return points

def best_word (pool):

    default_word = pool[0]

    for word in word_array:
        print(default_word, word)
        if word_points(word, pool) > word_points(default_word, pool):
            default_word = word

    return default_word


def remove_words (pool_array, guess, answer):
    print("Guess: {}".format(guess))
    print("Answer: {}".format(answer[0]))
    pool = pool_array.tolist()
    if guess not in word_array:
        guess = word_dict[guess]
    remove_pool = []
    for word in pool:
        print(word)
        i =0
        for i in range(len(guess)):
            if answer[i] == 2:
                if(unidecode(word[i]) != unidecode(guess[i])):
                    remove_pool.append(word)
            elif answer[i] == 1:
                if(unidecode(word[i]) == unidecode(guess[i])):
                    remove_pool.append(word)
                if not (unidecode(guess[i]) in unidecode(word)):
                    remove_pool.append(word)
            elif answer[i] == 0:
                if guess[i] in unidecode(word):
                    remove_pool.append(unidecode(word))
    for words in remove_pool:
        pool.remove(words)
    return pool
            
        

            