from django.db import models


# Create your models here.
# HOW TO CREATE MODEL FILE AS PACKAGE

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class College(BaseModel):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)


class Courses(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    duration = models.PositiveSmallIntegerField()


class College_Course(BaseModel):
    college = models.ForeignKey(College, on_delete=models.PROTECT)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)


class Department(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)


class Student(BaseModel):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.PROTECT)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)


class Staff(BaseModel):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    college = models.ForeignKey(College, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)


class Staff_Course(BaseModel):
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)


class Subjects(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)


class Role(BaseModel):
    role_type = models.CharField(max_length=100, unique=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
