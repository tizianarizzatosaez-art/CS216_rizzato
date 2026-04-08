# chapelReport.py
# Tiziana Rizzato
# Prof. Lehman
# Count chapel attendance


# store students names

students = {}

# open student.scv for reading 

file = open("students.csv", "r")

# read first line 

line = file.readline()

# read all students 

while line != "":
    data = line.split(",")

    student_id = data [0].strip()
    student_name = data [1].strip()

    students[student_id] = student_name

    line = file.readline()

file.close()

# store chapel attendance

file = open("attendance.csv", "r")

attendance_count = {}

# read first line

line = file.readline()

# count attendance

while line != "":
    data = line.split(",")

    chapel_id = data[0].strip()
    student_id = data[1].strip()

    # count attendance for each student

    if student_id in attendance_count:
         attendance_count[student_id] = attendance_count[student_id] + 1
    else:
        attendance_count[student_id] = 1

    line = file.readline()


# write report.csv

report_file = open("report.csv", "w")

# go through all students 

for student_id in students:
    
    name = students[student_id]

    # get attendance or 0 if none 

    if student_id in attendance_count:
        total = attendance_count[student_id]
    else:
        total = 0

    # write line to report

    report_file.write(f"{student_id}, {name}, {total}\n")

# close report file

print( "Done writing report.csv")

report_file.close()


    
