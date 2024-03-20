## List Comprehension ##
#create new list based on an existing list

numbers = [1,2,3,4,5]
new_numbers = [n+1 for n in numbers]
print(new_numbers)
#[2, 3, 4, 5, 6]

#------------------------------------#

name = "Selina"
name_list = [letter for letter in name]
print(name_list)
#['S', 'e', 'l', 'i', 'n', 'a']

#------------------------------------#

range_list = [n*2 for n in range(1,5)]
print(range_list)

#------------------------------------#
## Conditional List Comprehension ##

names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) > 4]
print(short_names)
print(long_names)

#create a list that contains the repeated items inside 2 other lists
with open("file1.txt") as file1:
  list1 = file1.readlines() #automatically forms a list by appending each line
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [num for num in list1 if num in list2]

#------------------------------------#
## Dictionary Comprehension ##
from random import randint

names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
student_scores = {name:randint(0,100) for name in names} #key:value for item in list
print(student_scores)
passed_students = {student:score for (student,score) in student_scores.items() if score >= 60} #key:value for (key,value) in dict.items()
print(passed_students)

#------------------------------------#
## Iterate Over Pandas DataFrame ##
student_dict = {
  "student": ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"],
  "score": [12, 23, 34, 45, 56],
}

for (key, value) in student_dict.items():
  print(value) #print(key)

#pd dataframe is similar to py dict
import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
# allows iterations over rows
for (index_of_row, data_of_row) in student_data_frame.iterrows():
  print(data_of_row) #pd series
  print(data_of_row.student) #specify which column

  if data_of_row.student == "Caroline":
    print(data_of_row.score)
