from django.db import models


# Create your models here.
# TODO DO REAL MODEL
class Hour(models.Model):
    internalid = models.IntegerField('Cat serial number from the csv', null=True)
    name = models.CharField('Name of the cat', max_length=1000, null=True)
    breed = models.CharField('Breed of the cat', max_length=100, null=True)
    birth = models.DateField('Birthdate of the cat', null=True)
    gender = models.CharField('Gender of the cat', max_length=100, null=True)
    fur = models.CharField('Fur code of the cat', max_length=100, null=True)
    number = models.CharField('Identification number of the cat', max_length=200, null=True)
    title = models.CharField('Titles of the cat', max_length=100, null=True)
    father = models.CharField('Identification of the Father of the cat', max_length=200, null=True)
    mother = models.CharField('Identification of the Mother of the cat', max_length=200, null=True)
    site = models.CharField('Site from which the cat is from', max_length=20, null=True)
    health = models.CharField('Health information about the cat', max_length=500, null=True)
    fatherLink = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="fatherLink_cat")
    motherLink = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="motherLink_cat")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "NOT FOUND"
