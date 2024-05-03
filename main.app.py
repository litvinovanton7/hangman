import random
from hangman import draw_hangman


def random_word():
    try:
        with open('wordsDB/words.txt') as file:
            words = file.read().split()

            return random.choice(words)
    except FileNotFoundError:
        print('Error... File not found')


def check_letter(letter):
    return letter.isalpha() and len(letter) >= 0

def game():
    word = random_word().lower()
    hidden_word = list('*' * len(word))
    fail = 0
    game_result = ''

    print(word)

    while True:
        letter = input('Input a letter: ').lower()

        if not check_letter(letter):
            print('Please input correct letter -_- ')
            continue

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            print(''.join(hidden_word))
        else:
            print(draw_hangman(fail))
            fail += 1

        if '*' not in hidden_word:
            game_result = 'Congratulation! You guessed the word'
            break
        elif fail == 7:
            game_result = f'Sorry, you lost. The word was {word}'
            break

    return game_result


if __name__ == '__main__':
    print(game())
