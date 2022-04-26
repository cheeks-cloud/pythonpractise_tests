import unittest
from student import Student


class TestStudent(unittest.TestCase):

  def setUp(self):
    self.newStudent = Student(1234,"Agnes","Kaswii",True,78)

  def tearDown(self):
    Student.studentList = []

  def test__init(self):
    self.assertEqual(self.newStudent.id, 1234)
    self.assertEqual(self.newStudent.fName, "Agnes")
    self.assertEqual(self.newStudent.lName, "Kaswii")
    self.assertTrue(self.newStudent.graduated)
    self.assertEqual(self.newStudent.grade, 78)

  def testsaveStudent(self):
    self.newStudent.saveStudent()

    self.assertEqual(len(Student.studentList),1)


  def testsaveMultipleStudent(self):
     self.newStudent.saveStudent()
     studentTwo = Student(2346,"sarah","wamboi",False,45)
     studentTwo.saveStudent()

     self.assertEqual(len(Student.studentList),2)

  def testdeleteStudent(self):
     self.newStudent.saveStudent()
     studentTwo = Student(2346,"sarah","wamboi",False,45)
     studentTwo.saveStudent()

     self.newStudent.deleteStudent()
     self.assertEqual(len(Student.studentList),1)


  def testfindStudentByStudentId(self):
    self.newStudent.saveStudent()
    studentTwo = Student(2346,"sarah","wamboi",False,45)
    studentTwo.saveStudent()

    foundStudent = Student.findStudentByStudentId(2346)

    self.assertEqual(foundStudent.fName,"sarah")

    

    













if __name__ == "__main__":
  unittest.main()