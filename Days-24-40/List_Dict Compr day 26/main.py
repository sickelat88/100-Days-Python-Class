student_dict = {
    "student": ["Andrew", "Vanessa"],
    "score": [56, 76]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame

# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data farme

for (index, row) in student_data_frame.iterrows():
    print(row)