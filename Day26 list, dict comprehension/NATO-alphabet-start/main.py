import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data.to_dict())

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

def generate_phonetics():
    word = input("Please enter the word:").upper()
    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("This program takes only alphabets")
        generate_phonetics()
    else:
        print(result)


generate_phonetics()