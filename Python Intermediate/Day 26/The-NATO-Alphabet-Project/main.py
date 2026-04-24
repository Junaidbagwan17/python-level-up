import  pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# when you use to_dict it will not give you proper result why? gives you column-wise dictionary
# structure is: column → index → value

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(data_dict)

user_name = input("enter the name:").upper()
# result = []
# for l in user_name:
#     alphabet = l.upper()
#     words = (data_dict[alphabet])
#     result.append(words)
# print(result)
# HERE is how we did above in 1 line
result = [data_dict[l] for l in user_name]
print(result)

