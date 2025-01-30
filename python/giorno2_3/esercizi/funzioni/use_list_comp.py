# Studio delle list comprehension
"""
Una list comprehension** in Python
è una sintassi compatta e concisa per
creare una lista a
partire da un’altra sequenza
"""

import timeit
def pow_list_2(seq:list) -> list:
    """
        given a list, return a list with each value
        raised to the power of 2
    """
    return [x ** 2 for x in seq]

print("pow_list_2: ", pow_list_2([1,2,3]))


def sum_even_numbers_2(seq) :
    """
    return the sum of all even number is the list passed
    """
    return sum(el for el in seq if el % 2 == 0)

print("sum_even_2: ",sum_even_numbers_2([1,2,3,4,5,6,7,1000]))



def count_vowels_2(quote):
    vowels = "aeiou"
    return sum(1 for char in quote if char in vowels)

print("count_vowels_2: ", count_vowels_2("abc def ghi lmn opq rst uvz"))

## Test timeit
def sum_even_numbers(seq) :
    """
    return the sum of all even number is the list passed
    """
    even = []
    for n in seq:
        if n % 2 == 0:
            even.append(n)

    return sum(even)

## Test di velocità

# Eseguire il test di tempo per le due funzioni
seq = list(range(100))  # Definisco la sequenza da passare alle funzioni

# Misura il tempo di esecuzione della funzione 1
time_func1 = timeit.timeit('sum_even_numbers(seq)', globals=globals(), number=1000)
print(f"Tempo per func1: {time_func1} secondi")

# Misura il tempo di esecuzione della funzione 2
time_func2 = timeit.timeit('sum_even_numbers_2(seq)', globals=globals(), number=1000)
print(f"Tempo per func2: {time_func2} secondi")
