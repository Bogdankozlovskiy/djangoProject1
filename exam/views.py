from rest_framework import generics
from exam.serializers import ExamTicketListSerializer, ExamTicketDetailSerializer, CreateExamTicketSerializer, \
    QuestionsSerializer, QuestionsDetailSerializer, QuestionCreateSerializer
from exam.models import ExamTicket, Question


class ExamListCreateAPIView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateExamTicketSerializer
        if self.request.method == "GET":
            return ExamTicketListSerializer

    queryset = ExamTicket.objects.all()


class ExamDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ExamTicketDetailSerializer
    queryset = ExamTicket.objects.all()


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return QuestionCreateSerializer
        if self.request.method == "GET":
            return QuestionsSerializer


class QuestionDetail(generics.RetrieveAPIView):
    serializer_class = QuestionsDetailSerializer
    queryset = Question.objects.all()
