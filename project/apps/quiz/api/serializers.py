from rest_framework import serializers
from ..models import *





class MultipleChoose(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoose
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('text',)



class QuestionSerializer(serializers.ModelSerializer):
    multiple = MultipleChoose(required=False)

    class Meta:
        model = Question
        fields = ('body','multiple')

    def create(self, validated_data):
        print(validated_data)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title',)