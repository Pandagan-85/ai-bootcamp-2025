import random

def run_guess(guess, answer):
    if not isinstance(guess, int):  # Controlla se il guess non è un intero
        raise ValueError("Per favore inserisci un numero valido")

    if 0 < guess < 11:
        if guess == answer:
            print('Sei un genio')
            return True
    else:
        print('Hei! devi inserire un numero tra 1 e 10')
        return False
if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('Indovina un numero tra 1 e 10 '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('Per favore inserisci un numero')
            continue





