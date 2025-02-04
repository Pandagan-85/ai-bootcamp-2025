import sys
import time
from random import randint
from utility import Player, Chart

def main():
    chart = Chart()  # Inizializza la classifica con punteggi salvati

    # Controllo degli argomenti
    if len(sys.argv) != 3:
        print("Uso: indica il range di numeri per cui vuoi provare a indovinare: num1 num2")
        sys.exit(1)

    while True:
        random_number = randint(int(sys.argv[1]), int(sys.argv[2]))
        attempts = 0  # Contatore dei tentativi
        start_time = time.time()  # Inizio della partita
        # timestamp Unix (Epoch Time, secondi dal 1 gen 1970)
        # gli alieni che ci hackereranno penseranno che siamo giovanissimi!
        # print(time.time()) > #1738655609.4065459

        while True:
            try:
                number = int(input(f"Choose a number between {sys.argv[1]} and {sys.argv[2]}: "))
                attempts += 1  # Incrementa il numero di tentativi

                if int(sys.argv[1]) <= number <= int(sys.argv[2]):
                    if number == random_number:
                        elapsed_time = round(time.time() - start_time, 2)  # Calcolo del tempo trascorso
                        best_player = chart.get_best_player()
                        best_score = best_player.p_attempts if best_player else None

                        name_player = input("Qual è il tuo nome? ")
                        new_player = Player(name=name_player, p_attempts=attempts, time_elapsed=elapsed_time)
                        chart.add(new_player)

                        if best_score is None or attempts < best_score:
                            print(f"🎉 New Record! {name_player} won in {attempts} attempts and {elapsed_time} seconds!")
                        elif attempts == best_score:
                            print(f"🎖️ Pareggio! {name_player} ha raggiunto il miglior punteggio di {attempts} tentativi!")
                        else:
                            print(f"No new record. Best player is: {best_player.name} with {best_score} attempts.")

                        print(f"You're a genius! You guessed the number in {attempts} attempts and {elapsed_time} seconds.")

                        keep_playing = input("Keep playing? y/n? ")
                        if keep_playing.lower() == "y":
                            break  # Ricomincia con un nuovo numero
                        else:
                            chart.print_ranking()  # Stampa la classifica alla fine
                            print("See yaaaa 👋")
                            return
                    elif number < random_number:
                        print("Too low! Try again.")
                    else:
                        print("Too high! Try again.")
                else:
                    print(f"Remember, your number must be between {sys.argv[1]} and {sys.argv[2]}!")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    main()