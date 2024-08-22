
import pandas

data = pandas.read_csv('../NATO-alphabet-start/nato_phonetic_alphabet.csv')
# print(data.to_dict())

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

def generate_phonetics():
    word = input("Please enter the word:").upper()
    result = [phonetic_dict[letter] for letter in word]
    print(result)

generate_phonetics()
