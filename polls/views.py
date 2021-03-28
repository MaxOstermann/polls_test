from rest_framework import viewsets
from django.utils import timezone
from polls.models import Question, Poll, Attempt, Answer
from polls.serializers import QuestionSerializer, PollSerializer, \
    AttemptSerializer, AnswerSerializer


class PollViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Polls.
    """
    queryset = Poll.objects.filter(
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now(),
    )
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Questions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AttemptViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Attempts.
    """
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Answers.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
