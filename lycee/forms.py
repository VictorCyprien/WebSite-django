from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms.models import ModelForm
from .models import Student, Presence

class StudentForm(ModelForm):

    class Meta:

        model = Student

        fields = (
            "first_name",
            "last_name",
            'birth_date',
            'email',
            'phone',
            'comments',
            'cursus',
        )


class PresenceForm(ModelForm):

    student = forms.ModelChoiceField(queryset=Student.objects.order_by('last_name'))

    class Meta:

        model = Presence

        fields = (
            "reason",
            "isMissing",
            'date',
            'student',
            'start_time',
            'end_time',
        )


class CursusCallForm(forms.Form):
    date = forms.DateInput()
    
    choices = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple,
    )



class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", )
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.is_teacher = True
        if commit:
            user.save()
        return user