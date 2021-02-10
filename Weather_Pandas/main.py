import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()


print(data[data.temp == data.temp.max()])

