from django import forms
from .models import Resume

GENDER_CHOICES=[
    ('MALE','male'),
    ('FEMALE',"female")
]
JOB_CITY_CHOICE=[ 
    ('Kathmandu', 'Kathmandu'),
    ('Pokhara', 'Pokhara'),
    ('Biratnagar', 'Biratnagar'),
    ('Lalitpur', 'Lalitpur'),
    ('Bharatpur', 'Bharatpur'),

]
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label="Preferred job location's",choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city','pin','state','phone','job_city','profile_image','my_file']

        labels={"name":"Full Name","dob":"Date Of Birth","pin":"Pin Code","Phone":"Phone Number","email":"Email ID","profile_image":"Profile Image","my_file":"Document"}

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.DateInput(attrs={"class":"form-control"}),
            "locality":forms.TextInput(attrs={"class":"form-control"}),
            "city":forms.TextInput(attrs={"class":"form-control"}),
            "pin":forms.NumberInput(attrs={"class":"form-control"}),
            "state":forms.Select(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }