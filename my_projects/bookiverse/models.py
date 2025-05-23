from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

# class Department(models.Model):
#     department_id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=50)

# class Job(models.Model):
#     job_id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=50)
#     salary_range = models.JSONField()



# class Employee(models.Model):
#     employee_id  = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=50,null=False,default="kashif")
#     address  = models.TextField(max_length=200,null=False,blank=True,default="peshawar")
#     phone = models.CharField(max_length=20,null=False,unique=True,default="027830974692")
#     email = models.EmailField(max_length=50,null=False,unique=True,default="kashif@email.com")
#     job_id =models.ForeignKey(Job,on_delete=models.CASCADE,related_name="jobs") 
#     department_id = models.ForeignKey(Department,on_delete=models.SET_NULL,
#         null=True,
#         blank=True,related_name="dept") 

#     def __int__(self):
#         return self.employee_id
# class Payroll(models.Model):
#     payroll_id = models.BigAutoField(primary_key=True)
#     salary=models.PositiveBigIntegerField(null=False,blank=True)
#     bonus=models.PositiveBigIntegerField(null=False,blank=True)
#     deduction = models.PositiveBigIntegerField(null=False,blank=True)
#     paydate = models.DateField(blank=True,null=False)
#     employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)

# class Performance(models.Model):
#     performance_id  = models.BigAutoField(primary_key=True)
#     reviewdate = models.DateField(null=False,blank=True)
#     score = models.PositiveBigIntegerField(null=False,blank=True)
#     feedback = models.TextField(max_length=200,null=False,blank=True)
#     employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)

# class Benefit(models.Model):
#     benefit_id = models.BigAutoField(primary_key=True)
#     benefit_type = models.CharField(max_length=50,blank=True,null=False)
#     description = models.TextField(max_length=200,blank=True,null=False)
#     start_date = models.DateField(null=False,blank=True)
#     end_date = models.DateField(null=False,blank=True)
#     employee_id = models.ForeignKey(Employee,models.CASCADE,related_name="benefits")


# class Document(models.Model):
#     document_id  = models.BigAutoField(primary_key=True)
#     document_type = models.CharField(max_length=50,null=False,blank=True)
#     file_path = models.CharField(max_length=200,null=False,blank=True)
#     employee_id = models.ForeignKey(Employee,models.CASCADE)


# class Attendence(models.Model):
#     attendence_id = models.BigAutoField(primary_key=True)
#     date = models.DateField(blank=True,null=False)
#     check_in_time = models.DateTimeField(blank=True,null=False)
#     check_out_time = models.DateTimeField(blank=True,null=False)
#     employee_id = models.ForeignKey(Employee,models.CASCADE)

# statuses = {
#     "p":"pass",
#     "f":"fail"
# }
# class Training(models.Model):
#     training_id = models.BigAutoField(primary_key=True)
#     training_name = models.CharField(max_length=50,null=False,blank=True)
#     date  = models.DateField(blank=True,null=False)
#     status =  models.CharField(max_length=50,null=False,blank=True,choices=statuses)
#     description = models.TextField(max_length=200, null=False,blank=True)
#     employee_id = models.ManyToManyField(Employee,related_name="trainings")
    # def __str__(self):
    #     return self.name

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(null=False,max_length=50)
    email  = models.EmailField(null=False,unique=True)
    hash_password = models.CharField(null=False,max_length=55)
    role = models.CharField(null=False,max_length=50)
    flight = models.ManyToManyField('Flight',related_name='flights')

class Flight(models.Model):
    flight_id = models.BigAutoField(primary_key=True)
    flight_name =  models.CharField(null=False,max_length=50)  
    plane_name = models.CharField(null=False,max_length=50)  
    flight_origin = models.CharField(null=False,max_length=50)  
    flight_departure = models.CharField(null=False,max_length=50)  
    flight_date =  models.DateTimeField(null=False)
    flight_price = models.IntegerField(null=False)
    company = models.CharField(null=False,max_length=50)  

def spacechecker(value:str):
    if value.startswith(" ") and value.endswith(" "):
        raise ValidationError("the hotel name cannot start and end with space/white characters")

room_choices = [
    ('1',"1 rooms"),
    ('2',"2 rooms"),
    ('3',"3 rooms"),
    ('4',"4 rooms"),
    ('suite',"suite"),
]
class Hotel(models.Model):
    hotel_id = models.BigAutoField(primary_key=True)
    hotel_name = models.CharField(max_length=30,error_messages={
        'max_length': "Username too long (max 30 chars)",
        'required': "You must choose a username",
    },validators=[spacechecker],null=False)
    hotel_rooms = models.CharField(null=False,choices=room_choices,max_length=30)
    hotel_price = models.IntegerField(null=False)



    