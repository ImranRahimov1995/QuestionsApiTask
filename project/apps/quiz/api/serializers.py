from rest_framework import serializers
from ..models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MultipleChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoose
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    multiple = MultipleChooseSerializer(required=False, label='Options')

    class Meta:
        model = Question
        fields = ('body', 'multiple')

    def create(self, validated_data):
        multiple_options = validated_data.pop('multiple')

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


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
