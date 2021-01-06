from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    # path('', views.index),
    # path('ask/', views.ask_question, name='ask'),
    # path('<int:q_id>/', views.question_detail, name='q_id'),
    path('<int:id>/', views.QuestionDetailView.as_view(), name='id'),
    path('', views.IndexView.as_view(), name='all_questions'),
    path('ask/', views.AskView.as_view(), name='ask'),
    path('<int:id>/like/', views.LikeView.as_view(), name='like'),

]