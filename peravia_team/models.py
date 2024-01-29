from django.db import models
from utilities.utils import *
from django.utils.translation import gettext_lazy as _
# ----------------------------------------------------------
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.position}{ext}"
    return f"team/{final_name}"

# ----------------------------------------------------------
class Team(models.Model):
    Positions = (
        (_('Co-Founder & CEO'), _('Co-Founder & CEO')),
        (_('International Procurement Manager'), _('International Procurement Manager')),
        (_('Procurement Manager'), _('Procurement Manager')),
        (_('Administrative Manager'), _('Administrative Manager')),
        (_('Financial Manager'), _('Financial Manager')),
        (_('Industrial Accountant'), _('Industrial Accountant')),
        (_('IT Manager'), _('IT Manager')),
        (_('Brand Manager'), _('Brand Manager'))

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
