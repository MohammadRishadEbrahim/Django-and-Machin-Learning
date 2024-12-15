from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
# Model of Adminstrators in Models default Django

# Create Model of Camera Model(Table)
class Camera(models.Model):
    Name = models.CharField(max_length=100 , unique=True)
    Password = models.CharField(validators=[MinLengthValidator(5)],max_length=20)
    Active = models.OneToOneField("Security",on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.Name
    
    
# Create Model of Security Model(Table)

class Security(models.Model):
    Name = models.CharField(max_length=100 , unique=True)
    Password = models.CharField(validators=[MinLengthValidator(5)],max_length=20)

    Active , UnActive = "Active" , "No Active"
    status_choice = ((Active,"Active"),
                     (UnActive,"No Active"),
                    )
    Status = models.CharField(choices=status_choice,max_length=50,blank=True,null=True)


    Camera_Name = models.OneToOneField("Camera",on_delete=models.CASCADE,blank=True,null=True)
    Phone = models.CharField(validators=[MinLengthValidator(10)],max_length=13 , unique=True)
    Email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.Status)
    
# Craete Model of Cantact
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
