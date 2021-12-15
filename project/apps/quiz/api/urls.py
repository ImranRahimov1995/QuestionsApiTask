from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('auth/',
         include('rest_framework.urls', namespace='rest_framework')),

    path('create/quiz/',views.CreateQuizView.as_view()),
    path('create/<str:quiz>/question/',views.CreateQuestionView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
