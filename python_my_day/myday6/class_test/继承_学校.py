class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self, stu_obj):
        print("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        print("雇佣新员工%s" % staff_obj.name)
        self.teachers.append(staff_obj)

class SchoolNambal(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolNambal):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print("""
        ---- info of teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        """% (self.name,self.name, self.age, self.sex, self.salary, self.course))
    def teach(self):
        print("%s is teaching course [%s]"%(self.name, self.course))

class Student(SchoolNambal):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self):
        print("""
        ---- info of student:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        """% (self.name,self.name, self.age, self.sex, self.stu_id, self.grade))
    def pay_tuition(self,amount):
        print("%s has paid tuition for $%s" % (self.name, amount))

school = School("老男孩", "北京———")
t1 = Teacher("Awse", 20, "M", 20000, "English")
t2 = Teacher("Alex", 30, "M", 300000, "Python")
s1 = Student("ChengRonghua", 33, "M", 1, "python")
s2 = Student("Jc", 18, "M", 2, "python")
t1.tell()
s1.tell()
school.enroll(s1)
school.enroll(s2)
school.hire(t2)
for stu in school.students:
    stu.pay_tuition(500)
