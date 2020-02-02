from django.urls import path,include
from .views import *
urlpatterns = [
    path('save', addAlltoDb),
    path('get', get_question.as_view()),
    # path('answer', answer),
    # path('get_all_q', get_all_q),
    path('get_all_question', get_all_question.as_view()),
]
