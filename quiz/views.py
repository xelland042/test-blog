from random import shuffle, sample

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from quiz.models import Answer, Question, Category


def quiz_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'quiz/categories_list.html', context=context)


def quiz_by_slug(request, slug):
    quiz_questions = Question.objects.filter(category__slug=slug)
    answers = Answer.objects.filter(question__in=quiz_questions)
    correct_answer = {}
    for i in answers:
        if i.is_correct:
            correct_answer[i.question.id] = i.id
    answers = list(answers)
    answers = sample(answers, len(answers))

    if request.method == 'POST':
        selected_answer = request.POST.dict()
        selected_answer.pop('csrfmiddlewaretoken')
        if len(selected_answer) == len(correct_answer):
            selected_answer = list(selected_answer.values())
            correct_answer = list(correct_answer.values())
            temp = False
            for i in range(0, len(selected_answer)):
                if int(selected_answer[i]) == correct_answer[i]:
                    temp = True
                else:
                    temp = False
            if temp:
                return render(request, 'quiz/congratulations.html')
        return render(request, 'quiz/failed.html')
    context = {
        'quiz_questions': quiz_questions,
        'answers': answers,
        'category_slug': slug,
    }
    return render(request, 'quiz/quiz_by_slug.html', context)
