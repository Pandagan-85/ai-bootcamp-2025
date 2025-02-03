import sys
from random import randint

# Controllo degli argomenti
if len(sys.argv) != 3:
    print("Uso: indica il range di numeri per cui vuoi provare a indovinare num1, num2")
    sys.exit(1)

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))
attempts = 0  # Contatore dei tentativi


while True:
    try:
        number = int(
            input(f'Please choose a number that falls {sys.argv[1]} and {sys.argv[2]}: '))
        attempts += 1  # Incrementa il numero di tentativi

        if int(sys.argv[1]) <= number <= int(sys.argv[2]):
            if number == random_number:
                print(f"You're a genius! You guessed the number in {attempts} attempts.")
                break
            elif number < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        else:
            # printo un errore se si digita un numero fuori range
            print(f"Remember, your number must be between {sys.argv[1]} and {sys.argv[2]}!")
    except ValueError:
        # printo un errore se non si digita un numero
        print("Please enter a number")
        continue