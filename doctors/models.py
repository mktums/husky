from django.conf import settings
from django.db import models, IntegrityError
from django.db.models import Count
from django.utils.datetime_safe import datetime
from .utils import today, format_date


class Doctor(models.Model):
    name = models.CharField('имя', max_length=255)

    class Meta:
        verbose_name = 'врача'
        verbose_name_plural = 'врачи'
        ordering = ('name', )

    def __str__(self):
        return self.name


class RecordManager(models.Manager):
    def excluded_dates(self, doctor_id=None):
        if not doctor_id:
            raise IntegrityError('Doctor ID is not specified.')
        qs = self.get_queryset().values('date').annotate(
            day_records=Count('date')
        ).filter(
            date__gte=today(),
            doctor=doctor_id,
            day_records=len(range(*settings.WORKING_HOURS))
        ).order_by('name')
        return qs

    def available_time(self, doctor_id=None, day=None):
        if not doctor_id:
            raise IntegrityError('Doctor ID is not specified.')
        if not day:
            raise IntegrityError('Day is not specified.')
        qs = self.get_queryset().filter(
            doctor=doctor_id, date=day).values('time')
        all_hours = set(range(*settings.WORKING_HOURS))
        if day == today():
            now = datetime.now()
            all_hours ^= set(range(settings.WORKING_HOURS[0], now.hour + 1))
            qs = qs.filter(time__gte=now)
        qs = {
            'hours': list(all_hours ^ {record['time'].hour for record in qs})
        }
        return qs


class Record(models.Model):
    doctor = models.ForeignKey(
        Doctor, verbose_name='Врач', related_name='records'
    )
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    name = models.CharField('Ф.И.О. пациента', max_length=255)

    objects = RecordManager()

    class Meta:
        verbose_name = 'запись на прием'
        verbose_name_plural = 'записи на прием'
        ordering = ('date', 'time')
        unique_together = ('date', 'time', 'doctor')

    def __str__(self):
        return 'Запись к {0} на {1:%H:%M} {2}'.format(
            self.doctor.name, self.time, format_date(self.date)
        )
