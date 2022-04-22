from audioop import reverse
import json
from django.shortcuts import redirect, render
from datetime import datetime

# Create your views here.

from django.http import HttpResponse
from .models import Cursus, Student, Presence
from .forms import CursusCallForm, StudentForm, PresenceForm
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


class StudentCreateView(CreateView):

  model = Student
  form_class = StudentForm
  template_name = 'lycee/student/create.html'

  def get_success_url(self) -> str:
      return reverse("detail_student", args=(self.object.pk,))

class CursusCallView(CreateView):
  form_class = CursusCallForm
  template_name = 'lycee/cursuscall/detail_cursuscall.html'


class PresenceCreateView(CreateView):

  model = Presence
  form_class = PresenceForm
  template_name = 'lycee/presence/create.html'

  def get_success_url(self) -> str:
      return reverse("detail_presence", args=(self.object.pk,))


def index(request):
  result_list = Cursus.objects.order_by('name')

  template = loader.get_template("lycee/index.html")

  context = {
    "liste": result_list,
  }

  return HttpResponse(template.render(context, request))

def detail_grade(request, cursus_id):

  query = Student.objects.filter(cursus=cursus_id).order_by('last_name')
  cursus = Cursus.objects.get(pk=cursus_id)

  context = {'liste': query, 'cursus': cursus}

  return render(request, 'lycee/detail_grade.html', context)


def detail_student(request, student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {'liste' : result_list}

  return render(request, 'lycee/student/detail_student.html', context)


def update_student(request, student_id):
  student = Student.objects.get(pk=student_id)
  form = None

  if request.method == 'POST':
      form = StudentForm(request.POST, instance=student)
      if form.is_valid():
          form.save()
          return redirect('detail_student', student_id)
  else:
      form = StudentForm(instance=student)
  
  return render(request, 'lycee/student/update.html', {'form': form})


def cursus_call(request, cursus_id):
  if request.method == "POST":
    print(request.POST)
    for student_id in request.POST.getlist('missing'):
      print(student_id)

      date = request.POST.getlist('date_cursuscall')
      str_date = "".join(date)

      new_missing = Presence(
        reason="Missing",
        isMissing=True,
        date=str_date,
        student=Student.objects.get(pk=student_id),
        start_time="9:00",
        end_time="17:00",
      )

      new_missing.save()
    return redirect('detail_all_presence')

  result_list = Student.objects.filter(cursus=cursus_id).order_by('last_name')

  context = {'liste' : result_list}

  return render(request, 'lycee/cursuscall/detail_cursuscall.html', context)


def detail_presence(request, presence_id):
  result_list = Presence.objects.get(pk=presence_id)

  context = {'liste' : result_list}

  return render(request, 'lycee/presence/detail_presence.html', context)


def update_presence(request, presence_id):
  presence = Presence.objects.get(pk=presence_id)
  form = None

  if request.method == 'POST':
      form = PresenceForm(request.POST, instance=presence)
      if form.is_valid():
          form.save()
          return redirect('detail_presence', presence_id)
  else:
      form = PresenceForm(instance=presence)
  
  return render(request, 'lycee/presence/update.html', {'form': form})


def detail_all_presence(request):

  result_list = Presence.objects.all().order_by('student__last_name')
  cursus = Cursus.objects.all()

  context = {'cursus': cursus, 'presence': result_list}

  return render(request, 'lycee/presence/index.html', context)