import pandas as pd

#data is the returned 'pandas DataFrame' object
data = pd.read_csv("weather_data.csv")
print(data)
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

#-----------------------------------------------#
#pandas takes the first row of the csv file to be the names of each column (by default)

print(data["temp"]) #specifies column name
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24

#-----------------------------------------------#

data_dict = data.to_dict()
print(data_dict) #converts DataFrame into dictionary
# {
#     'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 
#     'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 
#     'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
# }

#-----------------------------------------------#

temp_list = data["temp"].to_list() #converts Series into list
print(temp_list)
# [12, 14, 15, 14, 21, 22, 24]

# avg_temp = sum(temp_list) / len(temp_list)
avg_temp = data["temp"].mean() #Series.mean()
max_temp = data["temp"].max()
print(avg_temp)
print(max_temp)

#-----------------------------------------------#
#pandas automatically converts each of the headings into an attribute

print(data.condition)
#data["condition"] == data.condition

#-----------------------------------------------#
#Get data in ROW:

monday_row = data[data.day == "Monday"] #DataFrame[row, column]
max_temp_row = data[data.temp == data.temp.max()] #returns the index of the row that meets this condition

#-----------------------------------------------#
#Create Dataframe from SCRATCH
students_dict = {
    "name": ["Amy", "James", "Jack"], #Heading: Series
    "score": [98, 97, 96], #Heading: Series
}
students_data = pd.DataFrame(students_dict) #converts the dictionary into a pd Dataframe
students_data.to_csv("./students_data.csv")