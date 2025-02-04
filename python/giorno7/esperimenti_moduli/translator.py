from translate import Translator

translator = Translator(to_lang='it')
"""
esercizio per creare traduzioni!
Figo!
"""
try:
    with open('traduzione.txt', mode='w') as file_out, open('da_tradurre.txt') as file_in:
        text = file_in.read()
        translation = translator.translate(text)
        print(translation)
        file_out.write(translation)
except FileNotFoundError as err:
    print('Controlla la posizione del tuo file da tradurre')
