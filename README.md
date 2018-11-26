# gp_evals
python 3.x script to reformat grade breakdown from jupyter for evaluations

Copy/Paste your Jupyter grade book information into excel and save it as a .csv file. Then, from terminal, type 
Q4_evals.py > gradebreakdown.txt

This will produce a file called gradebreadown.txt with the following information:

LastName, FirstName
 
Quarter 4 Wonder/Inquiry/Participation: A-

Quarter 4 Tests: B+

Quarter 4 Quizzes: A

Quarter 4 Homework: B

Quarter 4 Classwork: A

Quarter 4 Overall Grade: 84.40%

Semester Exam Grade: A

Semester 2 Overall Grade: B

----------------------

Otherkid, Student
 
Quarter 4 Wonder/Inquiry/Participation: B-

Quarter 4 Tests: C

Quarter 4 Quizzes: B

Quarter 4 Homework: B-

Quarter 4 Classwork: A

Quarter 4 Overall Grade: 78.90%

Semester Exam Grade: D

Semester 2 Overall Grade: C-


An example of the formatting of the input files can be found in example_cats.csv and example_ES.csv.

This program should increase evaluation writing speed, and reduce errors in numeric to letter grade conversion, reduce grade typos, and misspelling of student names.

*All grades here are completely fictional, and are not based on any particular student at GP.
