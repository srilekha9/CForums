from django import forms
from blog.models import Group_details, Quiz
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from . import views

OPTION_CHOICES= [
        ('A', 'OptionA'),
        ('B', 'OptionB'),
        ('C', 'OptionC'),
        ('D', 'OptionD'),]

class SignUpForm(UserCreationForm, forms.Form):
    Profile_pic = forms.FileField(label='UploadProfilePhoto')
    
    
class Profilepic(forms.Form):
    ProfilepicUpload = forms.FileField(label = "Upload profile photo")
    
class Create_quiz(forms.Form):
    Title = forms.CharField(max_length = 100)
    Question1 = forms.CharField(widget=forms.Textarea)
    OptionA1 = 	forms.CharField(max_length = 100)
    OptionB1 = forms.CharField(max_length = 100)
    OptionC1 = forms.CharField(max_length = 100)
    OptionD1 = forms.CharField(max_length = 100)
    Answer1= forms.CharField(widget=forms.Select(choices=OPTION_CHOICES))
    Question2 = forms.CharField(widget=forms.Textarea)
    OptionA2 = 	forms.CharField(max_length = 100)
    OptionB2 = forms.CharField(max_length = 100)
    OptionC2 = forms.CharField(max_length = 100)
    OptionD2 = forms.CharField(max_length = 100)
    Answer2= forms.CharField(widget=forms.Select(choices=OPTION_CHOICES))
    Question3 = forms.CharField(widget=forms.Textarea)
    OptionA3 = 	forms.CharField(max_length = 100)
    OptionB3 = forms.CharField(max_length = 100)
    OptionC3 = forms.CharField(max_length = 100)
    OptionD3 = forms.CharField(max_length = 100)
    Answer3= forms.CharField(widget=forms.Select(choices=OPTION_CHOICES))
    Question4 = forms.CharField(widget=forms.Textarea)
    OptionA4 = 	forms.CharField(max_length = 100)
    OptionB4 = forms.CharField(max_length = 100)
    OptionC4 = forms.CharField(max_length = 100)
    OptionD4 = forms.CharField(max_length = 100)
    Answer4= forms.CharField(widget=forms.Select(choices=OPTION_CHOICES))
    Question5 = forms.CharField(widget=forms.Textarea)
    OptionA5 = 	forms.CharField(max_length = 100)
    OptionB5 = forms.CharField(max_length = 100)
    OptionC5 = forms.CharField(max_length = 100)
    OptionD5 = forms.CharField(max_length = 100)
    Answer5 = forms.CharField(widget=forms.Select(choices=OPTION_CHOICES))


class CreateGroupForm(forms.Form):
	Title = forms.CharField(max_length=100)
	Caption = forms.CharField(max_length=100)
	CoverPhoto = forms.FileField(label='UploadCoverPhoto', help_text='max. 2 megabytes')

class AddContestForm(forms.Form):
	ProgramTitle = forms.CharField(required=True)
	ProgramDescription = forms.CharField(required=True,widget=forms.Textarea)
	docfile = forms.FileField(label='UploadTestCaseFile', help_text='max. 42 megabytes')
	
class AttendContest(forms.Form):
    docfile = forms.FileField(label='UploadProgram')

"""class AttendQuiz(forms.Form):
    def __init__(self,*args,**kwargs):
        self.Quiz_id = kwargs.pop('id')
        super(AttendQuiz, self).__init__(*args,**kwargs)
    Title = Quiz.objects.get(Titleid = Quiz_id)
    Title.Question1
    OPTION_CHOICE1= [
        (Title.A1, 'OptionA'),
        (Title.B1, 'OptionB'),
        (Title.C1, 'OptionC'),
        (Title.D1, 'OptionD'),]     
    OPTION1 = forms.ChoiceField(choices = OPTION_CHOICE1, widget = forms.RadioSelect())
    Title.Question2
    OPTION_CHOICE2= [
        (Title.A2, 'OptionA'),
        (Title.B2, 'OptionB'),
        (Title.C2, 'OptionC'),
        (Title.D2, 'OptionD'),]     
    OPTION2 = forms.ChoiceField(choices = OPTION_CHOICE2, widget = forms.RadioSelect())
    Title.Question3
    OPTION_CHOICE3 = [
        (Title.A3, 'OptionA'),
        (Title.B3, 'OptionB'),
        (Title.C3, 'OptionC'),
        (Title.D3, 'OptionD'),]     
    OPTION3 = forms.ChoiceField(choices = OPTION_CHOICE3, widget = forms.RadioSelect())
    Title.Question4
    OPTION_CHOICE4 = [
        (Title.A4, 'OptionA'),
        (Title.B4, 'OptionB'),
        (Title.C4, 'OptionC'),
        (Title.D4, 'OptionD'),]     
    OPTION4 = forms.ChoiceField(choices = OPTION_CHOICE4, widget = forms.RadioSelect())
    Title.Question5
    OPTION_CHOICE5 = [
        (Title.A5, 'OptionA'),
        (Title.B5, 'OptionB'),
        (Title.C5, 'OptionC'),
        (Title.D5, 'OptionD'),]     
    OPTION5 = forms.ChoiceField(choices = OPTION_CHOICE5, widget = forms.RadioSelect())"""
    
class UploadPostForm(forms.Form):
    PostDescription = forms.CharField(widget = forms.Textarea)
    PostUpload = forms.FileField(label='UploadPost', help_text='max. 2 megabytes')

class QuizTitle(forms.Form):
    Title = forms.CharField(max_length=100)
    NOQ = forms.IntegerField()
    
