from rest_framework import generics, views, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import *
from ..models import *
from django.db.models import Q

from rest_framework.exceptions import ValidationError
class QuizView(views.APIView):

    def get(self, request):
        quizes = Quiz.objects.all()
        serializer = QuizSerializer(quizes, many=True)

        return Response({'quizes': serializer.data})


class CreateQuestionView(generics.CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        quiz = Quiz.objects.filter(
            Q(title=self.kwargs['quiz']) |
            Q(title=self.kwargs['quiz'].capitalize())
        ).first()
        print(quiz)
        if not quiz:
            raise ValidationError('The quiz is not exists')
        serializer.save(quiz=quiz)
