import random
wordlist = ['abort', 'basic', 'block', 'debug', 'crash', 'input', 'flash', 'forth', 'image', 'index', 'layer', 'linux', 'macro', 'octal', 'proxy', 'patch',  'stack']
word = random.choice(wordlist)

default = "\033[0m"
green = "\033[92m"
yellow = "\033[33m"

def gen_hint(word, guess):
    color = default
    hint = ""
    for i in range(5):
        if (guess[i] == word[i]):
            color = green
        elif (guess[i] in word):
            color = yellow
        else:
            color = default

        hint += color + guess[i] + default
    return hint

def game_loop():
    guess = ""
    for i in range(6):
        guess = input('Enter your 5-letter guess: ')
        if len(guess) != 5:
            print('Invalid guess. Try again.')
            continue
        if guess == word:
            print(f'You win! The word was {gen_hint(word, guess)}')
            break
        else:
            if i < 5:
                print(f'Try again. Hint: {gen_hint(word, guess)}')
            else:
                print(f'You lost. The word was {word}.')

game_loop()
