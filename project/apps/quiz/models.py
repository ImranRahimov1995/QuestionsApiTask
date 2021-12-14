from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Quiz(models.Model):
    """
        Модель Опроса

    """

    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField()


class Question(models.Model):
    """
        Модель Вопроса :


        body - это тело вопроса
        answer для разного выбора типа ответа
    """
    quiz = models.ForeignKey(Quiz,
                             on_delete=models.CASCADE,
                             related_name='question')

    body = models.CharField(max_length=300)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text',
                                         'multiplechoose',
                                         # 'oneChoose',
                                     )})
    object_id = models.PositiveIntegerField()
    answer = GenericForeignKey('content_type', 'object_id')


class Text(models.Model):
    text = models.CharField(max_length=255)


class MultipleChoose(models.Model):
    first = models.CharField(max_length=50)
    second = models.CharField(max_length=50)
    third = models.CharField(max_length=50, blank=True, null=True)
    fourth = models.CharField(max_length=50, blank=True, null=True)
    fifth = models.CharField(max_length=50, blank=True, null=True)
