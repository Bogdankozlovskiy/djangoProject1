from django.urls import path
from exam import views


urlpatterns = [
    path("exam/", views.ExamListCreateAPIView.as_view()),
    path("exam/<int:pk>/", views.ExamDetailAPIView.as_view()),
    path("question/", views.QuestionListCreate.as_view()),
    path("question/<int:pk>", views.QuestionDetail.as_view())
]
