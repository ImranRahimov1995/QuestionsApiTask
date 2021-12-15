from rest_framework import generics, views, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import *
from ..models import *
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from django.utils import timezone

now = timezone.now()


# Auth______________________________________
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# End Auth_________________________________

class CreateQuestionView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        now = timezone.now()
        quiz = Quiz.objects.filter(
            Q(title=self.kwargs['quiz']) |
            Q(title=self.kwargs['quiz'].capitalize()) & Q(end_date__gte=now)

        ).first()
        queryset = Question.objects.filter(quiz=quiz)
        return queryset

    def perform_create(self, serializer):
        now = timezone.now()
        quiz = Quiz.objects.filter(
            Q(title=self.kwargs['quiz']) |
            Q(title=self.kwargs['quiz'].capitalize()) & Q(end_date__gte=now)

        ).first()

        if not quiz:
            raise ValidationError('The quiz is not exists')
        serializer.save(quiz=quiz)


class ChangeQuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        quiz = Quiz.objects.filter(
            Q(title=self.kwargs['quiz']) |
            Q(title=self.kwargs['quiz'].capitalize()) & Q(end_date__gte=now)

        ).first()
        queryset = Question.objects.filter(quiz=quiz)
        return queryset


class ChangeQuizView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    lookup_field = 'title'
    permission_classes = [IsAdminUser, ]
    queryset = Quiz.objects.filter(end_date__gte=now)


class CreateQuizView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAdminUser]


class QuizListView(generics.ListAPIView):
    pass
