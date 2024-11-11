from rest_framework import serializers

from quiz.models import Quiz, Question, Answer, QuestionChoice, QuizSession
from socket_api.services import update_leaderboard


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'created_by']

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ['id', 'choice_text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_text', 'type', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)

        for choice_data in choices_data:
            QuestionChoice.objects.create(question=question, **choice_data)

        return question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['participant', 'question', 'answer_text', 'is_correct', 'answered_at']

    def create(self, validated_data):
        answer = super().create(validated_data)
        question = validated_data['question']
        participant = validated_data['participant']

        if question.question_type == 'multiple_choice':
            correct_choice = question.choices.filter(is_correct=True).first()
            answer.is_correct = answer.answer_text == correct_choice.choice_text
        else:
            answer.is_correct = answer.answer_text.strip().lower() == question.correct_answer.strip().lower()

        answer.save()
        score_increment = 10 if answer.is_correct else 0  # Ví dụ: cộng 10 điểm nếu đúng
        participant.score += score_increment
        participant.save()

        # Gọi hàm update_leaderboard để gửi cập nhật lên WebSocket
        update_leaderboard(participant.quiz_session.id, participant.user.id, participant.score)
        return answer


class QuizSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSession
        fields = ['id', 'quiz', 'session_code', 'start_time', 'end_time', 'max_participants']
        read_only_fields = ['id', 'session_code']

    def create(self, validated_data):
        validated_data['session_code'] = self._generate_session_code()
        validated_data['is_active'] = True
        return super().create(validated_data)

    def _generate_session_code(self):
        import uuid
        return str(uuid.uuid4())
