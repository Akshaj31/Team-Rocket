from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    department_id = models.IntegerField()
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "auditdb.employees"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LoginLogoutLog(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    event_type=models.CharField(max_length=10)
    event_time=models.DateTimeField(auto_now_add=True)
    ip_address=models.CharField(max_length=55)
    user_agent=models.CharField(max_length=255)
    
    class Meta:
        db_table = "auditdb.login_logout_log"