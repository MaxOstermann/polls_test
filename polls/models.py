from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    description = models.TextField()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    TYPES = [
        ('text', 'text'),
        ('one-ch', 'one choice'),
        ('many-ch', 'many choices'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPES,
        default='text',
    )
    question_text = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.choice_text


class Attempt(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='attempts',
        verbose_name='Пользователь', default=None, null=True, blank=True)
    interactive = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='attempts',
        verbose_name='Опрос')

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'

        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.user.username


class Answer(models.Model):
    attempt = models.ForeignKey(
        Attempt, on_delete=models.CASCADE, related_name='answers',
        verbose_name='Попытка')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='questions',
        verbose_name='Вопрос')
    choice = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='choices',
        verbose_name='Вариант ответа', default=None, null=True, blank=True)
    answer = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return "{} {}".format(self.user.username,
                              self.question.question_text)
