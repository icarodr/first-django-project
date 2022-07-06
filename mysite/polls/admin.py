from dataclasses import fields
from django.contrib import admin
from .models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    
    
admin.site.register(Question, QuestionAdmin)

