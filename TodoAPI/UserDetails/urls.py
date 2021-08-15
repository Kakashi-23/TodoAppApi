from django.urls import path, include
from .views import TodoDetailList

urlpatterns = [
    path('savedata', TodoDetailList.as_view()),

]
