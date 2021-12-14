from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class Quiz(models.Model):
    """
        Модель Опроса

    """

    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering =('-start_date',)



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
    options = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return self.body


    

class Text(models.Model):
    text = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.text

class MultipleChoose(models.Model):
    first = models.CharField(max_length=50,blank=True,null=True)
    second = models.CharField(max_length=50,blank=True,null=True)
    third = models.CharField(max_length=50, blank=True, null=True)
    fourth = models.CharField(max_length=50, blank=True, null=True)
    fifth = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'A. {self.first} \
                 B. {self.second} \
                 C. {self.third}  \
                 D. {self.fourth} \
                 E. {self.fifth} '

#____________________________

class Answer(models.Model):

    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answer')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='my_answer')
    selected = models.CharField(max_length=255)
    second_selected = models.CharField(max_length=255,blank=True,null=True)
    third_selected = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        if self.second_selected or self.third_selected:
            return f'A. {self.selected} \
                     B. {self.second_selected} \
                     C. {self.third_selected} '
        
        return self.selected