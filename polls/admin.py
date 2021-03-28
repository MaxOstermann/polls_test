from django.contrib import admin
from .models import Poll, Question, Choice, Attempt, Answer


class QuestionInline(admin.TabularInline):
    model = Question


class PollAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Attempt)
admin.site.register(Answer)
