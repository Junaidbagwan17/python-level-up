#TODO: Print values in csv files

# with open(r"C:\Users\Junaid\Downloads\weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# above method will take lot of cleaning so what we can do instead?
# we have inbuilt library for data handling

import csv
with open(r"C:\Users\Junaid\Downloads\weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    print(data)

    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

# Now you see there is little difficulty in printing temprature as it is so to deal with this we have PANDAS library
# now look how pandas will do print temprature column within two lines and can pritn whole DataFrame in go.

import pandas

data = pandas.read_csv(r"C:\Users\Junaid\Downloads\weather_data.csv") # r before file or replace blackslash into forward slash
# print(data)
print(data["temp"])
