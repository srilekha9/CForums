from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User_Group(models.Model):
    user_name = models.ForeignKey('UserProfile')
    groups = models.CharField(max_length = 500)
    
class Group_Post(models.Model):
    group_name = models.CharField(max_length = 100)
    group_post = models.CharField(max_length = 500)
    Description = models.TextField(max_length =10000, null = True)
    def __str__(self):
        return self.group_name

class UserProfile(models.Model):
    user_name = models.CharField(max_length = 100, primary_key = True)
    profile_pic = models.CharField(max_length = 500, default = 'creative.jpg')
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key = True)
    Name = models.CharField(max_length=100)
    """Password = models.CharField(widget=form.PasswordInput)"""
    Group = models.CharField(max_length = 20)
   
receiver(post_save, sender=User)
def create_self_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user =instance)
receiver(post_save, sender=User)
def save_User_profile(sender,instance,**kwargs):
    instance.profile.save() 
class QuizDetail(models.Model):
    #Userid = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    Title = models.CharField(max_length=50, primary_key = True)
    Timelimithr = models.CharField(max_length=10)
    Timelimitmin = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Title

class Quiz(models.Model):
    Titleid = models.CharField(max_length=100)
    Question1 = models.TextField()
    A1 = models.CharField(max_length=1000)
    B1 = models.CharField(max_length=1000)
    C1 = models.CharField(max_length=1000)
    D1 = models.CharField(max_length=1000)
    Answer1 = models.CharField(max_length=100)
    Question2 = models.TextField()
    A2 = models.CharField(max_length=1000)
    B2 = models.CharField(max_length=1000)
    C2 = models.CharField(max_length=1000)
    D2 = models.CharField(max_length=1000)
    Answer2 = models.CharField(max_length=100)
    Question3 = models.TextField()
    A3 = models.CharField(max_length=1000)
    B3 = models.CharField(max_length=1000)
    C3 = models.CharField(max_length=1000)
    D3 = models.CharField(max_length=1000)
    Answer3 = models.CharField(max_length=100)
    Question4 = models.TextField()
    A4 = models.CharField(max_length=1000)
    B4 = models.CharField(max_length=1000)
    C4 = models.CharField(max_length=1000)
    D4 = models.CharField(max_length=1000)
    Answer4 = models.CharField(max_length=100)
    Question5 = models.TextField()
    A5 = models.CharField(max_length=1000)
    B5 = models.CharField(max_length=1000)
    C5 = models.CharField(max_length=1000)
    D5 = models.CharField(max_length=1000)
    Answer5 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Titleid
        
"""class ProgramDetail(models.Model):
    Userid = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    Title = models.CharField(max_length=200, primary_key = True)
    
    def __str__(self):
        return self.Userid"""
    
class Program(models.Model):
#    Titleid = models.ForeignKey('ProgramDetail', on_delete = models.CASCADE)
    PTitle = models.CharField(max_length=100)
    PDescription = models.TextField(max_length = 100)
    testcase = models.TextField(max_length = 100)
    
    def __str__(self):
        return self.PTitle
    
class Postings(models.Model):
     UPosts_Description = models.TextField(max_length = 10000)
     UPosts_Photo = models.CharField(max_length=100)
     created_date = models.DateTimeField(default = timezone.now)
     
     
     def __str__(self):
        return self.UPosts_Description
        
class Group_details(models.Model):
    Gname = models.CharField(max_length=30, primary_key = True)
    Caption = models.CharField(max_length=100)
    CoverPhoto=  models.CharField(max_length=100)

    def __self__(self):
        return self.Gname
        
"""class UserProfile(models.Model):
    Userid = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    image = models.ImageField(upload_to=)"""
