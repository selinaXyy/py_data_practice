import pandas as pd

#declare empty lists
fur_color = []
num_each_color = []

#read data
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#find fur color series
color_data = squirrel_data["Primary Fur Color"] #pd Series (list)

#append colors to color list
for color in color_data:
    #notna == not NaN
    if (pd.notna(color)) and (not color in fur_color): #if color is not NaN && does not exist in fur_color
        fur_color.append(color)

#append counts to counts list
for color in fur_color:
    #only sums the values that are True
    fur_color_sum = sum(color_data == color) #pd Series is allowed to compare to a single value, and returns Bool
    num_each_color.append(fur_color_sum)

#create dict
squirrel_count_dict = {
    "Fur Color": fur_color, 
    "Count": num_each_color,
}

squirrel_count_table = pd.DataFrame(squirrel_count_dict)
squirrel_count_table.to_csv("./squirrel_count.csv")