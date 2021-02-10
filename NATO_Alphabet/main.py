import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

df = pandas.read_csv("nato_phonetic_alphabet.csv")

dictio = {value.letter: value.code for (index, value) in df.iterrows()}

word = input("What 's your word? ").upper()

t_list = [dictio[letter] for letter in word]

print(t_list)


