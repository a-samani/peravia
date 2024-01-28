from django.db import models
from utilities.utils import *

# ----------------------------------------------------------
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.position}{ext}"
    return f"team/{final_name}"

# ----------------------------------------------------------
class Team(models.Model):
    Positions = (
        ('Co-Founder & CEO', 'Co-Founder & CEO'),
        ('International Procurement Manager','International Procurement Manager'),
        ('Procurement Manager','Procurement Manager'),
        ('Administrative Manager','Administrative Manager'),
        ('Financial Manager','Financial Manager'),
        ('Industrial Accountant','Industrial Accountant'),
        ('IT Manager','IT Manager'),
        ('Brand Manager','Brand Manager')
    )
    Rank = tuple([(i+1,str(i+1)) for i in range(len(Positions))])
    name = models.CharField(max_length=150)
    family = models.CharField(max_length=200)
    position = models.CharField(max_length=200, choices=Positions)
    rank = models.IntegerField(choices=Rank, default=0)
    member_image = models.ImageField(upload_to=upload_image_path,blank=True,null=True)
    linkedin = models.CharField(max_length=250)

    class Meta:
        ordering = ['rank']
        verbose_name = 'Team'
        verbose_name_plural = 'Team members'

    def __str__(self):
        return "{} {} {}".format(self.name, self.family, self.position)
