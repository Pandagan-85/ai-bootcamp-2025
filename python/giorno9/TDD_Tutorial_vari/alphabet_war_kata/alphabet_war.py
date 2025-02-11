
def alphabet_war(fight):
    """
    left side letters, and score:
    w  = 4, p = 3, b = 2, s = 1
    Right side letters and score:
    m =4 ,q =3, d = 2, z = 1
    Other letters are 0 points
    `*` is a bomb kill adiacent letters:
    `aa*aa => a___a
    :param fight: string of letter
    :return: string with comunication
    """
    battlefield = list(fight)
    for i, char in enumerate(fight):
        if char == "*":
            if i > 0:
                battlefield[i - 1] = "_"  # Lettera a sinistra della bomba
            battlefield[i] = "_"  # La bomba stessa
            if i < len(fight) - 1:
                battlefield[i + 1] = "_"  # Lettera a destra della bomba

    clean_fight = "".join(battlefield).replace("_", "")

    # 2. Definire i punteggi delle lettere
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    # 3. Calcolare i punteggi
    left_score = sum(left_side.get(char, 0) for char in clean_fight)
    right_score = sum(right_side.get(char, 0) for char in clean_fight)

    # 4. Determinare il vincitore
    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"

