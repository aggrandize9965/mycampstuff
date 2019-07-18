#!/usr/bin/env python3

"""
File: students.py
Name:

Description:
Sources:

===============================================
Template on how to open and read a file
===============================================
file = open(filename)	# Opens the file and stores the file object in <file>
file_contents = []		# Creates a list to store the lines in the file

for line in file.readlines():	# Goes over each line in the file
    file.contents.append(line)	# Appends each line in the file to <file_contents>
    
file.close()	# Closes the file, since we are now done with the file
				# We still have access to all the lines in the file, since we stored them in <file_contents>
===============================================

===============================================
Template on how to open and write to a file
===============================================
file = open(filename, w+)	# Opens the file and stores the file object in <file>, creates new file if it does not exist

file.write(content+'\n')       # Writes to the file and goes to next line when done
    
file.close()	# Closes the file, since we are now done with the file
				
===============================================
"""


def main():
    filename = "data.txt"
    students = {}

    populate_dicts(students, filename)
    add_letter_grades(students)
    display_students(students)


# This will add the student data from the file into the dictinoary that was initiailzed in the main() function
def populate_dicts(students, filename):
    datafile = open(filename)

    for line in datafile.readlines():
        cleaned = line.rstrip().split(',')
        id_number, grade = "".join(cleaned[1].split()), eval("".join(cleaned[2].split()))
        
        students[cleaned[0]] = [id_number, grade]

    datafile.close()


# This will add the letter grades to the end of the dictionary keys
def add_letter_grades(students):
    # Code here
    for student in students:
        grade = students[student][1]
        if grade >= 80:
            letter = 'A'
        elif grade >= 65:
            letter = 'B'
        elif grade >=50:
            grade = 'C'
        else: 
            letter = 'D'
        students[student].append(letter)

# This will write the student data to a new file (names, IDs, letter grades)
# Hint: start by figuring out how to print all the data needed
def display_students(students):
    # Code here
    for student in students:
        print(student.ljust(10)+str(students[student][0])+"    "+students[student][2])
                                    

if __name__ == "__main__":
    main()
