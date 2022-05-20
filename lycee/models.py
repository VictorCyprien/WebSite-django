from datetime import datetime
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
    return '{}'.format(self.name)

  class Meta:
    verbose_name_plural = 'Cursus'
    permissions = (
      ("check_cursus", "Can view the cursus"),
    )


class Student(models.Model):
  first_name = models.CharField(
    max_length=50,
    blank=False,
    null=False
  )

  birth_date = models.DateField(
    verbose_name='date of birth',
    help_text="YYYY-MM-DD",
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
    return f"{self.last_name} {self.first_name}"

  class Meta:
    permissions = (
      ("check_student", "Can view the student"),
      ("create_student", "Can create a student"),
      ("update_student", "Can update a student"),
    )



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
    default=datetime.now(),
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
    help_text="HH:MM",
  )

  end_time = models.TimeField(
    verbose_name="end_time",
    help_text="HH:MM",
  )

  class Meta:
    permissions = (
      ("check_presence", "Can view a presence"),
      ("create_presence", "Can create a presence"),
      ("update_presence", "Can update a presence"),
    )


class Matiere(models.Model):
  name = models.CharField(
    verbose_name="name",
    help_text="Name of the Matiere",
    blank=False,
    null=False, # pas de champ null (a conjuguer avec default
    default="",
    max_length=255, # taille maximale du champ
  )

  start_time = models.DateTimeField(
    verbose_name="Start time"
  )

  end_time = models.DateTimeField(
    verbose_name="End time"
  )

  cursus = models.ForeignKey(
    Cursus,
    related_name="Cursus",
    on_delete=models.CASCADE, # necessaire selon la version de Django
    null=False
  )


class Teacher(models.Model):
  name = models.CharField(
    verbose_name="name",
    help_text="Name of the Teacher",
    blank=False,
    null=False, # pas de champ null (a conjuguer avec default
    default="",
    max_length=255, # taille maximale du champ
  )

  matiere = models.ForeignKey(
    Matiere,
    related_name="Matiere",
    on_delete=models.CASCADE, # necessaire selon la version de Django
    null=False
  )