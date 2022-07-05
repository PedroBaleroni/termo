from words import word_array, word_dict
from unidecode import unidecode
import random

def valid_word (word):
    if len(word) > 5:
        print("A palavra deve ter no máximo 5 letras")
        return

    if word in word_array:
        return True
    else:
        if word in word_dict:
            return True
        else:
            print("A palavra não existe")
            return False

def receive_word (raw_word):
    print(unidecode(raw_word))
    if(valid_word(unidecode(raw_word))):
        return unidecode(raw_word) 

def pick_random_word ():
    return word_array[random.randint(0, len(word_array) - 1)]

def win_condition (word, asnwer):
    if unidecode(word) == unidecode(asnwer):
        return True
    else:
        return False

def present_word (word, answer):
    distinctive_letters = {}
    response = [0,0,0,0,0]
    for letter in answer:
        if letter not in distinctive_letters:
            distinctive_letters[letter] = 1
        else:
            distinctive_letters[letter] += 1
    for i in range(5):
        if word[i] == answer[i]:
            response[i] = 2
            distinctive_letters[word[i]] -= 1
    for i in range(5):
        if not response[i]>0:
            if word[i] in distinctive_letters:
                response[i] = 1
                distinctive_letters[word[i]] -= 1
            else:
                response[i] = 0
    print(response)

def game():
    answer = pick_random_word()
    print(answer)

    for i in range(6):
        word = receive_word(input("Digite uma palavra: "))
        if win_condition(word, answer):
            print("Você ganhou!")
            break
        else:
            present_word(word, answer)
    print("Fim de jogo :(")

        