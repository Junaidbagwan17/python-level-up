import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


def generate_phonatic():
    word = input("Enter a word:").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, please insert letters only in the alphabet.")
        generate_phonatic()
    else:
        print(output_list)

generate_phonatic()