from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User_login(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.EmailField(unique = True)
    Password = models.CharField(max_length=10)


    class Meta:
        db_table ='User_login'
        verbose_name_plural = "UserLogin"

    def __str__(self) -> str:
        return self.Name

class User_data(models.Model):
    User_login = models.ForeignKey(User_login,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=25, default='', blank=True,null=True)
    Last_name = models.CharField(max_length=25, default='', blank=True,null=True)
    # profile_image = models.FileField(upload_to='images/',default='images/user.png')
    House_No = models.CharField(max_length=12, default='', blank=True, null=True)
    Mobile_No = models.CharField(max_length=12, default='', blank=True, null=True)
    Alternate_No = models.CharField(max_length=12, default='', blank=True, null=True)
    Email_Address = models.CharField(max_length=40, default='', blank=True, null=True)
    # Gender = models.CharField(max_length=10, default='', blank=True, null=True)
    Occupation = models.CharField(max_length=20, default='', blank=True, null=True)
    total_Members = models.CharField(max_length=10, default='', blank=True, null=True)
    total_Vehicles = models.CharField(max_length=10, default='', blank=True, null=True) 
    # message = models.TextField(max_length=300, default='', blank=True, null=True)


    class Meta:
        db_table ='UserData'
        verbose_name_plural = "User_Data"

    # def __str__(self) -> str:
    #     return self.Email
    
    def __str__(self) -> str:
        return self.User_login.Email

class Notification(models.Model):
    # User_login = models.ForeignKey(User_login,on_delete=models.CASCADE
    date = models.CharField(max_length=10, default='', blank=True, null=True)
    title = models.CharField(max_length=50, default='', blank=True, null=True)
    Message = models.CharField(max_length=300, default='', blank=True, null=True)

    class Meta:
        db_table = 'Notification'

    def __str__(self) -> str:
        return self.date

class occupation(models.Model):
    name = models.CharField(max_length=25, default='', blank=True,null=True)
    email = models.CharField(max_length=40, default='', blank=True, null=True)
    number = models.CharField(max_length=12, default='', blank=True, null=True)
    work = models.CharField(max_length=25, default='', blank=True,null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'occupation'

class image_add(models.Model):
    image = models.ImageField(upload_to = "image")

    class Meta:
        db_table = 'image_add'

    # def __str__(self) -> str:
    #     return self.image
    

    

