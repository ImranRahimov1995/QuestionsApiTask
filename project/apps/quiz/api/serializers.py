from rest_framework import serializers
from ..models import *
from django.contrib.contenttypes.models import ContentType

class MultipleChooseSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = MultipleChoose
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('text',)



class QuestionSerializer(serializers.ModelSerializer):
    multiple = MultipleChooseSerializer(required=False)

    class Meta:
        model = Question
        fields = ('body','multiple')

    def create(self,validated_data):
        multiple_data = validated_data.pop('multiple')
        options = MultipleChoose.objects.create(**multiple_data)
        newQuestion = Question()
        newQuestion.quiz = Quiz.objects.first()
        newQuestion.body = validated_data['body']
        newQuestion.content_type = ContentType.objects.get_for_model(MultipleChoose)
        newQuestion.object_id = options.pk
        newQuestion.save()

        return newQuestion


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title',)