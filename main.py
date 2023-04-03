import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data_frame)
# create a dictionary of letter with corresponding word
data_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
print(data_dict)
