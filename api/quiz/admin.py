

from django.contrib import admin

# Register your models here.
from quiz.models import Quiz, Question, QuestionChoice, QuizSession, Participant, Answer, Leaderboard


class QuizAdmin:
    list_display = (
        "id",
        "name",
        "created_by",
        "is_active",
    )


class QuestionAdmin:
    list_display = (
        "id",
        "quiz",
        "type",
        "question_text",
        "correct_answer",
    )


class QuestionChoiceAdmin:
    list_display = (
        "id",
        "question",
        "choice_text",
        "is_correct",
    )


class QuizSessionAdmin:
    list_display = (
        "id",
        "quiz",
        "session_code",
        "start_time",
        "end_time",
        "max_participants",
        "is_active",
    )


class ParticipantAdmin:
    list_display = (
        "id",
        "quiz",
        "user",
        "quiz_session",
        "score",
    )


class AnswerAdmin:
    list_display = (
        "id",
        "participant",
        "question",
        "answer_text",
        "is_correct",
        "answered_at",
    )


class LeaderboardAdmin:
    list_display = (
        "id",
        "quiz_session",
        "user",
        "score",
        "rank",
    )


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)
admin.site.register(QuizSession, QuizSessionAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Leaderboard, LeaderboardAdmin)
