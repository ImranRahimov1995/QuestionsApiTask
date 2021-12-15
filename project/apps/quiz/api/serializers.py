from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from ..models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MultipleChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoose
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    multiple_options = MultipleChooseSerializer(required=False, label='Options')
    options = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ('pk', 'body', 'multiple_options', 'options')

    def create(self, validated_data):
        multiple_options = validated_data.pop('multiple_options')

        if multiple_options['second'] != '':
            options = MultipleChoose.objects.create(**multiple_options)
        else:
            text = multiple_options['first']
            options = Text.objects.create(text=text)

        newQuestion = Question()
        newQuestion.quiz = validated_data['quiz']
        newQuestion.body = validated_data['body']
        newQuestion.content_type = ContentType.objects.get(
            app_label='quiz',
            model=options._meta.model_name)
        newQuestion.object_id = options.pk
        newQuestion.save()

        return newQuestion

    def update(self, instance, validated_data):
        multiple_options = validated_data.pop('multiple_options')
        counter = 0        
        one_field = []
        for k in multiple_options.keys():
            if multiple_options[k] != '':
                one_field.append(k)
                counter += 1
        if counter > 1:
            options = MultipleChoose.objects.create(**multiple_options)
        elif counter <= 1: 
            text = multiple_options[one_field[0]]
            options = Text.objects.create(text=text)
        counter=0   
        instance.options = options
        instance.save()
        return super().update(instance, validated_data)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('body',)

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionBodySerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = ('selected','second_selected',
                    'third_selected','question','user')