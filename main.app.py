import random


def random_word():
    try:
        with open('wordsDB/words.txt') as file:
            words = file.read().split()

            return random.choice(words)
    except FileNotFoundError:
        print('Error')


if __name__ == '__main__':
    print(random_word())