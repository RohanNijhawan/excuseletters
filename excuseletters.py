"""

Four steps to do well:
	1) acknowledge nervousness
	2) allow nervousness, to an extent
	3) use that to...
	4) comfortably kick ass

"""
import pickle
try:
	classDict = pickle.load( open('classdict.p', 'rb'))
except FileNotFoundError:
	classDict = {}
	pickle.dump(classDict, open('classdict.p', 'wb'))

class ClassDetail():
	"""docstring for ClassDetail"""
	def __init__(self, department, classNumber, day, time, instructorName):
		super(ClassDetail, self).__init__()
		self.department = department
		self.classNumber = classNumber
		self.day = day
		self.time = time
		self.instructorName = instructorName.title()

	def listOfDays(self):
		listOfDays = []
		if 'M' in self.day:
			listOfDays.append('Monday')
		if 'Tu' in self.day:
			listOfDays.append('Tuesday')
		if 'W' in self.day:
			listOfDays.append('Wednesday')
		if 'Th' in self.day:
			listOfDays.append('Thursday')
		if 'F' in self.day:
			listOfDays.append('Friday')
		return listOfDays

	def mondayFridayOnly(self):
		listOfDays = []
		if 'M' in self.day:
			listOfDays.append('Monday')
		if 'F' in self.day:
			listOfDays.append('Friday')
		return listOfDays

	def fullDepartmentName(self):
		if self.department not in classDict:
			newDepartment = input("The department abbreviation, " + self.department + ", cannot be found. Please enter the name manually:\n")
			classDict[self.department] = newDepartment
		return classDict[self.department]

	def formattedClassString(self, studentName, SID, day):
		formatted = "" + studentName + '\t' + SID + '\t' + self.fullDepartmentName() + " " + self.classNumber + '\t' + self.instructorName + '\t' + day + '\t' + self.time + '\n'
		return formatted


classes = open('classes.txt', 'r')
destination = open('classesoutput.txt', 'w')
for line in classes:
	lineList = line.split('\t')
	if len(lineList) < 2:
		continue
	if len(lineList) == 2:
		studentName = lineList[0]
		studentID = lineList[1].split()[0]
		print("Generating info for: " + studentName + ", " + studentID)
	else:
		try:
			aClass = ClassDetail(lineList[1], lineList[2], lineList[9], lineList[10], lineList[6])
		except IndexError:
			print("The line " + lineList + " was not written because there was an IndexError.")
			continue
		for day in aClass.mondayFridayOnly():
			destination.write(aClass.formattedClassString(studentName, studentID, day))

pickle.dump(classDict, open('classdict.p', 'wb'))
	