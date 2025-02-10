import re
# tutorial https://www.youtube.com/watch?v=R1VYSFQcKsQ

def stringcalculator(param):
    if not param:
        return 0
    # Usa una regex per dividere sia su ',' che su '\n'
    numeri = re.split(r"[,\n]", param)
    # Controllo negativi
    negativi = [num for num in numeri if int(num) < 0]

    if negativi:
        raise ValueError(f"Negatives not allowed: {', '.join(negativi)}")
    """
    if len(numeri) < 2:
        return int(param)
    elif len(numeri) == 2:
        num1 = int(numeri[0])
        num2 = int(numeri[1])
        return num1 + num2
    elif len(numeri)==3:
        num1 = int(numeri[0])
        num2 = int(numeri[1])
        num3 = int(numeri[2])
        return num1 + num2 + num3
    """
    return sum(int(num) for num in numeri if int(num) <= 1000)

