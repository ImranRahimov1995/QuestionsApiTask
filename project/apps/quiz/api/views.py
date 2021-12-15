from rest_framework import generics ,views,permissions,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import *
from ..models import *


class QuizView(views.APIView):

    def get(self,request):
        quizes = Quiz.objects.all()
        serializer = QuizSerializer(quizes,many=True)

        return Response({'quizes':serializer.data})




class CreateQuestionView(generics.CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]

