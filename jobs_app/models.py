from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.



class platform(models.Model):
    name=models.CharField(max_length=100)
    platform_link=models.URLField(max_length=100)
    hr=models.CharField(max_length=100)

    def __str__(self):
        return f'posted on {self.name} HR is {self.hr} ' 
class job(models.Model):
    job_title=models.CharField(max_length=50,default='')
    salary=models.IntegerField()
    company=models.CharField(max_length=200,default='')
    job_platform=models.ForeignKey(platform,on_delete=models.CASCADE,related_name="job",null=True,blank=True)
    location=models.CharField(max_length=200,default='')
    description=models.TextField(default='')
    date_and_time=models.DateTimeField(auto_now_add=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    job_Type=[('ft','full-time'),
              ('pt','part-time')]
    job_type=models.CharField(max_length=2,choices=job_Type,default='ft')
    current_working=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.job_title} at {self.company}'

class company_review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    hiring_rate=models.PositiveBigIntegerField(validators=[MinValueValidator(100),MaxValueValidator(5000)],null=True)
    about_company=models.CharField(max_length=200,null=True)
    job=models.ForeignKey(job,on_delete=models.CASCADE,related_name='reviews',null=True,blank=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.hiring_rate)+" "+"hired at "+self.job.job_title+" by "+self.job.company
    