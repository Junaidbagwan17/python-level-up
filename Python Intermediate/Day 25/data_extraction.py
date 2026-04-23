import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260423.csv")
# print(data.head())
# print(data.columns)

gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "color": ["Gray", "Red", "Black"],
    "count": [gray_sq_count, red_sq_count, black_sq_count]
}
new_df = pandas.DataFrame(data_dict)
print(new_df)
new_df.to_csv("squirrel_color_count.csv")
