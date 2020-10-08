from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Employee(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    other_name = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    state_of_origin = models.CharField(max_length=25)
    lga_of_origin = models.CharField(max_length=25)
    employment_date = models.DateField()
    retirement_date = models.DateField()
    photograph = models.ImageField(upload_to='images')
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def  get_full_name(self):
        return self.last_name+" "+self.first_name+" "+ self.other_name

class Leave(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class EmployeeDepartment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_department')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_added = models.DateField()
    date_left = models.DateField(null=True)

class EmployeeLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_leave')
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class EmployeePosition(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_position')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)