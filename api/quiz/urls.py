from django.urls import path
from quiz import views

urlpatterns = [
    path("", views.QuizViewAPI.as_view(), name="quiz-list"),
    path("question", views.QuestionViewAPI.as_view(), name="question-list"),
    path("sessions", views.QuizSessionAPI.as_view(), name="session"),
    path("sessions/join", views.JoinQuizSessionView.as_view(), name="sessions-join"),
    path("sessions/<uuid:session_id>/leaderboard", views.LeaderBoardView.as_view(), name="leaderboard"),
    path("answers", views.AnswerViewSet.as_view(), name="answers"),
]
