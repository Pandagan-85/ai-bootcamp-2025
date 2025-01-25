# Scrivere il codice dell'esercizi qui dentro
def  mydivmod(a,b):
    """
    Return the tuple (x//y, x%y), trowing error if `b = 0`
    """
    if b == 0:
        raise ZeroDivisionError("Errore: Non è possibile dividere per zero!")
    result = (a//b, a%b)
    return result


print(mydivmod(5,2))

def pow_list(seq: list) -> list:
    """
    given a list, return a list with each value
    raised to the power of 2
    """
    seq2 = []
    for el in seq:
        seq2.append(el ** 2)
    return seq2

print("pow_list: ", pow_list([1,2,3]))

# ops ho fatto un conta caratteri e non parola XD
def count_characters(quote):
    """
    return the count of each letter
    """
    i = 0
    for word in quote:
        for character in word:
            i+=1
    return i
print("count_characters: ", count_characters("ciao ciao ciao, dsf"))

def count_words(words):
    """
    return the count of words of the given sentence
    """
    return len(words.split(" "))

print("count_words: ", count_words("ciao ciao ciao"))

def reverse_string(quote):
    """
    return a given in string in reversed order
    """
    return quote[::-1]


print("reverse_string: ", reverse_string("ciao maria"))

def factorial(n):
    """
    return the factorial of a give number
    """
    result = 1
    for number in range(1,n+1): # start valore incluso, stop escluso
        result = result * number
    return result
print("factorial: ",factorial(5))

def is_palindrome(word):
    """
    check if the given string is a palindrome
    """
    if word == word[::-1]:
        print("Wow è un palindromo")
        return True
    else:
        print("Non è un palindromo :(, prova con un'altra parola")
        return False

is_palindrome("racecar")

def sum_even_numbers(seq) :
    """
    return the sum of all even number is the list passed
    """
    even = []
    for n in seq:
        if n % 2 == 0:
            even.append(n)

    return sum(even)

print("sum_even: ",sum_even_numbers([1,2,3,4,5,6,7,1000]))


def find_max(seq):
    """
    Return the largest number in the list
    """
    a = 0
    for n in seq:
        if n > a:
            a = n
    return a
print("find_max: ",find_max([1,5,6,7,134]))

def count_vowels(quote):
    """
    count the total vowels in a string
    """
    vowels = ["a", "e", "i", "o", "u"]
    count=0
    for word in quote:
        for character in word:
            if character in vowels:
                count+=1
    return count


print("count_vowels: ",count_vowels("abc def ghi lmn opq rst uvz"))


