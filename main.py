import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data_frame)
# create a dictionary of letter with corresponding word
phonetic_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}


# print(phonetic_dict)
# create a list of the phonetic code words from a word that the user inputs

def generate_phonetics():
    user_input = input("Enter a word: ").upper()
    try:
        new_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(new_list)


generate_phonetics()
