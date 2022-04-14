from audioop import reverse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Cursus, Student
from .forms import StudentForm
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse


class StudentCreateView(CreateView):

  model = Student
  form_class = StudentForm
  template_name = 'lycee/student/create.html'

  def get_success_url(self) -> str:
      return reverse("detail_student", args=(self.object.pk,))


def index(request):
  result_list = Cursus.objects.order_by('name')

  template = loader.get_template("lycee/index.html")

  context = {
    "liste": result_list,
  }

  return HttpResponse(template.render(context, request))

def detail(request, cursus_id):
  resp = 'result for cursus {}'.format(cursus_id)
  return HttpResponse(resp)

def detail_student(request, student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {'liste' : result_list}

  return render(request, 'lycee/student/detail_student.html', context)
