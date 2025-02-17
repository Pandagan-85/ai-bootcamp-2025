from collections import defaultdict, Counter
def count(seq):
    """
    counter = {}
    for el in seq:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    return counter
    """
    """
    # refactor con default dict
    counter = defaultdict(int)

    for el in seq:
        counter[el] += 1
    return counter
    """

    # refactor con counter
    def count_characters(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string")

        return dict(Counter(s))
