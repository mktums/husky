from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Record
from .utils import today, normalize_weekdays


class RecordModelForm(ModelForm):
    def clean(self):
        cleaned_data = super(RecordModelForm, self).clean()

        time = cleaned_data.get('time')
        date = cleaned_data.get('date')
        doctor = cleaned_data.get('doctor')

        if time:
            try:
                assert time.hour in range(*settings.WORKING_HOURS)
                assert time.hour in Record.objects.available_time(doctor, date).get('hours')
            except AssertionError:
                raise ValidationError("Выберите правильное время.")

        if date:
            try:
                assert date
                assert date >= today()
                assert date.isoweekday() not in normalize_weekdays(*settings.DISABLED_WEEKDAYS)
                assert date not in Record.objects.excluded_dates(doctor)
            except AssertionError:
                raise ValidationError("Выберите правильную дату.")

    class Meta:
        model = Record
        fields = ('doctor', 'date', 'time', 'name')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ф.И.О.'
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Имя врача',
            }),
            'date': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'time': forms.Select(attrs={
                'class': 'form-control',
            }),

        }
