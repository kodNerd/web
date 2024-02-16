from django.db import models

class Students(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adm_no = models.PositiveBigIntegerField()
   
    def __str__(self):
        return f'Student Name: {self.first_name} {self.last_name} Admn No: {self.adm_no}'
