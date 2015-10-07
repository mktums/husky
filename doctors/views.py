from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from .forms import RecordModelForm
from .models import Record
from .utils import format_date


def index(request):
    form = RecordModelForm(request.POST or None)
    if form.is_valid():
        data = form.save()
        messages.success(
            request,
            'Вы успешно записаны ко врачу {0}'
            ' на {1:%H:%M} {1:%d.%m.%Y}'.format(
                data.doctor.name, datetime.combine(data.date, data.time)
            )
        )
        return redirect(reverse('index'))
    return render(request, 'base.html', {'form': form, 'settings': settings})


def get_excluded_dates_by_doctor(request, doctor_id):
    qs = Record.objects.excluded_dates(doctor_id)
    exclude_dates = {'dates': [format_date(result['date']) for result in qs]}
    return JsonResponse(exclude_dates)


def get_time_by_doctor_and_date(request, doctor_id, date):
    date = format_date(date, reverse=True)
    available_time = Record.objects.available_time(doctor_id, date)
    return JsonResponse(available_time)
