# with open("weather_data.csv") as weather_data:
#     weather_list = weather_data.readlines()
#
# print(weather_list)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# # avg_list = sum(temp_list) / len(temp_list)
# # print(avg_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in columns
# print(data.condition)

# get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)
# print(int((monday.temp * 9/5) + 32))
#

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

