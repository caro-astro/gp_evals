#using copy/pasted data from jupiter to print out grade breakdown by category

import pandas as pd
import numpy as np

#function to convert percents to letter grades
def PtoLgrade(pgrade):
	if pgrade >= 93.0:
		return "A"
	if pgrade < 93.0 and pgrade >= 90.0:
		return "A-"
	if pgrade < 90.0 and pgrade >= 87.0:
		return "B+"
	if pgrade < 87.0 and pgrade >= 83.0:
		return "B"
	if pgrade < 83.0 and pgrade >= 80.0:
		return "B-"
	if pgrade < 80.0 and pgrade >= 77.0:
		return "C+"
	if pgrade < 77.0 and pgrade >= 73.0:
		return "C"
	if pgrade < 73.0 and pgrade >= 70.0:
		return "C-"
	if pgrade < 70.0 and pgrade >= 67.0:
		return "D+"
	if pgrade < 67.0 and pgrade >= 63.0:
		return "D"
	if pgrade < 63.0 and pgrade >= 60.0:
		return "D-"
	if pgrade < 60:
		return "F"
###########################################
#main code
#there is a method to download a pdf and convert that to excel and then convert to csv, but the columns are not working out right now.
#so I just went to the gradebook report in jupiter and c/pd the table into excel and truncated and labeled

cfile1='~/Analysis/teaching/example_cats.csv'
gtable=pd.read_csv(cfile1)

cfile2='~/Analysis/teaching/example_ES.csv'
ftable=pd.read_csv(cfile2)

#split into columns
ihw=gtable['homework']
igp=gtable['participation']
icw=gtable['classwork']
its=gtable['tests']
iqz=gtable['quizzes']
iname=gtable['Name']
itg=gtable['Grade']
nstu=len(iname)

#get exam and semester grades, this requres some string splitting.
exam=ftable['E1']
sem1=ftable['S1']
eg=list()
sg=list()

x=0
for x in range(0,nstu):
	f1=str(exam[x])
	f2=f1[0:3]
	eg=pd.to_numeric(f2)
	f3=str(sem1[x])
	f4=f3[0:3]
	sg=pd.to_numeric(f4)
	#output grade breakdown
	print(iname[x])
	print(" ")
	print('Quarter 4 Wonder/Inquiry/Participation: %s' %PtoLgrade(igp[x]))
	print('Quarter 4 Tests: %s' %PtoLgrade(its[x]))
	print('Quarter 4 Quizzes: %s' %PtoLgrade(iqz[x]))
	print('Quarter 4 Homework: %s' %PtoLgrade(ihw[x]))
	print('Quarter 4 Classwork: %s' %PtoLgrade(icw[x]))
	print('Quarter 4 Overall Grade: %s' %itg[x])
	print('Semester Exam Grade: %s' %PtoLgrade(eg))
	print('Semester 2 Overall Grade: %s' %PtoLgrade(sg))
	print('----------------------')


