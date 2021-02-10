import pandas

raw_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = []
count = []
id = []

gray_count = len(raw_data[raw_data["Primary Fur Color"] == "Gray"])
black_count = len(raw_data[raw_data["Primary Fur Color"] == "Black"])
red_count = len(raw_data[raw_data["Primary Fur Color"] == "Cinnamon"])

print(gray_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
