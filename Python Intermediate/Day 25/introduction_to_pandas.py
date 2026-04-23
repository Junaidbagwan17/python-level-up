import pandas
#
data = pandas.read_csv(r"C:\Users\Junaid\Downloads\weather_data.csv")
print(data) # dataframe
print(data["temp"]) # Series
print("-----------------------------\n")

print("converting dataframe into Dict")
data_dict = data.to_dict()
print(data_dict)

print("-----------------------------\n")
print("converting data series as list")
data_list = data["temp"].to_list()
print(data_list)

#TODO: What is AVERAGE temperature ?
total = 0
count = 0
for i in data_list:
    total += i
    count += 1
print("Sum of values:",total)
print("Count of values:",count)

avg_temp = (total / count)
print(f"The average temperature is {avg_temp}")

# BUT WITH USING PANDAS WE CAN FIND AVERAGE MORE EASILY
print("The average temperature is",data["temp"].mean())

# TODO: WHAT is MAXIMUM temp ?
print(data["temp"].max())
#
# TODO: Get data in the columns
print(data["condition"])
print(data.condition)

# TODO: Get data in rows
print(data[data.day == "Monday"])
print(data[data["day"] == "Tuesday"])

#TODO: print which row of data has highest temp in the week
print(data[data.temp == data.temp.max()])

#TODO: Print the weather condition for day monday
monday = data[data.day == "Monday"]
print(monday.condition)

# TODO: Convert Mondays temp into Fahrenheit
# (34°C × 9 / 5) + 32 = 93.2°F

monday = data[data.day == "Monday"] #In that example, monday.temp is a Series with ONLY ONE VALUE
mondays_temp = int(monday.temp.iloc[0])# And Python wants a pure number, not a container
monday_temp_F = mondays_temp * 9/5 + 32
print(f"Celsius:{mondays_temp} = Fahrenheit : {monday_temp_F}")


# TODO: Create a DataFrame from scratch

data_dict = {
    "students" : ["Alex", "Bob", "Momo"],
    "score": [70, 80 ,65]
}

df = pandas.DataFrame(data_dict)
print(df)

#TODO: convert Df into csv file
df.to_csv("student_score.csv")