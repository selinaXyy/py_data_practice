import pandas as pd

nato_alphabet_data_frame = pd.read_csv("./nato_phonetic_alphabet.csv")
#convert to dict
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet_data_frame.iterrows()}
#ask input
user_input = input("Enter a word: ").strip().upper()
#find corresponding value
output_list = [nato_alphabet_dict[letter] for letter in user_input]

print(output_list)
