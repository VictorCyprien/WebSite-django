from django import forms
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