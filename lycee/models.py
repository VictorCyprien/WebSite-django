from django.db import models

# Create your models here.
class Cursus(models.Model):
  name = models.CharField(
    max_length=50,
    blank=False,
    null=True,
    default='aucun',
  )

  year_from_bac=models.SmallIntegerField(
    help_text ="year since le bac",
    verbose_name="year",
    blank=False,
    null=True,
    default=0
  )
  
  scholar_year = models.CharField(
    max_length=9,
    blank=False,
    null=True,
    default='0000-00001'
  )
  
  def __str__(self):
    return '{} {}: {}'.format(self.name,self.year_from_bac,self.scholar_year)

  class Meta:
    verbose_name_plural = 'Cursus'


class Student(models.Model):
  first_name = models.CharField(
    max_length=50,
    blank=False,
    null=False
  )

  birth_date = models.DateField(
    verbose_name='date of birth',
    blank=False,
    null=False
  )

  last_name = models.CharField(
    verbose_name="lastname",
    help_text="last name of the student",
    blank=False, # pas de champ vide
    null=False, # pas de champ null (a conjuguer avec default
    default="???",
    max_length=255, # taille maximale du champ
  )

  phone = models.CharField(
    verbose_name="phonenumber",
    help_text="phone number of the student",
    blank=False, # pas de champ vide
    null=False, # pas de champ null (a conjuguer avec default
    default="0999999999",
    max_length=10, # taille maximale du champ
  )

  email = models.EmailField(
    verbose_name="email",
    help_text="phone number of the student",
    blank=False, # pas de champ vide
    null=False, # pas de champ null (a conjuguer avec default
    default="x@y.z",
    max_length=255, # taille maximale du champ
  )

  comments = models.CharField(
    verbose_name="comments",
    help_text="some comments about the student",
    blank=True,
    null=False, # pas de champ null (a conjuguer avec default
    default="",
    max_length=255, # taille maximale du champ
  )

  cursus = models.ForeignKey(
    Cursus,
    related_name="cursus",
    on_delete=models.CASCADE, # necessaire selon la version de Django
    null=True
  )

  def __str__(self):
    return f"{self.first_name} {self.last_name}"



class Presence(models.Model):
  reason = models.CharField(
    verbose_name="reason",
    help_text="Reason about student missing",
    blank=False,
    null=False, # pas de champ null (a conjuguer avec default
    default="",
    max_length=255, # taille maximale du champ
  )

  isMissing = models.BooleanField(
    verbose_name="isMissing",
    help_text="Student missing ?",
    blank=False, # pas de champ vide
    null=False, # pas de champ null (a conjuguer avec default
    default=True,
  )

  date = models.DateField(
    verbose_name='Date of Student Missing',
    blank=False,
    null=False,
  )

  student = models.ForeignKey(
    Student,
    related_name="Student",
    on_delete=models.CASCADE, # necessaire selon la version de Django
    null=False
  )


  start_time = models.TimeField(
    verbose_name="start_time",
  )

  end_time = models.TimeField(
    verbose_name="end_time",
  )
