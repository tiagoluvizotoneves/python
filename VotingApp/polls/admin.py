from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # Você também pode usar admin.StackedInline para um layout diferente
    model = Choice
    extra = 3  # Define quantos campos de escolha serão exibidos por padrão

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)