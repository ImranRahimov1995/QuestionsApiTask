from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import api
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)

urlpatterns = [
    #auth
    path('auth/',
         include('rest_framework.urls', namespace='rest_framework')),

    #For admin
    path('create/quiz/',api.CreateQuizView.as_view()),
    path('create/<str:quiz>/question/',api.CreateQuestionView.as_view()),
    path('get/<str:quiz>/<pk>/',api.ChangeQuestionView.as_view()),
    path('get/<str:title>/', api.ChangeQuizView.as_view()),

    #For users,get all active()
    path('quiz/all/',api.QuizListView.as_view()),
    path('quiz/<str:title>/', api.QuestionsView.as_view()),
    path('<quiz>/<pk>/create/answer/',api.AnswerCreateView.as_view()),
    path('<user_id>/<quiz>/answers/',api.UserQuizAnswerView.as_view()),
    path('<quiz>/answers/',api.QuizAllAnswersView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
