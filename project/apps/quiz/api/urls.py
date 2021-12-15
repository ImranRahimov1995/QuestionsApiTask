from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path('create/quiz/',views.CreateQuizView.as_view()),
    path('create/<str:quiz>/question/',views.CreateQuestionView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
