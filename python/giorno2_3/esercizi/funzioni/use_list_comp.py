# Studio delle list comprehension
"""
Una list comprehension** in Python
è una sintassi compatta e concisa per
creare una lista a
partire da un’altra sequenza
"""
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