
from ast import If


class Student:

  studentList = []

  def __init__(self,id,fName,lName,graduated,grade):
    self.id = id
    self.fName = fName
    self.lName = lName
    self.graduated = graduated
    self.grade = grade


  def saveStudent(self):
     Student.studentList.append(self)

  def deleteStudent(self):
    Student.studentList.remove(self)


  @classmethod
  def findStudentByStudentId(cls, id):
    for student in cls.studentList:
      if student.id == id:
         return student





