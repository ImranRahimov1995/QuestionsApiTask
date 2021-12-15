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
    queryset = Quiz.objects.all()


class CreateQuizView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAdminUser]

#_____For users
class QuizListView(generics.ListAPIView):
    """Get all active quiz for now """
    serializer_class = QuizSerializer
    queryset = Quiz.objects.filter(end_date__gte=now)

class QuestionsView(generics.ListAPIView):
    """Get all quiz question"""
    serializer_class = QuestionSerializer
    queryset = Quiz.objects.filter(end_date__gte=now)

    def get_queryset(self):
        quiz = Quiz.objects.filter(
            Q(title=self.kwargs['title']) |
            Q(title=self.kwargs['title'].capitalize()) & Q(end_date__gte=now)
        ).first()
        queryset = Question.objects.filter(quiz=quiz)
        return queryset

class UserQuizAnswerView(generics.ListAPIView):
    """Get user quiz answers"""
    serializer_class = AnswerSerializer

    def get_queryset(self):
        quiz = Quiz.objects.filter(
            title=self.kwargs['quiz']
        ).first()
        user = User.objects.filter(pk=self.kwargs['user_id']).first()
        if user:
            queryset = user.my_answer.filter(question__quiz=quiz)
            return queryset
        else:
            raise ValidationError("User id isn't correct")



class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        question = Question.objects.filter(pk=self.kwargs['pk']).first()
        if not question:
            raise ValidationError('Question does not exists')
        user = self.request.user
        if user.is_authenticated:
             serializer.save(question=question,user=user)
        serializer.save(question=question)

class QuizAllAnswersView(generics.ListAPIView):
    """Get user quiz answers"""
    serializer_class = AnswerSerializer

    def get_queryset(self):
        quiz = Quiz.objects.filter(
            title=self.kwargs['quiz']
        ).first()
        queryset = Answer.objects.filter(question__quiz=quiz)
        return queryset