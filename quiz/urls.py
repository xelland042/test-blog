from django.urls import path

from quiz.views import quiz_categories, quiz_by_slug

app_name = 'quiz'

urlpatterns = [
    path('', quiz_categories, name='quiz-categories'),
    path('<slug:slug>', quiz_by_slug, name='categories-slug'),
]
