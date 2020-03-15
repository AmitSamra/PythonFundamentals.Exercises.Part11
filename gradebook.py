from enum import Enum
import uuid

class AliveStatus(Enum):
	Deceased = 0
	Alive = 1

class Person():
	def __init__(self, first_name, last_name, dob, alive):
	self.first_name = first_name
	self.last_name = last_name
	self.dob = dob
	self.alive = alive
	
	def update_first_name(f_n)
		return self.first_name = fn

	def update_last_name(l_n)
		return self.last_name = ln

	def update_dob(d_b):
		return self.dob = db

	def update_status(a)
		return self.alive = a

class Instructor(Person):
	def __init__(self, instructor_id):
		self.instructor_id = "Instructor_"uuid.uuid4()
		super().__init__(first_name, last_name, dob, alive)

class student(Person):
	def __init__(self, student_id_id):
		self.student_id = "Student_"uuid.uuid4()
		super().__init__(first_name, last_name, dob, alive)

class ZipCodeStudent(Student):
	def __init__(self):
		super().__init__(first_name, last_name, dob, alive)

class CollegeStudent(Student):
	def __init__(self):
		super().__init__(first_name, last_name, dob, alive)

class Classroom():
	def __init__(self, students, instructors):
		self.students = students
		self.instructors = instructors
	
	def add_isntructor(a_i):
		pass

	def remove_isntructor(r_i):
		pass	

	def add_student(a_s):
		pass

	def remove_student(r_s):
		pass

	def print_instructors(p_i):
		pass

	def print_students(p_s):
		pass

	