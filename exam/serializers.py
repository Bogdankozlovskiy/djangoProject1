from exam.models import ExamTicket, Question, Answer
from rest_framework import serializers


class ExamTicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTicket
        fields = ["title", "created"]


class CreateExamTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTicket
        fields = ["title", "questions"]


class QuestiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ExamTicketDetailSerializer(serializers.ModelSerializer):
    questions = QuestiosSerializer(many=True)

    class Meta:
        model = ExamTicket
        fields = "__all__"


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["is_correct", "text"]


class QuestionCreateSerializer(serializers.ModelSerializer):
    answer_set = AnswerCreateSerializer(many=True)

    class Meta:
        model = Question
        fields = ["answer_set", "text"]

    def create(self, validated_data):
        answer_set = validated_data.pop('answer_set')
        question = Question.objects.create(**validated_data)
        for answer_data in answer_set:
            Answer.objects.create(question=question, **answer_data)
        return question


class QuestionsDetailSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"
