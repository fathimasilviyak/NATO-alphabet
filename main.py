import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data_frame)
# create a dictionary of letter with corresponding word
phonetic_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
# print(phonetic_dict)
# create a list of the phonetic code words from a word that the user inputs
user_input = input("Enter a word: ")
new_list = [phonetic_dict[letter.upper()] for letter in user_input]

print(new_list)
