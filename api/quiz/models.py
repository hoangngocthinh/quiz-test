from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import UuidTimeStamModel
from quiz.choices import QUESTION_TYPES, ESSAY
from user.models import User


# Create your models here.
class Quiz(UuidTimeStamModel):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User, related_name="quiz_owner", on_delete=models.DO_NOTHING, default=None
    )
    is_active = models.BooleanField(default=True)


class Question(UuidTimeStamModel):
    quiz = models.ForeignKey(
        Quiz, related_name="question_quiz", on_delete=models.deletion.CASCADE
    )
    type = models.CharField(max_length=30, choices=QUESTION_TYPES, default=ESSAY)
    question_text = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=20)


class QuestionChoice(UuidTimeStamModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class QuizSession(UuidTimeStamModel):
    quiz = models.ForeignKey(
        Quiz, related_name="session_quiz", on_delete=models.deletion.CASCADE
    )
    session_code = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=None, null=True, blank=True)
    end_time = models.DateTimeField(default=None, null=True, blank=True)
    max_participants = models.IntegerField(validators=[MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)


class Participant(UuidTimeStamModel):
    quiz = models.ForeignKey(
        Quiz, related_name="participant_quiz", on_delete=models.deletion.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="user_participant", on_delete=models.deletion.CASCADE
    )
    quiz_session = models.ForeignKey(
        QuizSession, related_name="quiz_session_participant", on_delete=models.deletion.CASCADE
    )
    score = models.IntegerField(validators=[MinValueValidator(0)], default=0)


class Answer(UuidTimeStamModel):
    participant = models.ForeignKey(
        Quiz, related_name="participant_answer", on_delete=models.deletion.CASCADE
    )
    question = models.ForeignKey(
        Question, related_name="question_answer", on_delete=models.deletion.CASCADE
    )
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    answered_at = models.DateTimeField(default=None, null=True, blank=True)


class Leaderboard(UuidTimeStamModel):
    quiz_session = models.ForeignKey(
        QuizSession, related_name="quiz_session_leader_board", on_delete=models.deletion.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="user_leader_board", on_delete=models.deletion.CASCADE
    )
    score = models.IntegerField(validators=[MinValueValidator(0)])
    rank = models.IntegerField(validators=[MinValueValidator(1)])
