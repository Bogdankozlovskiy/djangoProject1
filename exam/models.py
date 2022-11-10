from django.db import models


class ExamTicket(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField("auth.User", through="exam.ExamTiketToUser")
    questions = models.ManyToManyField("exam.Question")


class ExamTiketToUser(models.Model):
    exam = models.ForeignKey("exam.ExamTicket", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)


class Mark(models.Model):
    exam_ticket_to_user = models.ForeignKey("exam.ExamTiketToUser", on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey("exam.Question", on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
