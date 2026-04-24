import pandas

student_data= {
    "student": ["Alice", "Bob" ,"James"],
    "score": [80, 55, 71]
}

# Loop over dict and print its key and values
for i in student_data:
    # print(i) #  this will print key only or we can say column name
    # print(student_data[i]) # this will print keys and values on bottom of it eg. all col and then all values list
    #print(student_data[i][1]) # this will give you BOB score and his name
    pass

for k,v in student_data.items():
    #print(k,v)
    #print(v)
    pass

# now lets use DF
student_data_frame = pandas.DataFrame(student_data)
# print(student_data_frame)

for i in student_data_frame:
    # print(student_data_frame[i]) # this will give first names and then score as separate series
    pass
print("-----------------------------")

for c,r in student_data_frame.items():
    #print(c) #this will give you both column names
    #print(r) # this will give you items in columns both separately as series
    # print(c,r) # this are not useful they are just printing
    pass

print("-----------------------------")

# so we have method from pandas called iterrows
# LOOP though the rows of DF
for (index , row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == "Bob":
        print(row)

    if row.score > 75:
        print(row.student)