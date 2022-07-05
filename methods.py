from words import word_array, word_dict

def word_points (word):
    points = 0
    
    for answer_word in word_array:
        for letter in word:
            if letter in answer_word:
                points += answer_word.count(letter)
        for i in range(5):
            if answer_word[i] == word[i]:
                points += 2
    return points

def best_word ():

    default_word = word_array[0]

    for word in word_array:
        if word_points(word) > word_points(default_word):
            default_word = word

    return default_word

            