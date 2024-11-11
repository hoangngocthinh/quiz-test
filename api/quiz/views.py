from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from core.redis import RedisService
from quiz.exceptions import QuizException
from quiz.models import Quiz, Question, QuizSession, Participant, Answer
from quiz.serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, QuizSessionSerializer


class QuizViewAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        quiz_id = request.query_params.get("quiz_id")
        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            raise QuizException
        queryset = Question.objects.filter(quiz=quiz)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuizSessionAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        quiz_id = request.data.get("quiz")
        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            raise QuizException

        if quiz.created_by != request.user:
            return Response({"error": "You do not have permission to create a session for this quiz."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = QuizSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JoinQuizSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session_code = request.data.get('session_code')
        quiz_id = request.data.get('quiz_id')

        try:
            session = QuizSession.objects.get(session_code=session_code)
            Participant.objects.create(user_id=request.user.id, quiz_session=session, quiz_id=quiz_id)
            return Response({"message": "User joined the session successfully", "session_id": session.id},
                            status=status.HTTP_200_OK)
        except QuizSession.DoesNotExist:
            return Response({"error": "Session not found or is no longer active"}, status=status.HTTP_404_NOT_FOUND)


class AnswerViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class LeaderBoardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        session_id = kwargs.get("session_id")
        leaderboard = RedisService(session_id).get_leaderboard(top_n=10)
        if leaderboard:
            return Response(leaderboard)
        else:
            participants = (Participant.objects.filter(quiz_session_id=session_id)
                            .annotate(total_score=Sum('score')).order_by('-total_score'))
            if participants:
                leaderboard = [
                    {
                        "user_id": participant.user.id,
                        "username": participant.user.username,
                        "score": participant.total_score,
                        "rank": index + 1
                    }
                    for index, participant in enumerate(participants)
                ]

            return Response(leaderboard)
