import random
from hangman import Hangman


# Return random word
def get_word(array_words):
    return random.choice(array_words)


# Return letter position
def get_position(letter, word_key_value):
    position = []

    for index, value in word_key_value:
        if value == letter:
            position.append(index)

    return position


# Format word
def format_word(word):
    string = ''

    for c in word:
        string += c + " "

    return string


def main():
    array_words = []
    hit = miss = 0
    array_hit = []
    array_miss = []
    aux = []

    enf = Hangman()

    with open('palavras.txt', 'r') as words:
        for w in words:
            # Removing "\n"
            w = w.replace("\n", "")
            w = w.strip()
            array_words.append(w)

    word = get_word(array_words)
    word_key_value = list(enumerate(word))

    # Starting aux
    for l in word:
        aux.append("_")

    print("\nWelcome to HangMan!\n")

    while True:
        # print hangman
        enf.get_man(miss)

        # print array miss
        if array_miss:
            print("\nWrong letters: " + format_word(array_miss))

        # print currently word board
        print("\n" + format_word(aux))

        letter = input("\nPress and confirm a letter: ")

        if letter in array_miss or letter in array_hit:
            print("This letter was already used.")
            pass
        else:
            if letter in word:
                position = get_position(letter, word_key_value)

                # updating aux
                for pos in position:
                    aux[pos] = letter

                # updating hit
                hit += len(position)
                array_hit.append(letter)

                if hit == len(word):
                    enf.get_win()
                    print("\nWord: " + word)
                    break
                else:
                    pass
            else:
                miss += 1
                array_miss.append(letter)

                if miss == 6:
                    # print hangman
                    enf.get_man(miss)
                    enf.get_game_over()
                    print("\nWord: " + word)
                    break
                else:
                    pass


if __name__ == '__main__':
    main()
