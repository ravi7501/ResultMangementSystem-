from django.db import models

# Create your models here.
class Students(models.Model):
    Sr_No=models.IntegerField(primary_key=True )
    Division=models.CharField(max_length=3)
    RollNo=models.IntegerField(null=True)
    Name=models.CharField(max_length=30,blank=True)
    Accountancy=models.IntegerField(null=True)
    English=models.IntegerField(null=True)
    Maths=models.IntegerField(null=True)
    Economics=models.IntegerField(null=True)
    Business_Studies=models.IntegerField(null=True)
    Total=models.IntegerField(null=True)
    Average=models.IntegerField(null=True)
    Grade=models.CharField(max_length=5)
    Result=models.CharField(max_length=10)

    def __str__ (self):
        return self.Name