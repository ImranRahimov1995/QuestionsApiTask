from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path('quizes/all/',views.QuizView.as_view()),
    path('create/<str:quiz>/question',views.CreateQuestionView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
