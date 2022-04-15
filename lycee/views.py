from audioop import reverse
from django.shortcuts import redirect, render

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

  query = Student.objects.filter(cursus=cursus_id)

  context = {'liste': query}

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
    cursus_call = request.POST.getlist('call')
    print(cursus_call)

  result_list = Student.objects.filter(cursus=cursus_id)

  context = {'liste' : result_list}

  return render(request, 'lycee/cursuscall/detail_cursuscall.html', context)


def detail_presence(request, presence_id):
  result_list = Presence.objects.get(pk=presence_id)

  context = {'liste' : result_list}

  return render(request, 'lycee/presence/detail_presence.html', context)


def detail_all_presence(request):

  query = Presence.objects.all()

  context = {'liste': query}

  return render(request, 'lycee/presence/index.html', context)