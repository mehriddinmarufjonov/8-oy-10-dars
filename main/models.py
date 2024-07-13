from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


def file_size(value):
    limit = 300 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Dars uchun yuklanayotgan video hajmi 300MB dan oshmasligi kerak')


class LessonVideo(models.Model):
    video = models.FileField(
        upload_to='lesson/videos/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'wmv']),
            file_size
        ]
    )
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f'{self.lesson.name} - {self.video.name}'
