while True:
    user_input = input(">>> ").strip()

    if user_input.lower() == "quit":
        print("ciao, alla prossima!")
        break  # Esce dal loop
    try:
        # Dividere l'input in operandi e operatore
        # con la destrutturazione
        operand1, operator, operand2 = user_input.split()
        # Convertiamo in float per gestire sia interi che float
        operand1, operand2 = float(operand1), float(operand2)

        # Eseguire l'operazione
        if operator == "+":
            print(operand1 + operand2)
        elif operator == "-":
            print(operand1 - operand2)
        elif operator == "*":
            print(operand1 * operand2)
        elif operator == "/":
            if operand2 == 0:
                print("Errore: divisione per zero.")
            else:
                print(operand1 / operand2)
        else:
            print("Errore: operatore non supportato. Usa solo '+', '-', '*' o '/'.")
    except ValueError:
        print("Errore: formato non valido. Per favore usa il formato '123 + 345'.")
    except ZeroDivisionError:
        print("Errore: impossibile dividere per zero.")
    except Exception as e:
        print(f"Errore generico: {e}")