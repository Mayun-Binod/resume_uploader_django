from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
# Create your models here.
STATE_CHOICE=NEPAL_STATES = [
    ('1', 'Province No. 1'),
    ('2', 'Madhesh Province'),
    ('3', 'Bagmati Province'),
    ('4', 'Gandaki Province'),
    ('5', 'Lumbini Province'),
    ('6', 'Karnali Province'),
    ('7', 'Sudurpashchim Province'),
]
class Resume(models.Model):
    pk_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    name=models.CharField(max_length=150)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    phone=PhoneNumberField(region="NP")
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to="profileimage",blank=True)
    my_file=models.FileField(upload_to='document',blank=True)
