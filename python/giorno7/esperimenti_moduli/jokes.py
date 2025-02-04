import pyjokes
import csv
"""
joke = pyjokes.get_joke("it", "neutral")
print(joke)
print(pyjokes.get_jokes('it', 'neutral'))

for joke in pyjokes.get_jokes('it'):
    print(joke)
"""


jokes = pyjokes.get_jokes('it', 'neutral')


with open("jokes.csv", 'w') as fd:
    writer = csv.writer(fd)
    writer.writerow(["Joke on python programmer 🤓"])
    for joke in jokes:
        writer.writerow([joke])

