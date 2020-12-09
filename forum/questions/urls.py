from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('', views.index),
    path('ask/', views.ask_question, name='ask'),
    path('<int:q_id>/', views.question_detail, name='q_id'),

]